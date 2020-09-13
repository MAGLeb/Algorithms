# 13 сен 2020, 20:45:29 34416742 A Python 3.7.3

import math

BASE = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
B = 62


def main():
    data_base = {}

    f = open('20 (2)', 'r')
    # w = open('output_1.txt', 'w')
    number_strings = int(f.readline())
    line = f.readline().strip()

    for _ in range(number_strings):
        method, url, *content = line.split()
        protocol, link = url.split('//')
        link, domain = link.split('.')

        if method.lower() == 'post':
            encoded_url = encoder(len(data_base))
            key = protocol + '//' + str(encoded_url) + '.' + domain
            data_base[decoder(key)] = content
            print(key)
            # w.writelines(key + '\n')

        else:
            key = decoder(protocol + '//' + str(link) + '.' + domain)
            if key in data_base:
                print(' '.join(data_base[key]))
                # w.writelines(' '.join(data_base[key]) + '\n')
            else:
                print('error')
                # w.writelines('error\n')

        line = f.readline().strip()


def decoder(string):
    decoded_string = 0

    for letter in string:
        pos = BASE.find(letter)
        decoded_string = B * decoded_string + pos

    return decoded_string


def encoder(num):
    r = num % B
    q = math.floor(num / B)
    encoded_string = BASE[r]

    while q > 0:
        r = q % B
        q = math.floor(q / B)
        encoded_string = BASE[r] + encoded_string

    return encoded_string


main()
