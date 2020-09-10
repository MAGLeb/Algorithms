f = open('workFromHome.txt', 'r')
number = int(f.readline())
result = []
interm = number

while interm > 2:
  result.append(str(interm % 2))
  interm = interm // 2

if interm == 2:
  result.append('01')
else:
  result.append(str(interm))

result = ''.join(result)[::-1]
print(result)
