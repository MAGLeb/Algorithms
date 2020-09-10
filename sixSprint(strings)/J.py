f = open('J.txt', 'r')
big_string = f.readline().strip()
number_strings = int(f.readline())
array_of_strings = []

line = f.readline().strip()

while line:
    array_of_strings.append(line)
    line = f.readline().strip()


def solution(string, array):
    def z_function(s, length):
        n = len(s)
        z = [0 for _ in range(n)]
        l, r, k = 0, 0, 0
        for i in range(1, n):
            if i > r:
                l, r = i, i
                while r < n and s[r - l] == s[r]:
                    r += 1
                z[i] = r - l
                r -= 1
            else:
                k = i - l
                if z[k] < r - i + 1:
                    z[i] = z[k]
                else:
                    l = i
                    while r < n and s[r - l] == s[r]:
                        r += 1
                    z[i] = r - l
                    r -= 1
        for index, value in enumerate(z):
            if value != length:
                z[index] = 0

        return z[length+1:]

    def recursive(total_z_array):
        if len(total_z_array) == 0:
            return True

        for i in range(len(total_z_array)):
            for j in range(len(total_z_array[i])):
                number_letters = total_z_array[i][j]
                if number_letters != 0:
                    if recursive(total_z_array[number_letters:]):
                        return True

        return False

    z_array = []

    for item in array:
        if len(z_array) == 0:
            z_array = list(map(lambda x: [x], z_function(item + '#' + string, len(item))))
            continue
        else:
            z_result = z_function(item + '#' + string, len(item))

            for index, value in enumerate(z_result):
                if value != 0:
                    if z_array[index] == 0:
                        z_array[index] = [value]
                    else:
                        z_array[index] += [value]

    if recursive(z_array):
        return 'YES'
    else:
        return 'NO'


print(solution(big_string, array_of_strings))

