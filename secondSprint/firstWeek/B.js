const fs = require('fs');

const lines = (fs.readFileSync('B.txt', 'utf-8')).split('\n');
const numberLines = Number(lines[0])
const array = lines[1].split(' ').map(item => Number(item))

function maxSum(array) {
  let result = 0
  let openTransaction = false
  let intermediate = 0

  for (let i = 0; i < array.length - 1; i++) {

    if (!openTransaction) {
      if (array[i] - array[i + 1] < 0) {
        intermediate = array[i]
        openTransaction = true
      }
    } else if (array[i] - array[i + 1] >= 0) {
      result += array[i] - intermediate
      openTransaction = false
      intermediate = 0
    }
  }

  if (openTransaction) {
    if (intermediate - array[numberLines - 1] < 0) {
      result += array[numberLines - 1] - intermediate
    }
  }

  return result
}

console.log(maxSum(array))