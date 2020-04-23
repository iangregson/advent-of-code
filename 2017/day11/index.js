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
    .then(findMinimumSteps)
}

function parseData(data) {
  return data.trim().split(',')
}

function findMinimumSteps(directions) {
  const directionMap = { 'n': [-1,1,0], 'ne': [0,1,-1], 'se': [1,0,-1], 's': [1,-1,0], 'sw': [0,-1,1], 'nw': [-1,0,1] }
  const MAX = (a, b) => Math.max(a, b)
  const distance = x => x.map(Math.abs).reduce(MAX, Number.MIN_SAFE_INTEGER)

  let point = [0, 0, 0]
  let max = Number.MIN_SAFE_INTEGER

  for (let d of directions) {
    point = point.map((x, i) => x + directionMap[d][i])
    max = Math.max(max, distance(point))
  }

  return [distance(point), max]
}

