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
    .then(removeExclusions)
    .then(removeGarbage)
    .then(countGroups)
    .then(() => originalInput)
    .then(removeExclusions)
    .then(selectGarbage)
}

function parseData(input) {
  return input.split('\n')
    .filter(line => line !== '')
    .map(line => line
      .replace('==', '===')
      .replace('!=', '!==')
      .split(' '))
}

function removeExclusions(data) {
  data = data.split('')
  let exclamationIndex = data.indexOf('!')
  while (exclamationIndex !== -1) {
    data.splice(exclamationIndex, 2)
    exclamationIndex = data.indexOf('!')
  }
  return data.join('')
}

function removeGarbage(data) {
  return data.replace(/<(.*?)>/g, '')
}

function countGroups(data) {
  let nestLevel = 0
  let score = 0

  for (let char of data) {
    if (char === ',') continue
    if (char === '{') {
      nestLevel++
      score += (nestLevel)
    } else if (char === '}') {
      nestLevel--
    }

  }

  return score
}

function selectGarbage(data) {
  const countCharacters = str =>
    str.slice(1, -1).length
  const sum = (a, b) => a + b

  return data.match(/<(.*?)>/g)
    .map(countCharacters)
    .reduce(sum, 0)

}
