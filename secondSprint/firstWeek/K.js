const fs = require('fs')
const lines = fs.readFileSync('K.txt', 'utf-8').split('\n')
const numberline = Number(lines[0].split(' ')[0])
let totalSum = Number(lines[0].split(' ')[1])

const array = lines[1].split(' ').map(item => Number(item)).sort((a, b) => a - b)

let result = 0

for (let i = 0; i < numberline; i++) {
  if (totalSum - array[i] >= 0) {
    totalSum -= array[i]
    result++
  } else {
    break
  }
}

console.log(result)