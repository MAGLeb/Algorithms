class Heap:
  def __init__(self):
    self.array = []
  
  def __repr__(self):
    return ' '.join(map(lambda x: x[0], self.array))

  def addElement(self, item):
    self.array.append([item, len(self.array)])

    if len(self.array) > 1:
      indexChild = len(self.array)
      indexParent = int(indexChild / 2)
      while self.comporator(self.array[indexParent - 1], self.array[indexChild - 1]):
        interm = self.array[indexParent - 1]
        self.array[indexParent - 1] = self.array[indexChild - 1]
        self.array[indexChild - 1] = interm
        indexChild = indexParent
        indexParent = int(indexChild / 2)
        if indexParent == 0:
          break

  def returnSortedArray(self):
    result = []

    while True:
      if len(self.array) == 1:
        result.append(self.array[0])
        break
      result.append(self.array[0])
      self.array[0] = self.array.pop()
      self.heapify()

    return result      

  def heapify(self):
    length = len(self.array)
    indexParent = 1

    while True:

      if length >= 2 * indexParent + 1:
        indexLeft = 2 * indexParent
        indexRight = indexLeft + 1

        if self.comporator(self.array[indexLeft - 1], self.array[indexRight - 1]):
          if self.comporator(self.array[indexParent - 1], self.array[indexRight - 1]):
            minIndex = indexRight
          else:
            minIndex = indexParent
        elif self.comporator(self.array[indexParent - 1], self.array[indexLeft - 1]):
          minIndex = indexLeft
        else:
          minIndex = indexParent

        if minIndex == indexParent:
          break

        interm = self.array[indexParent - 1]
        self.array[indexParent - 1] = self.array[minIndex - 1]
        self.array[minIndex - 1] = interm
        indexParent = minIndex

      elif length >= 2 * indexParent:
        indexLeft = 2 * indexParent
        if self.comporator(self.array[indexParent - 1], self.array[indexLeft - 1]):
          interm = self.array[indexParent - 1]
          self.array[indexParent - 1] = self.array[indexLeft - 1]
          self.array[indexLeft - 1] = interm
        
        break

      else:
        break

  def comporator(self, parent, child):
    name = 'kondratiy'
    index_parent = parent[1]
    index_child = child[1]
    parent = parent[0].split()
    child = child[0].split()
    parent_name = parent[0]
    child_name = child[0]
    counter_parent = 0
    counter_child = 0

    for letter in name:
      if letter in parent_name:
        counter_parent += 1
      if letter in child_name:
        counter_child += 1

    if counter_child == counter_parent == len(name):
      if index_child > index_parent:
        return True
      else:
        return False
    elif counter_parent == len(name):
      return False
    elif counter_child == len(name):
      return True
    else:
      parent_sum = sum(filter(lambda x: x > 0, map(int, parent[1:])))
      child_sum = sum(filter(lambda x: x > 0, map(int, child[1:])))

      if parent_sum == child_sum:
        if parent_name == child_name:
          if index_child > index_parent:
            return True
          else:
            return False
        elif parent_name > child_name:
          return True
        else:
          return False
      elif parent_sum < child_sum:
        return True
      else:
        return False

      


f = open('C.txt', 'r')

n = int(f.readline())
array = Heap()

for _ in range(n):
  array.addElement(f.readline().strip())

for item in array.returnSortedArray():
  print(item[0])