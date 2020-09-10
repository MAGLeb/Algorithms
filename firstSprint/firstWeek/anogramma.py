from collections import Counter

def is_anagram(word1, word2):
    return Counter(word1) == Counter(word2)

s1 = 'q1111wer'
s2 = 'rew1111q'

def make_dict(word):
  result = {}

  for letter in word:
    if(letter in result):
      result[letter] += 1
    else:
      result[letter] = 1

  return result

print(is_anagram(s1, s2))
print(make_dict(s1) == make_dict(s2))
