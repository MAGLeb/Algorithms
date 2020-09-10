f = open('C.txt', 'r')
n = int(f.readline())
array = list(f.readline().split())

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def returnString(self):
    results = []

    node = self
    while node:
      results.append(node.value)
      node = node.next

    return ' '.join(results)

class HashedDictionary:
  def __init__(self):
    self.dict = dict()

  def add(self, value, index):
    value = ''.join(sorted(value))

    if value in self.dict:
      node = self.dict[value]

      while node.next:
        node = node.next

      node.next = Node(index)
    else:
      self.dict[value] = Node(index)

  def __str__(self):
    results = []

    for key in self.dict:
      results.append(self.dict[key].returnString())

    return '\n'.join(results)

def main():
  hashDictionary = HashedDictionary()

  for index, item in enumerate(array):
    hashDictionary.add(item, str(index))

  print(hashDictionary)

if __name__ == "__main__":
  main()


