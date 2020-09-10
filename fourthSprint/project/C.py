### 17 авг 2020, 17:45:38 33786829 C Python 3.7.3

def comparator(parent, child):
    name_exception = "kondratiy"
    parent_sum = parent[2]
    child_sum = child[2]
    index_parent = parent[1]
    index_child = child[1]
    parent = parent[0].split()
    child = child[0].split()
    parent_name = parent[0]
    child_name = child[0]
    counter_parent = 0
    counter_child = 0

    for letter in name_exception:
        if letter in parent_name:
            counter_parent += 1
        if letter in child_name:
            counter_child += 1

    if counter_child == counter_parent == len(name_exception):
        return index_child > index_parent
    elif counter_parent == len(name_exception):
        return False
    elif counter_child == len(name_exception):
        return True
    else:

        if parent_sum == child_sum:
            if parent_name == child_name:
                return index_child > index_parent
            else:
                return parent_name > child_name
        else:
            return parent_sum < child_sum


class Heap:
    def __init__(self):
        self.array = []

    def __repr__(self):
        return ' '.join(map(lambda x: x[0], self.array))

    def add_element(self, element):
        total_points = sum(filter(lambda x: x > 0, map(int, element.split()[1:])))
        self.array.append([element, len(self.array), total_points])

        if len(self.array) > 1:
            index_child = len(self.array)
            index_parent = int(index_child / 2)
            while comparator(self.array[index_child - 1], self.array[index_child - 1]):
                intermediate = self.array[index_parent - 1]
                self.array[index_parent - 1] = self.array[index_child - 1]
                self.array[index_child - 1] = intermediate
                index_child = index_parent
                index_parent = int(index_child / 2)
                if index_parent == 0:
                    break

    def return_sorted_array(self):
        result = []

        while self.array:
            result.append(self.array[0])
            self.array[0] = self.array[len(self.array) - 1]
            self.array.pop()
            self.heapify()

        return result

    def heapify(self):
        length = len(self.array)
        index_parent = 1

        while True:

            if length >= 2 * index_parent + 1:
                index_left = 2 * index_parent
                index_right = index_left + 1

                if comparator(self.array[index_left - 1], self.array[index_right - 1]):
                    if comparator(self.array[index_parent - 1], self.array[index_right - 1]):
                        min_index = index_right
                    else:
                        min_index = index_parent
                elif comparator(self.array[index_parent - 1], self.array[index_left - 1]):
                    min_index = index_left
                else:
                    min_index = index_parent

                if min_index == index_parent:
                    break

                intermediate = self.array[index_parent - 1]
                self.array[index_parent - 1] = self.array[min_index - 1]
                self.array[min_index - 1] = intermediate
                index_parent = min_index

            elif length >= 2 * index_parent:
                index_left = 2 * index_parent
                if comparator(self.array[index_parent - 1], self.array[index_left - 1]):
                    intermediate = self.array[index_parent - 1]
                    self.array[index_parent - 1] = self.array[index_left - 1]
                    self.array[index_left - 1] = intermediate

                break

            else:
                break


f = open('input.txt', 'r')

n = int(f.readline())
participants_points = Heap()

for _ in range(n):
    participants_points.add_element(f.readline().strip())

for item in participants_points.return_sorted_array():
    print(item[0])
