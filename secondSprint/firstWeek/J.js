const fs = require('fs')
const words = fs.readFileSync('J.txt', 'utf-8').split(' ')

console.log(words[words.length - 1].length)