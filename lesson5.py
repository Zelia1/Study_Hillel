# 1. Дано целое число (int). Определить сколько нулей в этом числе.
my_number = 208405480
res = str(my_number).count('0')
print(res)

# Вариант 2
# my_str = ''
# for zero in str(my_number):
#     if zero == '0':
#         my_str += '0'
# res = my_str.count('0')
# print(res)

# Вариан 3
# my_number = 208405480
# my_number_list = []
# my_number_list.extend(str(my_number))
# res = 0
# for zero in range(len(my_number_list)):
#     if my_number_list[zero] == '0':
#         res += 1
# print(res)
##################################################
# 2. Дано целое число (int). Определить сколько нулей в конце этого числа.
my_number1 = 876240236470000000
res = 0
while my_number1 % 10 == 0:
    res += 1
    my_number1 //= 10
print(res)

# Вариант 2
# my_number1 = 876240236470000000
# my_str = str(my_number1)
# res = 0
# for zero in range(1, len(my_str) + 1):
#     if my_str[-zero] == '0':
#         res += 1
#     else:
#         break
# print(res)
##################################################
# 3a. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.
my_list_1 = [12, 4, 11, 'ds', 'vg', 3, 7]
my_list_2 = [3, 90, 'dd', 'm7', 'f', 9]
my_result = []
for index in range(len(my_list_1)):
    if index % 2 == 1:
        my_result.append(my_list_1[index])
for index in range(len(my_list_2)):
    if index % 2 == 0:
        my_result.append(my_list_2[index])
print(my_result)
##################################################
# 3b. Даны списки my_list_1 и my_list_2. Создать список my_result в который
# вначале поместить четные элементы (ИМЕННО ЭЛЕМЕНТЫ) из my_list_1 и потом нечетные элементы из my_list_2.
# my_list_1 = [1,2,3,4,5], my_list_2 = [10, 15, 20, 25] -> my_result [2, 4, 15, 25]
my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = [10, 15, 20, 25]
my_result = []
for index in range(len(my_list_1)):
    if index % 2 == 1:
        my_result.append(my_list_1[index])
for index in range(len(my_list_2)):
    if index % 2 == 0:
        my_result.append(my_list_2[index])
print(my_result)
