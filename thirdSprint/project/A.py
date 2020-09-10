### 2 июл 2020, 17:52:53 33577130	A Python 3.7.3
### 17 июл 2020, 22:55:26 33650776 A Python 3.7.3

### В 10 строк не получилось. Смотрю на код, сам удивляюсь. Если не сложно, объясни пожалуйста, что ты имел ввиду под этими фразами:
# 1). Или, чтобы решить задачу встроенным sort, то есть построить ключи. 
# (ключи построить? что загуглить или объясни словами пожалуйста)

# 2). Единственное что напрягает это куча памяти, выделенной на сортировку. Массив будет скопирован logn раз, классические реализации работают inplace. 
# (тут вообще не понял о чем идет речь, ниже привел строку к которой ты оставил комментарий, чтобы было удобно)
# return quiqeSort(left) + [mid] + quiqeSort(right) 


f = open('A.txt', 'r')

n = int(f.readline())
array = list(map(lambda x: list(map(int, list(x))), f.readline().strip().split()))



def checkValues(first, second):
  i = j = 0

  while True:
    if first[i] != second[j]:
      return first[i] > second[j]
    
    i = (i + 1) % len(first)
    j = (j + 1) % len(second)

    if not (i or j):
      return False
  



def quickSort(array):

  if len(array) < 2:
    return array

  mid = array[0]
  right = []
  left = []

  for item in array[1:]:
    if checkValues(item, mid):
      left.append(item)
    else:
      right.append(item)

  return quickSort(left) + [mid] + quickSort(right)



result = quickSort(array)
answer = ''.join(map(lambda x: ''.join(x), map(lambda x: map(str, x), result)))

print(result)





















# def checkValues(first, second):

#   min_lenght = len(first) if len(first) < len(second) else len(second)
#   max_lenght = len(first) if len(first) > len(second) else len(second)

#   for i in range(min_lenght):
#     if first[i] < second[i]:
#       return True
#     elif first[i] > second[i]:
#       return False

#   if len(first) == len(second):
#     return False

#   elif len(first) > len(second):
#     for i in range(min_lenght, max_lenght):
#       if first[i] == second[0]:
#         continue
#       elif first[i] < second[0]:
#         return True
#       else:
#         return False

#   else:
#     for i in range(min_lenght, max_lenght):
#       if second[i] == first[0]:
#         continue
#       elif second[i] > first[0]:
#         return True
#       else:
#         return False



# def boobleSort(array):
#   j = 0
  
#   while j != len(array):
#     for i in range(len(array) - j - 1):
#       if array[i][0] < array[i + 1][0]:
#         intermediate = array[i + 1]
#         array[i + 1] = array[i]
#         array[i] = intermediate
#       elif array[i][0] == array[i + 1][0]:
#         if len(array[i]) > len(array[i + 1]):
#           intermediate = array[i + 1]
#           array[i + 1] = array[i]
#           array[i] = intermediate

#     j += 1

#   return array

# def bitByBitBoobleSorting(array):
  
#   for i in range(len(array) - 1):
#     if len(array[i]) > 1 and len(array[i + 1]) > 1 and array[i][0] == array[i + 1][0]:

#       j = i
#       while True:
#         if array[j + 1][1] > array[j][1]:
#           intermediate = array[j + 1]
#           array[j + 1] = array[j]
#           array[j] = intermediate
#         elif array[j + 1][1] == array[j][1]:
#           if len(array[j]) == 2 and len(array[j + 1]) == 2:
#             continue
#           elif len(array[j]) == 3 and len(array[j + 1]) == 3:
#             if array[j + 1][2] > array[j][2]:
#               intermediate = array[j + 1]
#               array[j + 1] = array[j]
#               array[j] = intermediate
#           else:
#             if len(array[j + 1]) < len(array[j]):
#               intermediate = array[j + 1]
#               array[j + 1] = array[j]
#               array[j] = intermediate

#         j += 1

#         if j + 1 == len(array) or array[j + 1][0] != array[i][0]:
#           break

#   return array


# def checkValuesOld(first, second):

#   if first[0] < second[0]:
#     return True
#   elif first[0] > second[0]:
#     return False
#   else:
#     if len(second) == 1 and len(first) == 1:
#       return False
#     elif len(second) == 1 and len(first) == 2:
#       if first[1] >= second[0]:
#         return False
#       else:
#         return True
#     elif len(second) == 2 and len(first) == 1:
#       if second[1] >= first[0]:
#         return True
#       else:
#         return False
#     elif len(second) == 3 and len(first) == 1:
#       if second[1] > first[0] or (second[1] == first[0] and second[2] > first[0]):
#         return True
#       else:
#         return False
#     elif len(second) == 1 and len(first) == 3:
#       if first[1] > second[0] or (first[1] == second[0] and first[2] > second[0]):
#         return False
#       else:
#         return True

#     # lenght both >= 2
#     else:
#       if first[1] < second[1]:
#         return True
#       elif first[1] > second[1]:
#         return False
#       else:
#         if len(second) == 2 and len(first) == 2:
#           return False
#         elif len(second) == 2 and len(first) == 3:
#           if first[2] > second[0]:
#             return False
#           elif first[2] < second[0]:
#             return True
#           else:
#             if first[0] < first[1]:
#               return True
#             else:
#               return False
#         elif len(second) == 3 and len(first) == 2:
#           if second[2] > first[0]:
#             return True
#           elif second[2] < first[0]:
#             return False
#           else:
#             if first[0] <= first[1]:
#               return False
#             else:
#               return True


#         # lenght both eaqual 3
#         else:
#           if first[2] < second[2]:
#             return True
#           else:
#             return False

# def quickSortNew(array):
#   if len(array) < 2:
#     return array

#   mid = array[0]
#   right = []
#   left = []

#   for item in array[1:]:
#     if checkValuesOld(item, mid):
#       right.append(item)
#     else:
#       left.append(item)

#   return quickSortNew(left) + [mid] + quickSortNew(right)

# def quickSortOld(array):

#   if len(array) < 2:
#     return array

#   mid = array[0]
#   right = []
#   left = []

#   for item in array[1:]:
#     if len(item) < len(mid):
#       result = checkValuesOld(mid, item)
#       if result:
#         left.append(item)
#       else:
#         right.append(item)
#     else:
#       result = checkValuesOld(item, mid)
#       if result:
#         right.append(item)
#       else:
#         left.append(item)

#   return quickSortOld(left) + [mid] + quickSortOld(right)

# result_2 = quickSortNew(array)
# answer_2 = ''.join(map(lambda x: ''.join(x), map(lambda x: map(str, x), result_2)))

# print(result_2)
# print(answer == answer_2)

# for i in range(len(result)):
#   if result[i] != result_2[i]:
#     print(result[i], result_2[i])
#     break