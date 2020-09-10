const fs = require('fs')
const lines = fs.readFileSync('H.txt', 'utf-8').split('\n')
const numberItems = Number(lines[0])
const array = lines[1].split(' ').map(item => Number(item))

let maxResult = 0
let result = 1

for (let i = 0; i < numberItems - 1; i++) {

  if (array[i] < array[i + 1]) {
    result += 1
  } else {

    if (result > maxResult) {
      maxResult = result
    }
    result = 1
  }
}

console.log(maxResult)