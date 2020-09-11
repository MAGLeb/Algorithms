f = open('N.txt', 'r')

number_of_strings = int(f.readline())
array_of_strings = []

for _ in range(number_of_strings):
    array_of_strings.append(f.readline().strip())


def unpacking(string):
    result_string = ''
    index = 0

    while index < len(string):
        if string[index].isdigit():
            # find all number in string, not only first digit of number
            number = string[index]
            i = 1
            while string[index + i].isdigit():
                number += string[index + i]
                i += 1

            # find index_close_bracket
            index_close_bracket = index + i
            counter_brackets = 1
            j = 1
            while counter_brackets != 0:
                if string[index_close_bracket + j] == ']':
                    counter_brackets -= 1
                elif string[index_close_bracket + j] == '[':
                    counter_brackets += 1
                index_close_bracket += 1

            result_string += int(number) * unpacking(string[index + 1 + i:index_close_bracket])
            index = index_close_bracket
        else:
            if string[index] == ']':
                index += 1
                continue
            result_string += string[index]
            index += 1

    return result_string


def find_general_prefix(array):
    first_string = array[0]
    counter = 0

    for index, letter in enumerate(first_string):
        intermediate_counter = 0
        for string in array:
            if letter == string[index]:
                intermediate_counter += 1
            else:
                break

        if intermediate_counter == len(array):
            counter += 1
        else:
            break

    return first_string[:counter]


print(find_general_prefix(list(map(unpacking, array_of_strings))))
