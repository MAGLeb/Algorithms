# 13 сен 2020, 22:39:55	34421631 B Python 3.7.3
# 14 сен 2020, 15:23:06	34436366 B Python 3.7.3

class Node:
    def __init__(self, value=None, key=None, next_node=None):
        self.value = value
        self.key = key
        self.next_node = next_node

    def __str__(self):
        return self.value


class Hash:
    def __init__(self, max_table_size):
        self.p = 1
        while 2 ** (self.p + 1) < max_table_size:
            self.p += 1

        self.table = [0 for _ in range(2 ** self.p)]
        self.s = 2654435769
        self.simple = 997

    def hash_function(self, number):
        return (number * self.s % (2 ** 32)) >> (32 - self.p)

    def find_node_with_key(self, key, original_key):
        current_node = self.table[key]
        previous_node = None
        while True:
            if current_node.key == original_key or not current_node.next_node:
                break
            previous_node = current_node
            current_node = current_node.next_node

        return current_node, previous_node

    def put(self, key, value, original_key):
        if self.table[key] != 0:
            head = self.table[key]
            current_node = self.find_node_with_key(key, original_key)[0]

            if current_node.key == original_key:
                current_node.value = value
            else:
                new_node = Node(value, original_key, head)
                self.table[key] = new_node
        else:
            self.table[key] = Node(value, original_key)

    def get(self, key, original_key):
        if self.table[key] != 0:
            current_node = self.find_node_with_key(key, original_key)[0]
            if current_node.key == original_key:
                return current_node.value
            else:
                return '-1'
        else:
            return '-1'

    def delete(self, key, original_key):
        if self.table[key] != 0:
            current_node, previous_node = self.find_node_with_key(key, original_key)
            if current_node.key == original_key:
                if not previous_node:
                    if current_node.next_node:
                        self.table[key] = current_node.next_node
                    else:
                        self.table[key] = 0
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
    f = open('input.txt', 'r')
    number_strings = int(f.readline())
    hash_table = Hash(1000)

    for _ in range(number_strings):
        line = f.readline().strip()
        method, *values = line.split()
        original_key = int(values[0])
        key = hash_table.hash_function(original_key)

        if method == 'put':
            value = values[1]
            hash_table.put(key, value, original_key)
        elif method == 'get':
            print(hash_table.get(key, original_key))
        else:
            print(hash_table.delete(key, original_key))


solution()
