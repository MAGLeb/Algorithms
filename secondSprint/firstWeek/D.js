const fs = require('fs')
const lines = fs.readFileSync('D.txt', 'utf-8').split('\n')
const weightBagPack = Number(lines[0])
const items = lines.splice(2).map(item => item.split(' ').map(item => Number(item)))


// const weightBagPack = 85
// const items = [[30,41], [30,50],[31,40], [222,3], [1100,1]]

const returnResult = (items, weightBagPack) => {
  const result = []
  const checkArray = []
  let item = [-1, -1]
  let index = -1

  while (true) {

    for (let i = 0; i < items.length; i++) {
      if (checkArray.includes(i)) {
        continue
      }

      if (items[i][1] <= weightBagPack) {
        if (items[i][0] > item[0]) {
          item = items[i]
          index = i
        } else if (items[i][0] === item[0]) {
          if (items[i][1] < item[1]) {
            item = items[i]
            index = i
          }
        }
      }
    }

    if (index != -1) {
      weightBagPack -= item[1]
      result.push(index)
      checkArray.push(index)
      item = [-1, -1]
      index = -1
    } else {
      break
    }
  }

  return result
}

console.log(returnResult(items, weightBagPack).sort().join(' '))