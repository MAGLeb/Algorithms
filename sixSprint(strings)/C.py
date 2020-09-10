with open('C.txt', 'r') as f:
    string_input = f.readline().strip()


def main(string):
    dictionary = {}
    result_string = ''
    middle_letter = ''

    for letter in string:
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1

    dictionary = sorted(dictionary.items())

    for key, value in dictionary:
        if not middle_letter:
            if value % 2 == 1:
                middle_letter = key

        number_of_letters = int(value // 2)


        result_string += key * number_of_letters

    result_string += middle_letter + result_string[::-1]

    return result_string


print(main(string_input))
