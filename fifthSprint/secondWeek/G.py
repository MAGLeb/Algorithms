with open('G.txt', 'r') as f:
  string = f.readline().strip()

def solution(string):
  dictionary = {}
  result = []

  for i in range(len(string) - 9): 
    if string[i:i+10] in dictionary:
      dictionary[string[i:i+10]] += 1
      if dictionary[string[i:i+10]] == 2:
        result.append(string[i:i+10])
    else:
      dictionary[string[i:i+10]] = 1

  result.sort()

  for item in result:
    print(item)

  return

solution(string)