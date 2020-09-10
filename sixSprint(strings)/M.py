with open('M.txt', 'r') as f:
    number_of_strings = int(f.readline())
    array_of_strings = []
    line = f.readline().strip()

    while line:
        array_of_strings.append(line)
        line = f.readline().strip()


def solution(array_of_strings):

    def first_part_suffix(array_of_strings):
        array_of_trimmed_strings = []

        for string in array_of_strings:
            repeated_letters = set()
            intermediate_string = ''

            for letter in string[::-1]:
                if letter not in repeated_letters:
                    repeated_letters.add(letter)
                    intermediate_string += letter

            array_of_trimmed_strings.append(intermediate_string)

        return array_of_trimmed_strings

    def second_part_kmp(array_of_trimmed_strings):
        first_string = array_of_trimmed_strings[0]
        result_substring = ''

        for i in range(len(first_string)):
            intermediate_counter = 0
            for string in array_of_trimmed_strings:
                if len(string) <= i or string[i] != first_string[i]:
                    break
                intermediate_counter += 1

            if intermediate_counter != len(array_of_trimmed_strings):
                break

            result_substring += first_string[i]

        return result_substring[::-1]

    array_of_trimmed_strings = first_part_suffix(array_of_strings)
    return second_part_kmp(array_of_trimmed_strings)


print(solution(array_of_strings))
