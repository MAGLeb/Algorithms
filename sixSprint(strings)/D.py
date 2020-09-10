f = open('D.txt', 'r')
string_input = f.readline().strip()


def main(string):
    dictionary = {}

    for letter in string:
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1

    for key, value in dictionary.items():
        if value == 1:
            return key

    return None


result = main(string_input)

if result:
    print('YES')
    print(result)
else:
    print('NO')
