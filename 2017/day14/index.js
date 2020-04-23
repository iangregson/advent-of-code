  module.exports = { run }


function run() {
  const testInputHex = 'a0c2017'
  const inputKey = 'oundnydw'
  const rowCount = 128

  return Promise.resolve(inputKey)
    .then(key => makeRowIndexedKeys(key, rowCount))
    .then(keys => keys.map(getKnotHash))
    .then(hashes => hashes.map(hexToBin))
    .then(grid => ({
      part1: countUsedBlocks(grid),
      part2: countGroups(grid, rowCount)
    }))
}

function makeRowIndexedKeys(key, rowCount) {
  return new Array(rowCount).fill(0)
    .map((v, i) => `${key}-${i}`)
}

function hexToBin(hexStr) {
  const HEX = 16
  const BINARY = 2
  return hexStr.split('')
    .reduce((binaryStr, hexChar) => {
      binaryStr += parseInt(hexChar, HEX).toString(BINARY)
      return binaryStr
    }, '')
}

function countUsedBlocks(grid) {
  return grid.reduce((usedBlocks, binaryString) => {
    usedBlocks += binaryString.match(/1/g).length
    return usedBlocks
  }, 0)
}

function countGroups(grid, rowCount) {
  grid = grid.map(row => row.split('').map(Number))
  let groupNumber = 2

  for (let y = 0; y < rowCount; y++) {
    for (let x = 0; x < rowCount; x++) {
      let marked = markGroup(x, y)
      marked && groupNumber++
    }
  }
  return groupNumber -= 2

  function markGroup(x, y) {
    let row = grid[y]
    if (!row) return
    if (grid[y][x] === 1) {
      grid[y][x] = groupNumber
      markGroup(x, y - 1)
      markGroup(x, y + 1)
      markGroup(x - 1, y)
      markGroup(x + 1, y)
      return true
    }
    return false
  }
}

// Part 1
// take key and append -rowIndex
  // map all rowIndexed keys to knotHashes
// treating each hash as a hex sequence, convert to binary
// sum all the 1s

// Part 2
// Take the grid from part 1
// Iterate each character, recursively color neighbors, incrememting region count along the way
// Result is the region count
//
// 8108 is too high

// Knot hashing algorithm from https://pastebin.com/hH9w70GV

function getKnotHash(input) {
    const sequence = [...Array(256).keys()];
    let position = 0;
    let skip = 0;
    input = input.split("").map(c => c.charCodeAt(0)).concat([17, 31, 73, 47, 23]);

    let knot = tieKnot(sequence, input, 64);

    return getHexForArray(getDenseHash(knot));
}
function tieKnot(input, lengths, rounds = 1) {
    let result = input.slice();
    let position = 0;
    let skip = 0;

    for (let round = 0; round < rounds; round++) {
      for (let i = 0; i < lengths.length; i++) {
        let loopLength = lengths[i];
        let reversedSection = [];

        for (let at = position, x = 0; x < loopLength; x++) {
          at = (position + x) % result.length;
          reversedSection.unshift(result[at]);
        }

        for (let at = position, x = 0; x < loopLength; x++) {
          at = (position + x) % result.length;
          result[at] = reversedSection[x];
        }

        position = (position + loopLength + skip) % result.length;
        skip++;
      }
    }

    return result;
  }
function getDenseHash(sparseHash) {
    let result = [];

    for (let blockNr = 0; blockNr < 16; blockNr++) {
        let block = sparseHash.slice(blockNr * 16, (blockNr + 1) * 16);
        result[blockNr] = block.reduce((a,b) => a ^ b);
    }

    return result;
}
function getHexForArray(denseHash) {
    return denseHash
        .map(digit => ("0" + digit.toString(16)).substr(-2))
        .join("");
}
