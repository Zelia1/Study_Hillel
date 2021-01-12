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


def write_quotes_csv(number_of_quotes):
    with open(r"C:\Users\Zelia\PycharmProjects\Study_Hillel\StudiTest\quotes.csv", "w",
              encoding="utf-8") as write_quotes:

        url = "http://api.forismatic.com/api/1.0/"

        params = {"method": "getQuote",
                  "format": "json",
                  "key": 1,
                  "lang": "ru"}

        data_quote = []
        data_author = []
        data_link = []

        count = 0
        while count != number_of_quotes:
            params["key"] = random.randint(0, 999999)
            result = requests.get(url, params=params)
            quote = result.json()
            quote_text = quote["quoteText"]
            quote_author = quote["quoteAuthor"]
            quote_link = quote["quoteLink"]
            if quote_author != "" and quote_text not in data_quote:
                data_quote.append(quote_text)
                data_author.append(quote_author)
                data_link.append(quote_link)
                count += 1

        headers = ["Author", "Quote", "URL"]
        data = {}
        data_list = []
        for i in range(len(data_author)):
            data[headers[0]] = data_author[i]
            data[headers[1]] = data_quote[i]
            data[headers[2]] = data_link[i]
            data_copy = data.copy()
            data_list.append(data_copy)

        sorted_data = sorted(data_list, key=lambda sort: sort[headers[0]])

        fieldnames = data_list[0].keys()
        writer = csv.DictWriter(write_quotes, fieldnames=fieldnames, delimiter=";")
        writer.writerows(sorted_data)


number_of_quotes = 10
write_quotes_csv(number_of_quotes)


##########################################################################################
# 2. Дан файл authors.txt
# 2.1) написать функцию, которая считывает данные из этого файла,
# возвращая СПИСОК тех строк в которых есть полная дата, писатель и указание на его день рождения или смерти.
# Например: 26th February 1802 - Victor Hugo's birthday - author of Les Misérables.


def read_and_filter(path):
    with open(path, "r", encoding="utf-8") as read_file:

        data = []

        for line in read_file.readlines():
            data.append(line)
        new_data = "".join(data).split("\n")
        reg_exp = r"\b\w+[ ]\w+[ ]\d+[\s-]{3}[A-Za-z0-9]+"
        final_data = []

        for i in range(len(new_data)):
            result = re.findall(reg_exp, new_data[i])
            if len(result) != 0:
                for x in range(1):
                    if ("birthday" in new_data[i].lower()) or ("death" in new_data[i].lower()):
                        final_data.append(new_data[i])
    return final_data


file_path = r"C:\Users\Zelia\PycharmProjects\Study_Hillel\StudiTest\authors.txt"


##########################################################################################
# 2.2) Написать функцию, которая принимает список строк полученной в пункте 2.1, и возвращает список словарей
# в формате {"name": name, "date": date},
# где name это имя автора, а date - дата из строки в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)


def creat_dict_authors(data):
    reg_exp_name = r"[-\w.']+"
    reg_exp_date = r"[0-9]+"
    month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November",
                  "December"]

    temporary_dict = {}
    dict_author = []

    for list_index in range(len(result_filter)):
        name_find = re.findall(reg_exp_name, result_filter[list_index])
        date_find = re.findall(reg_exp_date, result_filter[list_index])
        if len(date_find[0]) < 2:
            old_digit = str(date_find.pop(0))
            new_digit = "0" + old_digit
            date_find.insert(0, new_digit)


        if "birthday" in name_find:
            search_index = name_find.index("birthday")
            temporary_dict["name"] = " ".join(name_find[4:search_index])

        elif "death" in name_find:
            search_index = name_find.index("death")
            temporary_dict["name"] = " ".join(name_find[4:search_index])

        for index_month in range(len(month_list)):
            if month_list[index_month] in name_find:
                if index_month < 9:
                    date_find.insert(1, "0" + str(index_month + 1))
                    temporary_dict["date"] = "/".join(date_find[:3])
                    copy_dict = temporary_dict.copy()
                    dict_author.append(copy_dict)
                if index_month >= 9:
                    date_find.insert(1, str(index_month + 1))
                    temporary_dict["date"] = "/".join(date_find[:3])
                    copy_dict = temporary_dict.copy()
                    dict_author.append(copy_dict)
    return dict_author


result_filter = read_and_filter(file_path)


##########################################################################################
# 2.3) Написать функцию, которая сохраняет результат пункта 2.2 в json файл.

def write_dict_in_json_file(path, dict):
    with open(path, "w") as write_in_json:
        json.dump(dict, write_in_json, indent=2)


path_in_json = r"C:\Users\Zelia\PycharmProjects\Study_Hillel\StudiTest\Authors.json"
dict_authors = creat_dict_authors(result_filter)
write_dict_in_json_file(path_in_json, dict_authors)
