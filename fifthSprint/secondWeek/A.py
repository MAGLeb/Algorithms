f = open('A.txt', 'r')

n = int(f.readline())

def solution(number):
  dictionary = set()
  while True:
    number = sum(list(map(lambda x: int(x) ** 2, list(str(number)))))

    if number != 1:
      if number in dictionary:
        return False
      else:
        dictionary.add(number)
    else:
      return True

                 
print(solution(n))