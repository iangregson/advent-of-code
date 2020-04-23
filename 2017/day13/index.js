const path = require('path')
const { promisify } = require('util')
const { readFile } = require('fs')
const read = promisify(readFile)

module.exports = { run }

function run() {
  return read(path.join(__dirname, 'input.txt'), 'utf-8')
    .then(calculateSeverity)
}


function calculateSeverity(data) {
  const input = data.trim();
  const guards = input.split('\n').map(s => s.match(/\d+/g).map(Number));
  const caughtByGuard = delay => ([d, r]) => (delay + d) % (2 * (r - 1)) === 0;
  const severity = delay => guards.filter(caughtByGuard(delay))
      .reduce((n, [d, r]) => n + d * r, 0);

  let delay = -1;
  while (guards.some(caughtByGuard(++delay)));
  return [severity(0), delay]
}

