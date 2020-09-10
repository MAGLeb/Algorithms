const fs = require('fs')
const lines = fs.readFileSync('G.txt', 'utf-8').split('\n')
const numberrow = Number(lines[0])
const numbercolumn = Number(lines[1])
const array = []

for (let i = 2; i < numberrow + 2; i++) {
  array.push(lines[i].split(' ').map(item => Number(item)))
}

let i = 0
let j = 0

let t = 0
let r = 0
let b = 0
let l = 0

while (true) {

  for (let w = l; w < numbercolumn - r; w++) {
    console.log(array[i][w])
    j = w
  }
  t++

  if (t + b === numberrow || r + l === numbercolumn) break

  for (let w = t; w < numberrow - b; w++) {
    console.log(array[w][j])
    i = w
  }
  r++

  if (t + b === numberrow || r + l === numbercolumn) break

  for (let w = numbercolumn - 1 - r; w >= l; w--) {
    console.log(array[i][w])
    j = w
  }
  b++

  if (t + b === numberrow || r + l === numbercolumn) break

  for (let w = numberrow - 1 - b; w >= t; w--) {
    console.log(array[w][j])
    i = w
  }
  l++

  if (t + b === numberrow || r + l === numbercolumn) break

}