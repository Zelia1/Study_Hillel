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
    if my_list_1[index] % 2 == 0:
        my_result.append(my_list_1[index])
for index in range(len(my_list_2)):
    if my_list_2[index] % 2 == 1:
        my_result.append(my_list_2[index])
print(my_result)
##################################################
# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
my_list = [1, 2, 3, 4]
new_list = my_list[1:]
new_list.append(my_list[0])
print(new_list)
##################################################
# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)
my_list = [1, 2, 3, 4]
element = my_list.pop(0)
my_list.append(element)
print(my_list)
##################################################
# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133.
my_string = '43 больше чем 34 но меньше чем 56'
my_list_digit = my_string.split()
res = 0
for index in range(len(my_list_digit)):
    if my_list_digit[index].isdigit():
        res += int(my_list_digit[index])
print(res)
##################################################
# 7. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
my_str = 'abcdefsku'
my_list = []
res = ''
if len(my_str) % 2 == 0:
    for index in range(len(my_str)):
        if index % 2 == 0:
            res = my_str[index] + my_str[index + 1]
            my_list.append(res)
else:
    for index in range(len(my_str)):
        if index % 2 == 1:
            res = my_str[index - 1] + my_str[index]
            my_list.append(res)
    res = my_str[-1] + '_'
    my_list.append(res)
print(my_list)
##################################################
# 8. Дана строка my_str в которой символы не повторяются и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить часть строки между этими символами.
# my_str = "My_long str", l_limit = "o", r_limit = "t" -> sub_str = "ng s"
my_str = "My_long str"
l_limit = "o"
r_limit = "t"
sub_str = my_str[my_str.find(l_limit) + 1:my_str.find(r_limit)]
print(sub_str)
##################################################
# 9. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
my_str = "My long string"
l_limit = "o"
r_limit = "g"
sub_str = my_str[my_str.find(l_limit) + 1:my_str.rfind(r_limit)]
print(sub_str)
##################################################
# 10. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
my_digit_list = [2, 4, 1, 5, 3, 9, 0, 7]
res = 0
for find_digit in range(1, len(my_digit_list) - 1):
    if my_digit_list[find_digit] > my_digit_list[find_digit - 1] + my_digit_list[find_digit + 1]:
        res += 1
print(res)
