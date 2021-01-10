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
        writer = csv.DictWriter(write_quotes, fieldnames=fieldnames)
        writer.writerows(sorted_data)

number_of_quotes = 10
write_quotes(number_of_quotes)