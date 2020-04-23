const path = require('path')
const { readFileSync } = require('fs')

module.exports = { run }

function run() {
  const moves = readFileSync(path.join(__dirname, 'input.txt'), 'utf-8').trim().split(',')
  let programs = 'abcdefghijklmnop'.split('')
  // let moves = [
  //   's1',
  //   'x3/4',
  //   'pe/b'
  // ]
  // let programs = 'abcde'.split('')

  let memory = {}
  let result = null

  for (let i = 0; i < 1e9; i++) {
    if (memory[result]) {
      result = memory[result]
    } else {
      let input = programs.join('')
      programs = moves.reduce(doOperation, programs)
      result = programs.join('')
      memory[input] = result
    }
  }

  return Promise.resolve({ result })
}

function doOperation(programs, move) {
  const moves = {
    s: (move, programs) => {
      let arg = parseInt(move.replace('s', ''), 10)
      return programs.slice(0 - arg).concat(programs.slice(0, programs.length - arg))
    },
    x: (move, programs) => {
      let [fst, snd] = move.replace('x', '').split('/').map(Number)
      let prog1 = programs[fst]
      let prog2 = programs[snd]
      programs[fst] = prog2
      programs[snd] = prog1
      return programs
    },
    p: (move, programs) => {
      let [fst, snd] = move.replace('p', '').split('/')
      let pos1 = programs.indexOf(fst)
      let pos2 = programs.indexOf(snd)
      programs[pos2] = fst
      programs[pos1] = snd
      return programs
    }
  }

  return moves[move[0]](move, programs)
}
