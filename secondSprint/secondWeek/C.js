const fs = require('fs')
const n = Number(fs.readFileSync('A.txt', 'utf-8'))


const fibanachi = n => {

  if (n === 1 || n === 0) return 1

  let prev = 1
  let prevprev = 1
  let result = 0

  for (let i = 2; i <= n; i++) {
    result = prev + prevprev
    prevprev = prev
    prev = result
  }

  return result

}

console.log(fibanachi(n))

