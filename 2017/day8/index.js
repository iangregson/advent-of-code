const path = require('path')
const { promisify } = require('util')
const { readFile } = require('fs')
const read = promisify(readFile)

module.exports = { run }

function run() {
  return read(path.join(__dirname, 'input.txt'), 'utf8').catch(console.error)
    .then(parseData)
    .then(createRegister)
    .then(findHighest)
}

function parseData(input) {
  return input.split('\n')
    .filter(line => line !== '')
    .map(line => line
      .replace('==', '===')
      .replace('!=', '!==')
      .split(' '))
}

function createRegister(data) {
  const register = {}
  let highestValueDuringProcessing = Number.MIN_SAFE_INTEGER
  const modify = (r, fn, param) => {
    switch (fn) {
      case 'inc':
        register[r] += parseInt(param, 10)
        break
      case 'dec':
        register[r] -= parseInt(param, 10)
        break
    }
  }
  data.forEach(([r, fn, param, i, testRegister, comparator, testValue]) => {
    !register[r] && (register[r] = 0)
    !register[testRegister] && (register[testRegister] = 0)
    let test = eval(`register['${testRegister}'] ${comparator} parseInt(testValue, 10)`)
    test && modify(r, fn, param)
    register[r] > highestValueDuringProcessing && (highestValueDuringProcessing = register[r])
  })
  console.log(highestValueDuringProcessing)
  return register
}

function findHighest(register) {
  const max = (a, b) => b > a ? b : a
  return Object.values(register).reduce(max, Number.MIN_SAFE_INTEGER)
}
