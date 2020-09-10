const fs = require('fs')
const lines = fs.readFileSync('J.txt', 'utf-8').split('\n')
let n = Number(lines[0])
const pos = Number(lines[1])
let result = false

function changeString(k) {

  if (n === 1) {
    return k === 2 ? !result : result
  }

  if (k <= 2 ** (n-1)) {
    n--
    return changeString(k)
  } else {
    result = !result
    n--
    return changeString(k - 2 ** (n))
  }
}



console.time('mark')
console.log(changeString(pos) ? 1 : 0)
console.timeEnd('mark')
