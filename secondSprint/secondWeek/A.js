const fs = require('fs')
const n = Number(fs.readFileSync('A.txt', 'utf-8'))

const fibanachi = n => n === 0 || n === 1 ? 1 : fibanachi(n - 1) + fibanachi(n - 2)

console.log(fibanachi(n))
