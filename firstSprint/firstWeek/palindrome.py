import re


string = re.sub(r'\W', '', 'A man, a plan, a canal: Panama').lower()


print(string == string[::-1])
