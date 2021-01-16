# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат (см. урок 12).
# Надо получить ровно столько не повторяющихся цитат с данными и сохранить их в csv файл
# (имя файла сделать параметром по умолчанию).
# Заголовки файла:
# Author, Quote, URL. Если автор не указан, цитату не брать.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).

import requests
import random
import csv
import re
import json


def read_and_save_qoute(number):
    url = "http://api.forismatic.com/api/1.0/"

    params = {"method": "getQuote",
              "format": "json",
              "key": 1,
              "lang": "ru"}

    data_list = []

    count = 0
    while count != number:
        data = {}
        params["key"] = random.randint(0, 999999)
        result = requests.get(url, params=params)
        quote = result.json()
        if quote["quoteAuthor"] != "" and quote["quoteText"] not in data_list:
            data["Author"] = quote["quoteAuthor"]
            data["Quote"] = quote["quoteText"]
            data["URL"] = quote["quoteLink"]
            data_copy = data.copy()
            data_list.append(data_copy)
            count += 1

    return data_list


number_of_quotes = 10
data_to_sort = read_and_save_qoute(number_of_quotes)
sorted_data = sorted(data_to_sort, key=lambda sort: sort["Author"])


def write_quotes_csv(data):
    with open(r"C:\Users\Zelia\PycharmProjects\Study_Hillel\StudiTest\quotes.csv", "w",
              encoding="utf-8") as write_quotes:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(write_quotes, fieldnames=fieldnames, delimiter=";")
        writer.writerows(data)


write_quotes_csv(sorted_data)


##########################################################################################
# 2. Дан файл authors.txt
# 2.1) написать функцию, которая считывает данные из этого файла,
# возвращая СПИСОК тех строк в которых есть полная дата, писатель и указание на его день рождения или смерти.
# Например: 26th February 1802 - Victor Hugo's birthday - author of Les Misérables.


def read_and_filter(path):
    with open(path, "r", encoding="utf-8") as read_file:

        data = []

        for line in read_file.readlines():
            if ("birthday" in line.lower()) or ("death" in line.lower()):
                data.append(line.split("\n"))

    return data


##########################################################################################
# 2.2) Написать функцию, которая принимает список строк полученной в пункте 2.1, и возвращает список словарей
# в формате {"name": name, "date": date},
# где name это имя автора, а date - дата из строки в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)


def creat_dict_authors(data):
    reg_exp_date = r"[0-9]+"
    month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November",
                  "December"]

    temporary_dict = {}
    data_authors = []

    for list_index in range(len(data)):
        data_for_processing = str(data[list_index]).split("-")
        temporary_dict["author"] = data_for_processing[1].split("'")[0].strip()
        date_list = data_for_processing[0][2:].split()
        for i in range(len(month_list)):
            if month_list[i] in date_list:
                if i < 9:
                    date_list[1] = "0" + str(i + 1)
                else:
                    date_list[1] = str(i + 1)
        temporary_dict["date"] = " ".join(date_list)
        new_date = "/".join(re.findall(reg_exp_date, temporary_dict["date"]))
        if len(new_date) < 10:
            new_date = "0" + new_date
        temporary_dict["date"] = new_date
        final_dict = temporary_dict.copy()
        data_authors.append(final_dict)

    return data_authors


##########################################################################################
# 2.3) Написать функцию, которая сохраняет результат пункта 2.2 в json файл.

def write_dict_in_json_file(path, data):
    with open(path, "w") as write_in_json:
        json.dump(data, write_in_json, indent=2)


file_path = r"C:\Users\Zelia\PycharmProjects\Study_Hillel\StudiTest\authors.txt"
data_from_file = read_and_filter(file_path)
path_in_json = r"C:\Users\Zelia\PycharmProjects\Study_Hillel\StudiTest\Authors.json"
data_to_write = creat_dict_authors(data_from_file)
write_dict_in_json_file(path_in_json, data_to_write)
