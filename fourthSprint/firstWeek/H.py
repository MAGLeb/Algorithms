f = open('H.txt', 'r')
n = int(f.readline())
array = list(map(int, f.readline().strip().split()))
k = int(f.readline())

class Heap:
  def __init__(self, array=[]):
    self.result = [-1000]

    for i in range(len(array)):
      self.result.append(array[i])
      self.heapify()

  def heapify(self):
    for j in range(len(self.result), 0, -1):
      if len(self.result) - 1 >= j * 2:
        if self.result[j] > self.result[j * 2]:
          intermediate = self.result[j * 2]
          self.result[j * 2] = self.result[j]
          self.result[j] = intermediate
      if len(self.result) - 1 >= j * 2 + 1:
        if self.result[j] > self.result[j * 2 + 1]:
          intermediate = self.result[j * 2 + 1]
          self.result[j * 2 + 1] = self.result[j]
          self.result[j] = intermediate

  def fullSortedTree(self):
    result = []

    for i in range(len(self.result)):
      result.append(self.popLeft())
      self.heapify()

    return result[1:]

  def popLeft(self):
    return self.result.pop(0)

  def addElement(self, value):
    self.result.append(value)
    self.heapify()

  def fullTree(self):
    return self.result[1:]


def solution(array, k):
  heap = Heap()

  for i in range(len(array)):
    for j in range(i + 1, len(array)):
      heap.addElement(abs(array[i] - array[j]))

  return heap.fullSortedTree()[k - 1]

print(solution(array, k))