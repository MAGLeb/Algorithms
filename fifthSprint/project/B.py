class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return self.value


class Hash:
    def __init__(self, max_table_size):
        self.dictionary = {}
        self.s = 2654435769
        self.p = 1

        while 2 ** (self.p + 1) < max_table_size:
            self.p += 1

    def hash_function(self, number):
        return (number * self.s % (2 ** 32)) >> (32 - self.p)

    def to_do(self, command):
        method, *values = command.split()
        key = self.hash_function(int(values[0]))

        if method == 'put':
            value = values[1]
            self.put(key, value)
        elif method == 'get':
            print(self.get(key))
        else:
            print(self.delete(key))

    def put(self, key, value):
        if key in self.dictionary:
            node = self.dictionary[key]
            new_node = Node(value, node)
            self.dictionary[key] = new_node
        else:
            self.dictionary[key] = Node(value)

    def get(self, key):
        if key in self.dictionary:
            return self.dictionary[key]
        else:
            return '-1'

    def delete(self, key):
        if key in self.dictionary:
            del self.dictionary[key]
            return 'ok'
        else:
            return 'error'
        # if key in self.dictionary:
        #     node = self.dictionary[key]
        #     next_node = node.next_node
        #     if next_node is None:
        #         del self.dictionary[key]
        #     else:
        #         self.dictionary[key] = next_node
        #     return 'ok'
        # else:
        #     return 'error'


def solution():
    f = open('B.txt', 'r')
    number_strings = int(f.readline())
    hash_table = Hash(1025)

    for _ in range(number_strings):
        line = f.readline().strip()
        hash_table.to_do(line)


solution()
