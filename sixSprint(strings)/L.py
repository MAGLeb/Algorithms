from functools import cmp_to_key

f = open('L.txt', 'r')
number_of_strings = int(f.readline())
array_of_strings = []

for _ in range(number_of_strings):
    line = f.readline().strip()
    array_of_strings.append(line)


def solution(array):
    dictionary = {}

    for item in array:
        if item in dictionary:
            dictionary[item] += 1
        else:
            dictionary[item] = 1

    def comparator(first, second):
        if first[1] == second[1]:
            if first[0] < second[0]:
                return -1
            else:
                return 1
        else:
            if first[1] > second[1]:
                return -1
            else:
                return 1

    result = sorted(dictionary.items(), key=cmp_to_key(comparator))[0][0]

    return result


print(solution(array_of_strings))
