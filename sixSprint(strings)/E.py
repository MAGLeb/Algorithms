f = open('E.txt', 'r')
number_of_string = int(f.readline())

total_array = []

for _ in range(number_of_string):
    number_of_words = int(f.readline())
    total_array.append(f.readline().strip().split())


def main(array):

    result_array = []

    def recursive(current_string, array_of_arrays):
        if len(array_of_arrays) == 1:
            last_array = array_of_arrays[0]

            for word in last_array:
                result_array.append(current_string + ' ' + word)
        else:
            first_array = array_of_arrays[0]

            for word in first_array:
                if current_string:
                    recursive(current_string + ' ' + word, array_of_arrays[1:])
                else:
                    recursive(word, array_of_arrays[1:])

    recursive('', array)

    return sorted(result_array)


for item in main(total_array):
    print(item)
