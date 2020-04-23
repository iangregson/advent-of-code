const path = require('path')
const { promisify } = require('util')
const { readFile } = require('fs')
const read = promisify(readFile)

module.exports = { run }

function run() {
  return read(path.join(__dirname, 'input.txt'), 'utf8').catch(console.error)
    .then(parseData)
    // .then(doTheGoodStuff_part1)
    .then(doTheGoodStuff_part2)
}

function parseData(input) {
  return input.split('\t')
    .map(x => parseInt(x))
}

function doTheGoodStuff_part1(data) {
  let distributions = [];
  let count = 0
  let firstDistribution = data.join()
  let currentDistribution = ''
  let done = false

  const makeNextDistribution = data => {
    let highestNumber = data.reduce((acc, next) => next > acc ? next : acc, 0);
    let index = data.indexOf(highestNumber)
    data[index] = 0
    let blocks = new Array(highestNumber).fill(1)
      .forEach((block, i) => {
        let nextIndex = (index + i + 1) % data.length
        data[nextIndex] += block
      })
    return data
  };

  while (!done) {
    data = makeNextDistribution(data)
    currentDistribution = data.join()
    if (distributions.includes(currentDistribution)) {
      done = true
    } else {
      distributions.push(currentDistribution)
    }
    count++
  }

  return count
}

function doTheGoodStuff_part2(data) {
  let distributions = [];
  let count = 0
  let count2 = 0
  let firstDistribution = data.join()
  let currentDistribution = ''
  let done = false

  const makeNextDistribution = data => {
    let highestNumber = data.reduce((acc, next) => next > acc ? next : acc, 0);
    let index = data.indexOf(highestNumber)
    data[index] = 0
    let blocks = new Array(highestNumber).fill(1)
      .forEach((block, i) => {
        let nextIndex = (index + i + 1) % data.length
        data[nextIndex] += block
      })
    return data
  };

  while (!done) {
    data = makeNextDistribution(data)
    currentDistribution = data.join()
    if (distributions.includes(currentDistribution)) {
      let numberOfTimesSeen = distributions.filter(d => d === currentDistribution).length
      if (numberOfTimesSeen === 2) {
        done = true
      } else {
        count++
        distributions.push(currentDistribution)
      }
    } else {
      distributions.push(currentDistribution)
    }
  }

  return count
}

