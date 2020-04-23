const path = require('path')
const { promisify } = require('util')
const { readFile } = require('fs')
const read = promisify(readFile)

module.exports = { run }

function run() {
  let originalInput = ''
    return read(path.join(__dirname, 'input.txt'), 'utf8').catch(console.error)
      .then(input => {
      originalInput = input
      return input
    })
    .then(parseData)
    .then(doGoodStuff)
    .then(() => doGoodStuffPt2(originalInput))
}

function parseData(data) {
  const parseInteger = i => parseInt(i, 10)
  return data.replace(/\s/g, '').split(',').map(parseInteger)
}

function range(n) {
  return [...Array(n).keys()]
}

function doGoodStuff(lengths) {
  const flatten = (acc, x) => acc.concat(x)
  let sequence = range(256)

  let skipSize = 0
  let currentStartPosition = 0

  const getNextPosition = (n, startPosition) => {
    let nextPosition = parseInt(n) + parseInt(startPosition)
    if (nextPosition >= sequence.length) {
      nextPosition = nextPosition % sequence.length
    }
    return nextPosition
  }
  const nextStartPosition = (currentPosition, skipSize, currentLength) => {
    return (currentPosition + skipSize + currentLength) % sequence.length
  }

  lengths.forEach(l => {
    let subSequence = []
    let subSeqPos = []
    let position = currentStartPosition
    for (let n in range(l)) {
      position = getNextPosition(n, currentStartPosition)
      subSequence.push(sequence[position])
    }
    position = currentStartPosition
    subSequence.reverse()
    for (let n in range(l)) {
      position = getNextPosition(n, currentStartPosition)
      sequence[position] = subSequence[n]
    }
    currentStartPosition = nextStartPosition(currentStartPosition, skipSize, l)
    skipSize++
  })
  return sequence[0] * sequence[1]
}

function doGoodStuffPt2(data) {
  const input = '157,222,1,2,177,254,0,228,159,140,249,187,255,51,76,30'
  // let lengths = [...data.toString(8)].map(x => x.charCodeAt(0))
  let lengths = data.split('').map(x => x.charCodeAt(0))
  let numbers = [...Array(256).keys()]
  let pos = 0, skip = 0
  let denseHash = []

  lengths.push(17, 31, 73, 47, 23)

  for (let i = 0; i < 64; i++) {
    for (const len of lengths) {
      if (len > 1) {
        numbers = [...numbers.slice(pos), ...numbers.slice(0, pos)]
        numbers = [...numbers.slice(0, len).reverse(), ...numbers.slice(len)]
        numbers = [...numbers.slice(-pos), ...numbers.slice(0, -pos)]
      }
      pos = (pos + len + skip++) % 256
    }
  }

  for (let i = 0; i < 16; i++) {
    const o = numbers.slice(i * 16, i * 16 + 16).reduce((a, b) => a ^ b)
    denseHash.push(o)
  }

  const zeropad = n => ("0" + n).substr(-2)
  const result = denseHash.map(n => zeropad(n.toString(16))).join("")
  return result
}
// Thanks to _A4_ for part 2!
// 2b0c9cc0449507a0db3babd57ad9e8d8
