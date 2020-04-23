const { readFileSync } = require('fs')
const path = require('path')

const input = readFileSync(path.join(__dirname, 'input.txt'), 'utf-8').trim()

const instructions = input.split('\n')
  .map(line => {
    let [ command, args ] = line.replace(/\s+/, '|').split('|')
    args.length > 1 && (args = args.split(/\s/))
    args = [...args]
    return { command, args }
  })

const registers = {}
const playHistory = []
const recoverHistory = []
let pos = 0

const get = (value, registers) => {
  if (!Number.isNaN(parseInt(value))) return parseInt(value)
  else {
    let v = parseInt(registers[value])
    return v || 0
  }
}

const commands = {
  'set': args => {
    let [ register, value ] = args
    registers[register] = get(value, registers)
    pos++
  },
  'add': args => {
    let [ register, value ] = args
    registers[register] += get(value, registers)
    pos++
  },
  'mul': args => {
    let [ register, value ] = args
    registers[register] = registers[register] * get(value, registers)
    pos++
  },
  'mod': args => {
    let [ register, value ] = args
    registers[register] = registers[register] % get(value, registers)
    pos++
  },
  'snd': args => {
    let [ register ] = args
    playHistory.push(registers[register])
    pos++
  },
  'rcv': args => {
    let [ register ] = args
    if (registers[register] && registers[register] !== 0) {
      if (playHistory.length > 0) console.log(playHistory.pop())
    }
    pos++
  },
  'jgz': args => {
    let [ register, offset ] = args
    if (registers[register] && registers[register] > 0) {
      pos += parseInt(offset)
    } else {
      pos++
    }
  }
}

function run() {
  while(pos < instructions.length) {
    let i = instructions[pos]
    commands[i.command](i.args)
  }
  return Promise.resolve({ recoverHistory, playHistory })
}

module.exports = { run }
