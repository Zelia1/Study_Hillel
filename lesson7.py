# 1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
# Задание можно выполнить и через обычный цикл и через генератор списков.
import random

random_value = [random.randint(1, 100) for value in range(20)]
print(random_value)
########################################################
# 2) Создать словарь triangle в который записать точки A B C (ключи),
# и их координаты - кортежи (значения),
# созданные случайным образом с помощью модуля random в диапазоне от -10 до 10 по каждой оси.
triangle = {'A': (random.randint(-10, 10),
                  random.randint(-10, 10),
                  random.randint(-10, 10)),
            'B': (random.randint(-10, 10),
                  random.randint(-10, 10),
                  random.randint(-10, 10)),
            'C': (random.randint(-10, 10),
                  random.randint(-10, 10),
                  random.randint(-10, 10))}
print(triangle)


########################################################
# 3) Создать функцию my_print, которая принимает в виде параметра строку и печатает ее
# с тремя символами * вначале и в конце строки.
# Пример:
# my_str = 'I'm the string'
# Печатает ***I'm the string***
def my_print(string):
    print(f'***{string}***')


line_here = input()
my_print(line_here)
########################################################
# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.
persons = [{"name": "John", "age": 15}, {"name": "Franc", "age": 15}, {"name": "Joi", "age": 32},
           {"name": "Jack", "age": 45}]
min_age = min([persons[man]["age"] for man in range(len(persons))])
man_name = max([len(persons[index]["name"]) for index in range(len(persons))])
persons_name = [persons[man]["name"] for man in range(len(persons)) if persons[man]["age"] == min_age]
max_name = [persons[index_name]["name"] for index_name in range(len(persons)) if
            len(persons[index_name]["name"]) == man_name]
average_amount = sum([persons[index_age]["age"] for index_age in range(len(persons))]) / len(persons)
print(*persons_name)
print(*max_name)
print(average_amount)
########################################################
# 5) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
my_dict_1 = {"name": "John", "age": 15, "header": "Chrome", "version": "2.0"}
my_dict_2 = {"name": "Joi", "age": 32, "country": "USA", "Interests": "fishing"}
my_list_key_in = []
for key in my_dict_1:
    if key in my_dict_2:
        my_list_key_in.append(key)
print(my_list_key_in)

my_list_not_key = []
for key in my_dict_1:
    if key not in my_dict_2:
        my_list_not_key.append(key)
print(my_list_not_key)

my_dict_3 = {}
for key in my_dict_1:
    if key not in my_dict_2:
        my_dict_3.update(key)
print(my_dict_3)