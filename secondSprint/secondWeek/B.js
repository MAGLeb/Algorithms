const fs = require('fs')
const n = Number(fs.readFileSync('A.txt', 'utf-8'))

const memory = []

const fibanachi = n => {

  if (memory[n] === undefined) {
    if (n === 1 || n === 0) {
      memory[n] = 1
    } else {
      memory[n] = fibanachi(n - 1) + fibanachi(n - 2)
    }
  }
  return memory[n]

}

console.log(fibanachi(n))