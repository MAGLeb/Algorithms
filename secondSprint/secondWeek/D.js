const fs = require('fs')
const n = Number(fs.readFileSync('A.txt', 'utf-8'))

function fibanachi(n) {
  let result = 0
  let prev = 1
  let prevprev = 1

  for (let i = 2; i <= n; i++) {
    result = (prev + prevprev) % 10
    prevprev = prev
    prev = result
  }

  return result
}

console.log(fibanachi(n))