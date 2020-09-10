f = open('P.txt', 'r')

n = int(f.readline())
keys = list(f.readline().strip().split())
m = int(f.readline())
values = list(f.readline().strip().split())


def solution(keys, values):
  result_dict = dict()

  for i in range(len(keys)):
    if len(values) <= i:
      result_dict[keys[i]] = None
    else:
      result_dict[keys[i]] = values[i]

  def printSolution(dictionary):
    for key, value in dictionary.items():
      print('{}: {}'.format(key, value))

  printSolution(result_dict)

solution(keys, values)
