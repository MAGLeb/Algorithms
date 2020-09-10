const fs = require('fs')
const lines = fs.readFileSync('E.txt', 'utf-8').split('\n')
const children = lines[1].split(' ').map(item => Number(item)).sort((a,b) => a-b)
const cookies = lines[3].split(' ').map(item => Number(item)).sort((a,b) => a-b)

let result = 0
let i = 0
let j = 0

while (true) {

  if (children[i] > cookies[cookies.length] || j === cookies.length || i === children.length) {
    break
  }

  if (children[i] <= cookies[j]) {
    i++
    result++
  }
  j++
}

// for (let i = 0; i < children.length; i++) {

//   if (children[i] > cookies[cookies.length]) {
//     break
//   }

//   for (let j = 0; j < cookies.length; j++) {
//     if (children[i] <= cookies[j]) {
//       cookies.splice(j, 1)
//       result++
//       break
//     }
//   }
// }

console.log(result)