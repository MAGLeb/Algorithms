# 13 сен 2020, 20:45:29 34416742 A Python 3.7.3

from string import digits, ascii_letters

BASE = digits + ascii_letters
B = 62


def main():
    data_base = {}
    f = open('input.txt', 'r')
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

        else:
            key = decoder(protocol + '//' + str(link) + '.' + domain)
            if key in data_base:
                print(' '.join(data_base[key]))
            else:
                print('error')

        line = f.readline().strip()


def decoder(string):
    decoded_string = 0

    for letter in string:
        pos = BASE.find(letter)
        decoded_string = B * decoded_string + pos

    return decoded_string


def encoder(num):
    r = num % B
    q = num // B
    encoded_string = BASE[r]

    while q > 0:
        r = q % B
        q //= B
        encoded_string = BASE[r] + encoded_string

    return encoded_string


main()
