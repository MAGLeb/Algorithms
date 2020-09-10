const fs = require('fs');

const lines = (fs.readFileSync('G.txt', 'utf-8')).split('\n');
const digits = Number(lines[0])

let max_value = '9'
let min_value = '1'

while (max_value.length !== digits) {
    max_value += '9'
    min_value += '0'
}

if (digits === 1) {
    console.log(0)
} else {
    for (let number = Number(min_value); number < Number(max_value) + 1; number++) {
        let even_sum = 0
        let odd_sum = 0

        for (let j = 0; j < digits; j += 2) {
            even_sum += Number(String(number)[j])
            if (j + 1 < digits) {
                odd_sum += Number(String(number)[j + 1])
            }
        }
        if (even_sum == odd_sum) {
            console.log(number)
        }
    }
}