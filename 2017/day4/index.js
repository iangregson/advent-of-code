const path = require('path')
const { promisify } = require('util')
const { readFile } = require('fs')
const read = promisify(readFile)

module.exports = { run }
function run() {
  return read(path.join(__dirname, 'input.txt'), 'utf8').catch(console.error)
    .then(parseData)
    .then(data => data.filter(validate))
    .then(data => data.length)
}

function parseData(input) {
  return input.split('\n').filter(passphrase => passphrase !== '')
}

function validate(passphrase) {
  const sortWords = word => word.split('').sort().join('')
  let words = passphrase.split(' ')
    .map(sortWords)
  let wordSet = new Set(words)
  return wordSet.size === words.length
}

