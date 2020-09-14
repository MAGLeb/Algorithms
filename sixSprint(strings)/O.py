f = open('O.txt', 'r')
string = f.readline().strip()


def solution(string):
    def kmp(s):
        p = [0 for _ in range(len(s))]
        for i in range(1, len(s)):
            j = p[i - 1]
            while j > 0 and s[i] != s[j]:
                j = p[j - 1]
            if s[j] == s[i]:
                j += 1
            p[i] = j
        return p

    index = 1
    while index < len(string) / 2:
        if not len(string) % index and index != 1:
            index += 1
            continue

        p_result = kmp(string[:index] + '#' + string)[index + 1:]
        print(p_result)
        counter = 0

        for iteration in range(index - 1, len(p_result), index):
            if p_result[iteration] == index:
                counter += 1
            else:
                break

        if counter == len(string) / index:
            return counter

        index += 1

    return 1


print(solution(string))
