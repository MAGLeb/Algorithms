const fs = require('fs')
const lines = fs.readFileSync('L.txt', 'utf-8').split('\n')
const number = Number(lines[0])
const array = lines[1].split(' ').map(item => Number(item))

// const number = 5
// const array = [1, 2, 3, 100, 1]

const func = (array) => {
    let i = 0

    while (i < number - 1) {

        if (array[i] === 0 || i > number - 1) {
            return false
        }
        
        i += array[i]

    }
    return true
}

console.log(func(array) ? 'True' : 'False')