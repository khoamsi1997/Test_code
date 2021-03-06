# # # #input strl = 'JhonDipPeta'
# # # #output = Dip
# # #
# # #
# strl1 = input(str('inout somethings: '))
# y = len(strl1)//2
# z = strl1[y - 1] + strl1[y] + strl1[y + 1]
# print(z)

# strl1 = input(str('inout somethings: '))
# y = len(strl1)//2
# print(y)
# z = strl1[y - 1: y + 2]
# print(z)

# s1 = input('input somethings: ')
# s2 = input('input somethings: ')
# print(s1[0:len(s1)//2] + s2 + s1[len(s1)//2:len(s1)])

# s1 = "America"
# s2 = "Japan"
# y = len(s1)
# x = len(s2)
#
# z = s1[0] + s2[0] + s1[y//2] + s2[x//2] + s1[y-1] + s2[x-1]
#
# print(z)

# str.lower # .upper
# str1 = 'PyNaTive'
# z = ''
# y = ''
# for i in str1:
#     if i.islower():
#         z += i
#     else:
#         y += i
# print(z + y)

# str1 = 'PyNaTive'
# z = ''
# y = ''
# for i in range(0, len(str1)):
#     if ord(str1[i]) in range(97, 122):
#         z += str1[i]
#     else:
#         y += str1[i]
# print(z + y)

# str1 = "P@#yn26at^&i5ve"
# chars = 0
# digits = 0
# symbol = 0
# for i in range(0, len(str1)):
#     if str1[i].isalpha():
#         chars += 1
#         print(chars)
#         print(str1[i])
#     elif str1[i].isnumeric():
#         digits += 1
#     else:
#         symbol += 1
#
# print(chars)
# print(digits)
# print(symbol)

def count(s1, s2):
    y = len(s2)
    for i in (s1):
        y -= 1
        print(i, end='')
        print(s2[y], end='')


# s1 = input('Please input somethings : ')
# s2 = input('Please input somethings : ')
# y = len(s2)
#
# if (s2[0 : y] in s1):
#     print('True')
# else:
#     print('False')

# str1 = "English = 78 Science = 83 Math = 68 History = 65 Lib =70 Japanese= 100"
#
# n = ''
# sum = 0
# for i in str1:
#     if i.isnumeric():
#         n += i
#
# y = len(n)//2
# for i in range(0, len(n), 2):
#     sum += int(n[i] + n[i+1])
#
# sum1 = str(sum)
# average = str(sum/y)
#
# print('sum is'' ' + sum1)
# print('average is'' '+average)

# str1 = input('Please input something: ')
# z = ''
# for i in range(len(str1)-1, 0, -1):
#     z += str1[i]
# print(z + str1[0])

# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# str2 = input('enter str: ')
# ls = str1.split()
# pos = 0
# for index in range(len(ls) - 1, -1, -1):
#     if str2 == ls[index]:
#         pos = index
#         break
# len_ls = 0
# for index in range(0, pos):
#     len_ls += len(ls[index]) + 1
# print(len_ls)

# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# str2 = input('')
# s = len(str2)
# for index in range(len(str1)-1, -1, -1):
#     if str1[index:index + s] == str2:
#         print(index)
#         break


# str1 = "English = 100 Science = 83 Math = 68 History = 65 lib = 100"
# count = 0
# ls = str1.split()
# sum_number = 0
# for number in ls:
#     if number.isnumeric():
#         count += 1
#         sum_number += int(number)
# average = str(sum_number/count)
# print('sum is %d' % sum_number)
# print('average is ' + average)

# str1 = 'Emma-is-a-data-scientist'
# ls_str1 = str1.split('-')
# print(ls_str1)
# for words in ls_str1:
#     print(words)

# str_list = ['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']
# cl_List = []
# for words in str_list:
#     if words != '' and words != None:
#         cl_List.append(words)
# print(cl_List)

# str1 = "/*Jon is @developer & musician"
# clStr = ''
#
# for alp in str1:
#     if alp.isalpha() or alp.isspace():
#         clStr += alp
# lsStr = clStr.split()
# print(' '.join(lsStr))
from typing import List


def str1(a):
    clStr = ''
    for alp in a:
        if not alp.isalpha() and not alp.isnumeric() and not alp.isspace():
            clStr += '#'
        else:
            clStr += alp
    return clStr


def num_str(a):
    nums = ''
    for val in a:
        if val.isnumeric():
            nums += val
    return


ls_str = "Emma25 is1 Data scientist50 and AI Expert".split()
print(ls_str)


def check(ls_spl):
    lst = []
    for val in ls_spl:
        count_alp = 0
        count_num = 0
        for alp in val:
            if alp.isalpha():
                count_alp += 1
            elif alp.isnumeric():
                count_num += 1
            if count_num != 0 and count_alp != 0:
                lst.append(val)
                break
    return lst



