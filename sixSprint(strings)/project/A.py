def solution(array):
    result_indexes = []

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if i == j:
                continue
            strings = [array[i] + array[j], array[j] + array[i]]

            for string in strings:
                if len(string) % 2:
                    string_length_half = int(len(string) / 2) + 1
                    string = string[:string_length_half] + string[string_length_half:][::-1]
                    z_fun_result = z_function(string)
                    # print(string, z_fun_result, string_length_half)
                    if z_fun_result[string_length_half] == string_length_half - 1:
                        result_indexes.append([i + 1, j + 1])
                else:
                    string_length_half = int(len(string) / 2)
                    string = string[:string_length_half] + string[string_length_half:][::-1]
                    z_fun_result = z_function(string)
                    # print(string, z_fun_result, string_length_half)
                    if z_fun_result[string_length_half] == string_length_half:
                        result_indexes.append([i + 1, j + 1])

    return result_indexes


def new_solution(array):
    result_indexes = []

    for i in range(len(array)):
        for j in range(len(array)):
            if i == j:
                continue
            string = array[i] + array[j]
            if is_palindrome(string):
                result_indexes.append([i+1, j+1])

    return result_indexes


def is_palindrome(string):
    l, r = 0, len(string) - 1

    while l < r:
        if string[l] == string[r]:
            l += 1
            r -= 1
        else:
            return False
    return True


def z_function(s):
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
    return z


def kmp(string):
    p = [0 for _ in range(len(string))]

    for i in range(1, len(string)):
        j = p[i - 1]
        while j > 0 and string[i] != string[j]:
            j = p[j - 1]
        if string[i] == string[j]:
            j += 1
        p[i] = j
    return p


f = open('A.txt', 'r')

number_of_string = int(f.readline())
array_of_string = []

for _ in range(number_of_string):
    array_of_string.append(f.readline().strip())

for result in new_solution(array_of_string):
    print(result[0], result[1])

# abbbba abbabb
# print(kmp('abbabb'))
# print(z_function('abbabb'))