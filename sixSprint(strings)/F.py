f = open('F.txt', 'r')

total_string = f.readline().strip()
string_from = f.readline().strip()
string_to = f.readline().strip()


def main(string, string_from, string_to):
    result_string = ''

    def knm(string_with_substring):
        p = [0 for _ in range(len(string_with_substring))]

        for i in range(1, len(string_with_substring)):
            j = p[i - 1]
            while j > 0 and string_with_substring[i] != string_with_substring[j]:
                j = p[j - 1]
            if string_with_substring[i] == string_with_substring[j]:
                j += 1
            p[i] = j
        return p

    full_string = string_from + '#' + string
    p_function = knm(full_string)

    i = len(p_function) - 1
    while i >= len(string_from) + 1:
        if p_function[i] == len(string_from):
            result_string += string_to[::-1]
            i -= len(string_from)
        else:
            result_string += full_string[i]
            i -= 1

    return result_string[::-1]


print(main(total_string, string_from, string_to))
