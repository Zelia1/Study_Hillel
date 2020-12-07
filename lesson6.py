# #1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate.
my_list = ['qwe', 'rty', 'asd', 'zxc', 'fgh']
new_my_list = []
for index, value in enumerate(my_list):
    if index % 2 == 0:
        new_my_list.append(value[::-1])
    else:
        new_my_list.append(value)
print(new_my_list)
##########################################################
# #2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".
my_list = ['qwe', 'aty', 'asd', 'cxc', 'fagh', 'andj']
new_my_list = [value for index, value in enumerate(my_list) if value[0] == 'a']
print(new_my_list)
# Вариант 2
# new_my_list = []
# for index, value in enumerate(my_list):
#     if value[0] == 'a':
#         new_my_list.append(value)
# print(new_my_list)
##########################################################
# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.
my_list = ['qwe', 'aty', 'asd', 'cxc', 'fagh', 'andj']
new_my_list = [value for index, value in enumerate(my_list) if 'a' in value]
print(new_my_list)
##########################################################
# 4. Дан список my_list в котором могум быть как строки (type str) так и целые числа (type int).
# Создать новый список в который поместить только строки из my_list.
my_list = ['qwe', 3, 'aty', 'asd', 1, 'cxc', 'fagh', 'andj', 10]
new_my_list = [value for index, value in enumerate(my_list) if type(my_list[index]) == str]
print(new_my_list)
##########################################################
# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.
my_str = 'dahjufddufkmdaikfhq[k'
my_list = [my_str[index] for index, value in enumerate(my_str) if my_str.count(value) < 2]
print(my_list)
#Вариант 2
# my_list = []
# for i in range(len(my_str)):
#     if my_str.count(my_str[i]) < 2:
#         my_list.append(my_str[i])
#print(my_list)
##########################################################
# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
my_str_1 = 'djkjdsayyiq12'
my_str_2 = 'djoiim1utqreasde'
res = list(set(my_str_1).intersection(set(my_str_2)))
print(res)
##########################################################
# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
my_str_1 = 'djkjdsayyifq1'
my_str_2 = 'djoiimuftq1reeg3'
my_str_list1 = [my_str_1[index] for index, value in enumerate(my_str_1) if my_str_1.count(value) < 2]
my_str_list2 = [my_str_2[index] for index, value in enumerate(my_str_2) if my_str_2.count(value) < 2]
my_set_1 = set(''.join(my_str_list1))
my_set_2 = set(''.join(my_str_list2))
res = list(my_set_1.intersection(my_set_2))
print(res)
##########################################################
# 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
# Фамилия
# Имя
# Возраст
# Проживание
#     Страна
#     Город
#     Улица
# Работа
#     Наличие
#     Должность
work = {'Availability': 'student',
        'Position': 'wizard'}
location = {'Country': 'England',
            'City': 'Little Winging',
            'Street': '4 Privet Drive'}
person = {'l_name': 'Potter',
          'f_name': 'Harry',
          'age': '14',
          'location': location,
          'Work': work}
print(person['location'])
##########################################################
# 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# придумать и указать граммы для продуктов):
# Составляющие
#     Коржи
#         Мука
#         Молоко
#         Масло
#         Яйцо
#     Крем
#         Сахар
#         Масло
#         Ваниль
#         Сметана
#     Глазурь
#         Какао
#         Сахар
#         Масло
cakes = {'flour': '3kg',
         'milk': '2 liters',
         'butter': '600 gram',
         'eggs': '10'}
cream = {'sugar': '2kg',
         'butter': '1kg',
         'vanilla': '200 gram',
         'sour cream': '1.5 liter'}
glaze = {'cocoa': '1kg',
         'sugar': '1.5kg',
         'butter': '500 gram'}
IT_cake = {'cakes': cakes,
           'cream': cream,
           'glaze': glaze}
print(IT_cake)
