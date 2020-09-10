with open('B.txt', 'r') as f:
    first_name = f.readline().strip()
    second_name = f.readline().strip()


def main(first, second):
    one_mistake = False

    if len(first) - len(second) > 1:
        return 'FAIL'
    elif len(first) - len(second) == 0:
        for letter_first, letter_second in zip(first, second):
            if letter_first != letter_second:
                if one_mistake:
                    return 'FAIL'
                one_mistake = True

        return 'OK'
    else:
        if len(first) - len(second) < 0:
            intermediate = first
            first = second
            second = intermediate

        for i in range(len(second)):
            if first[i] != second[i]:
                if one_mistake:
                    return 'FAIL'
                first = first[:i] + first[i + 1:]
                one_mistake = True

        return 'OK'


print(main(first_name, second_name))
