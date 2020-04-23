const path = require('path')
const { promisify } = require('util')
const { readFile } = require('fs')
const read = promisify(readFile)

module.exports = { run }

function run() {
  return read(path.join(__dirname, 'input.txt'), 'utf8').catch(console.error)
    .then(parseData)
    .then(doTheGoodStuff)
}

function parseData(input) {
  return input.split('\n')
    .filter(line => line !== '')
    .map(x => parseInt(x, 10))
}

function doTheGoodStuff(arr) {
  let count = -1
  let nextIndex = 0
  let currentValue = null

  while (currentValue !== undefined) {
    nextIndex += currentValue
    currentValue = arr[nextIndex]

    // Part 1
    // arr[nextIndex]++

    // Part 2
    if (arr[nextIndex] >= 3) arr[nextIndex]--
    else arr[nextIndex]++
    count++
  }
  return count
}
