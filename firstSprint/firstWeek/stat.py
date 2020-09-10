# lenghtArray = input()

# array = list(map(int, input().split(' ')))

# array = list(map(int, '-2 -1 -3 -1 2 -7 -8 -9 -10 -234 25 24 -24 -25 90 -89 -2 2 3 4 5 -3 -3 -1 -2 -1 3 -1 -2 -7 -8 -9 -10 -234 25 24 -24 -25 90 -89 -2 2 3 4 5 -3 -3 -1'.split(' ')))

# negative = []
# positive = list()
# count = 0

# for item in array:
#   negative.append(item) if item < 0 else positive.append(item)
#   count += 1

# negative = sorted(negative)
# positive = sorted(positive, reverse=True)
# result = 0



# for numPos in positive:
#   for i in range(len(negative)):
#     for j in range(i, len(negative) - i):
#       count += 1
#       intermediateSum = numPos + negative[i] + negative[j]
#       imtermediateCom = numPos * negative[i] * negative[j]
#       if(intermediateSum == 0 and (imtermediateCom % 2 == 0) and imtermediateCom > 0 and imtermediateCom > result):
#         result = imtermediateCom
        

# print(count)
# print(result if result != 0 else -1)




# lenghtArray = input()

# array = list(map(int, input().split(' ')))

# test = '-7 -8 -9 -10 -234 25 24 -24 -25 90 -89 -2 2 3 4 5 -3 -3 -1'

array = sorted(list(map(int, '-2 -1 3 -1 -2'.split(' '))))

result = -1

for i in range(len(array) - 2):
  start = i + 1
  end = len(array) - 1

  while start < end:

    intermediateSum = array[start] + array[end] + array[i]

    if intermediateSum > 0:
      end -= 1
    elif intermediateSum == 0:
      intermediateCom = array[start] * array[end] * array[i]
      start += 1

      if intermediateCom % 2 == 0 and intermediateCom > 0 and intermediateCom > result:
        result = intermediateCom
    else: start += 1

print(result)

