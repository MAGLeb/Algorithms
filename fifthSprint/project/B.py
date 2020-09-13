# 13 сен 2020, 22:39:55	34421631 B Python 3.7.3

class Node:
    def __init__(self, value=None, key=None, next_node=None):
        self.value = value
        self.key = key
        self.next_node = next_node

    def __str__(self):
        return self.value


class Hash:
    def __init__(self, max_table_size):
        self.dictionary = {}
        self.s = 2654435769
        self.p = 1
        self.simple = 997

        while 2 ** (self.p + 1) < max_table_size:
            self.p += 1

    def hash_function(self, number):
        return (number * self.s % (2 ** 32)) >> (32 - self.p)

    def to_do(self, command):
        method, *values = command.split()
        original_key = int(values[0])
        key = self.hash_function(original_key)

        if method == 'put':
            value = values[1]
            self.put(key, value, original_key)
        elif method == 'get':
            print(self.get(key, original_key))
        else:
            print(self.delete(key, original_key))

    def put(self, key, value, original_key):

        if key in self.dictionary:
            head = self.dictionary[key]
            current_node = self.dictionary[key]
            while True:
                if current_node.key == original_key or not current_node.next_node:
                    break
                current_node = current_node.next_node

            if current_node.key == original_key:
                current_node.value = value
            else:
                new_node = Node(value, original_key, head)
                self.dictionary[key] = new_node
        else:
            self.dictionary[key] = Node(value, original_key)

    def get(self, key, original_key):
        if key in self.dictionary:
            current_node = self.dictionary[key]
            while True:
                if not current_node.next_node or current_node.key == original_key:
                    break
                current_node = current_node.next_node
            if current_node.key == original_key:
                return current_node.value
            else:
                return '-1'
        else:
            return '-1'

    def delete(self, key, original_key):
        if key in self.dictionary:
            current_node = self.dictionary[key]
            previous_node = None

            while True:
                if not current_node.next_node or current_node.key == original_key:
                    break
                previous_node = current_node
                current_node = current_node.next_node
            if current_node.key == original_key:
                if not previous_node:
                    if current_node.next_node:
                        self.dictionary[key] = current_node.next_node
                    else:
                        del self.dictionary[key]
                elif not current_node.next_node:
                    previous_node.next_node = None
                else:
                    previous_node.next_node = current_node.next_node

                return 'ok'
            else:
                return 'error'
        else:
            return 'error'


def solution():
    f = open('B.txt', 'r')
    number_strings = int(f.readline())
    hash_table = Hash(1000)

    for _ in range(number_strings):
        line = f.readline().strip()
        hash_table.to_do(line)


solution()
