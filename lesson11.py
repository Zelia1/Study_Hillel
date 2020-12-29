# Задания
# data.json - файл с данными о некоторых математиках прошлого.
# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.
# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.
# 4. Написать функцию сортировки по количеству слов в поле "text"


import re
import json

# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.

def read_data(filename):
    with open(filename, "r", encoding="utf-8") as data_json:
        data = json.load(data_json)
    return data

filename = r"C:\Users\Zelia\PycharmProjects\Study_Hillel\StudiTest\data.json"

#######################################################################
# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).

def key_sorted_by_name(obj_dict):
    name = obj_dict["name"]
    if len(name.split(" ")) > 1:
        last_name = name.split()[-1]
    else:
        last_name = name
    return last_name
#
result_sorted_by_name = sorted(read_data(filename), key=key_sorted_by_name)

#######################################################################
# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.

def key_sorted_by_death_years(obj_dict):
    years = obj_dict["years"]
    life_data = re.findall(r"[A-Za-z0-9]", years)
    years_of_life = re.findall(r"[0-9]+", years)

    if life_data[-1] == "C":
        death_year = int(years_of_life[-1]) * -1
    else:
        death_year = int(years_of_life[-1])

    return death_year


result_sorted_by_death_years = sorted(read_data(filename), key=key_sorted_by_death_years)
# print(result_sorted_by_death_years)

#######################################################################
# 4. Написать функцию сортировки по количеству слов в поле "text"

def key_sorted_by_text(obj_dict):
    text = obj_dict["text"]
    text_list = len(text.split(" "))
    return text_list

result_sorted_by_len_text = sorted(read_data(filename), key=key_sorted_by_text)
