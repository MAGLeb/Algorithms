# f = open('L.txt', 'r')

# total_money = int(f.readline())
# n = int(f.readline())
# coins_array = list(map(int, f.readline().strip().split()))

total_money = 4
coins_array = [1,2,3]

total_result = 0

def recursive(reducer, array):
  total = 0

  for coin in array:
    if reducer + coin < total_money:
      total += recursive(reducer + coin, array)
    elif reducer + coin == total_money:
      total += 1

  return total



for i, coin in enumerate(coins_array):
  total_result += recursive(coin, coins_array[i:])

print(total_result)












