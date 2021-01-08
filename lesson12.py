# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат (см. урок 12).
# Надо получить ровно столько не повторяющихся цитат с данными и сохранить их в csv файл
# (имя файла сделать параметром по умолчанию).
# Заголовки файла:
# Author, Quote, URL. Если автор не указан, цитату не брать.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).

import requests
import random
import csv


def write_quotes(number_of_quotes):
    with open(r"C:\Users\Zelia\PycharmProjects\Study_Hillel\StudiTest\quotes.csv", "w", encoding="utf-8") as write_quotes:


        url = "http://api.forismatic.com/api/1.0/"

        params = {"method": "getQuote",
                  "format": "json",
                  "key": 1,
                  "lang": "ru"}

        data_quote = []
        data_author = []

        count = 0
        while count != number_of_quotes:
            params["key"] = random.randint(0, 999999)
            result = requests.get(url, params=params)
            quote = result.json()
            quote_text = quote["quoteText"]
            quote_author = quote["quoteAuthor"]
            if quote_author != "" and quote_text not in data_quote:
                data_quote.append(quote_text)
                data_author.append(quote_author)
                count += 1


        data = {}

        for i in range(len(data_author)):
            data[data_author[i]] = data_quote[i]

        # Сортировка данных
        def sorted_author_key(data):
            for key in range(len(data)):
                return data[key]
        new_data = []
        sorted_data = dict(sorted(data.items(), key=sorted_author_key))
        new_data.append(sorted_data)


        writeheader = ["Author", "Quote", "URL"]

        writer = csv.writer(write_quotes)
        # writer = csv.writer(write_quotes, delimiter=";")
        writer.writerow(writeheader)
        for row in sorted_data.keys():
            r = row
            writer.writerow(r)
        # for key, string in sorted_data.items():
        #     writer.writerow(key)


write_quotes(10)
