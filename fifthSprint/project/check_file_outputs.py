first_filename = 'output_2.txt'
second_filename = 'test_1_expected.txt'

f_1 = open(first_filename, 'r')
f_2 = open(second_filename, 'r')
counter = 1

line_1 = f_1.readline().strip()
line_2 = f_2.readline().strip()

while line_1:
    if line_1 != line_2:
        print(line_1, line_2, counter)
        break

    counter += 1
    line_1 = f_1.readline().strip()
    line_2 = f_2.readline().strip()
