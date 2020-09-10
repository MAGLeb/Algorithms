import math

BASE = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
B = 62


def main():
    data_base = {}

    f = open('A.txt', 'r')
    number_strings = int(f.readline())
    line = f.readline().strip()

    for _ in range(number_strings):
        method, url, *content = line.split()
        protocol, link = url.split('//')
        *link, domain = link.split('.')

        if method.lower() == 'post':
            encoded_url = encoder(len(data_base))
            key = protocol + '//' + str(encoded_url) + '.' + domain
            data_base[key] = content
            print(key)
        else:
            decoded_url = decoder('.'.join(link))
            key = protocol + '//' + str(decoded_url) + '.' + domain
            if key in data_base:
                print(' '.join(data_base[key]))
            else:
                print('error')

        line = f.readline()


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
