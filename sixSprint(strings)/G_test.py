f = open('G.txt', 'r')
w = open('output.txt', 'w')
digits = int(f.readline())
max_value = '9'
min_value = '1'
result = []

while len(max_value) != digits:
    max_value += '9'
    min_value += '0'

if digits == 1:
    print(0)
else:
    for number in range(int(min_value), int(max_value) + 1):
        even_sum = 0
        odd_sum = 0
        for j in range(0, digits, 2):
            even_sum += int(str(number)[j])
            if j + 1 < digits:
                odd_sum += int(str(number)[j + 1])

        if even_sum == odd_sum:
            w.write(str(number) + '\n')