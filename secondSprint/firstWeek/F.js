const fs = require('fs')
const lines = fs.readFileSync('F.txt', 'utf-8').split('\n')
const numberLines = Number(lines[0])
const stringLength = Number(lines[1])
const array = []
let result = 0

for (let i = 2; i < numberLines + 2; i++) {
  array.push(lines[i])
}

for (let i = 0; i < stringLength; i++) {
  for (let j = 0; j < numberLines - 1; j++) {
    if (array[j][i] > array[j + 1][i]) {
      result++
      break
    }
  }
}

console.log(result)