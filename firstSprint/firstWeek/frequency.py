f = open('frequency.txt', 'r')
word = f.readline()

dict_let_freq = dict()

for letter in word:
  if letter in dict_let_freq:
    dict_let_freq[letter] += 1
  else:
    dict_let_freq[letter] = 1

dict_freq_let = dict()

for key in dict_let_freq:
  value = dict_let_freq[key]

  if value in dict_freq_let:
    dict_freq_let[value].append(key)
  else:
    dict_freq_let[value] = [key]

result = ''

for item in sorted(dict_freq_let.items(), reverse=True):
  count = item[0]
  letters = sorted(item[1])

  for letter in letters:
    result += letter * count

print(result)