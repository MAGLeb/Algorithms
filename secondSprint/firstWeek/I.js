const fs = require('fs')
const lines = fs.readFileSync('I.txt', 'utf-8').split('\n')
const numbers = Number(lines[0])
const array = lines[1].split(' ').map(item => Number(item)).sort((a,b) => b-a)

const func = (array) => {
  let a = 0
  let b = 0
  let i = 0

  while (i !== numbers - 2) {

    if (a <= b) {
      a += array[i]
    } else {
      b += array[i]
    }

    i++
  }

  const first = array[i]
  const second = array[i + 1]

  if (a + first === b + second) {
    a += first
    b += second
  } else if (a + second === b + first) {
    a += second
    b += first
  } else if (a < b) {
    a += first + second
  } else {
    b += first + second
  }

  return a === b ? 'True' : 'False'
}

const newFunc = (array) => {
  let sum = array.reduce((acc, item) => acc + item) / 2
  let j = 0
  let i = 0

  while (j !== numbers) {
    
    let acc = 0

    for (let i = j; i < numbers - 1; i++) {
      if (acc + array[i] <= sum) {
        acc += array[i]
        if (acc === sum) {
          return true
        }
      } 
    }
    j++
    
  }

  return false
}

console.log(newFunc(array))
