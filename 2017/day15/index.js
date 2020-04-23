module.exports = { run }

function run() {
  const factorA = 16807
  const factorB = 48271

  const multipleA = 4
  const multipleB = 8

  const divisor = 2147483647
  const epoch = 5000000

  const nextValue = (x, factor) => (x * factor) % divisor
  const checkCriteria = (value, multipleOf) => value % multipleOf === 0

  let A = 65
  let B = 8921

  let countMatches = 0

  let queueA = []
  let queueB = []

  while (queueA.length < epoch || queueB.length < epoch) {
    A = nextValue(A, factorA)
    B = nextValue(B, factorB)
    if (checkCriteria(A, multipleA)) queueA.push(A)
    if (checkCriteria(B, multipleB)) queueB.push(B)
    console.log(queueA.length, queueB.length)
  }

  for (let i = 0; i < epoch; i++) {
    let A = queueA.shift()
    let B = queueB.shift()
    if (match(A, B)) countMatches++
  }
  return Promise.resolve(countMatches)

  function match(a, b) {
    let binaryA = parseInt(a, 10).toString(2).slice(-16)
    let binaryB = parseInt(b, 10).toString(2).slice(-16)
    return binaryA === binaryB
  }
}
