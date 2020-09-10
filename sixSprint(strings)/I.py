f = open('I.txt', 'r')
number_of_strings = int(f.readline())
array_of_strings = []
line = f.readline().strip()

while line:
    array_of_strings.append(line)
    line = f.readline().strip()


def solution(array_of_strings):
    first_string = array_of_strings[0]
    counter = 0

    for i in range(len(first_string)):
        intermediate_counter = 0
        for string in array_of_strings:
            if len(string) <= i or string[i] != first_string[i]:
                break
            intermediate_counter += 1

        if intermediate_counter != len(array_of_strings):
            break

        counter += 1

    return counter


print(solution(array_of_strings))
