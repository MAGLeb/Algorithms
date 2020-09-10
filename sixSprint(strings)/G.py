f = open('G.txt', 'r')
digits = int(f.readline())


def solution(digits):
    result = []
    if digits == 1:
        print(0)
        return

    if digits == 2:
        for i in range(1, 10):
            print(str(i) + str(i))
        return

    max_value = '9'
    min_value = '1'

    if digits % 2:
        while len(max_value) != digits - 1:
            max_value += '9'
            min_value += '0'
        digits -= 1
        max_value = int(max_value)
        min_value = int(min_value)

        for number in range(min_value, max_value + 1):
            odd_sum = 0
            even_sum = 0
            for digit_index in range(0, digits, 2):
                even_sum += int(str(number)[digit_index])
                if digit_index + 1 < digits:
                    odd_sum += int(str(number)[digit_index + 1])

            diff = even_sum - odd_sum
            if 0 >= diff > -10:
                result.append(str(number) + str(abs(diff)))
                # print(str(number) + str(abs(diff)))

    else:
        while len(max_value) != digits - 2:
            max_value += '9'
            min_value += '0'
        digits -= 2
        max_value = int(max_value)
        min_value = int(min_value)

        for number in range(min_value, max_value + 1):
            odd_sum = 0
            even_sum = 0

            for digit_index in range(0, digits, 2):
                even_sum += int(str(number)[digit_index])
                if digit_index + 1 < digits:
                    odd_sum += int(str(number)[digit_index + 1])

            diff = even_sum - odd_sum
            if abs(diff) < 10:
                i = 0
                if diff > 0:
                    while diff + i < 10:
                        result.append(str(number) + str(i) + str(diff + i))
                        # print(str(number) + str(i) + str(diff + i))
                        i += 1
                else:
                    diff = abs(diff)
                    while diff + i < 10:
                        result.append(str(number) + str(diff + i) + str(i))
                        # print(str(number) + str(diff + i) + str(i))
                        i += 1

    return result

# solution(digits)


f_read = open('output.txt', 'r')
line = f_read.readline().strip()
check_result = []

while line:
    check_result.append(line)
    line = f_read.readline().strip()


total_result = solution(digits)

for index, number in enumerate(total_result):
    # print(number)
    if number != check_result[index]:
        print(index, number, check_result[index])
        break