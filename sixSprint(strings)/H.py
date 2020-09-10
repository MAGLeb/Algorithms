with open('H.txt', 'r') as f:
    string_of_brackets = f.readline().strip()


def solution(brackets):
    counter = 0

    for bracket in brackets:
        if bracket == '(':
            counter += 1
        else:
            counter -= 1

    if counter % 2:
        print('NO')
    else:
        print('YES')
        print(abs(int(counter / 2)))


solution(string_of_brackets)
