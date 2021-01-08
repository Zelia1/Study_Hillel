# # объявление функции
# def is_correct_bracket(text):
#     count = 0
#     for i in range(len(text)):
#         if count >= 0:
#             if text[i] == '(':
#                 count += 1
#             if text[i] == ')' and count >= 0:
#                 count -= 1
#         else:
#             return False
#
#     return count == 0
#
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_correct_bracket(txt))

# import random
# my_alphabet = [chr(value) for value in range(97, 123)]
#
# def keys():
#     keys = ''.join([random.choice(my_alphabet) for key in range(5)])
#     return keys
#
# def values():
#     values = [[random.randint(-100, 100)], [random.random()], [True], [False]]
#     return random.choice(values)
#
# def write_dict():
#     my_dict = {keys(): random.choice(values()) for i in range(random.randint(5, 20))}
#     return my_dict
# print(write_dict())

#  1. Создает данные для записи в файл txt.
# Функция генерирует и возвращает строку случайной длинны (не менее 100 но не более 1000 символов).
# В строке должны присутствовать большие и маленькие буквы английского алфавита, цифры, пробелы,
# знаки препинания, символ перехода на новую строку (\n).
# Строка должна выглядеть как текст. Слова отделяться друг от друга пробелами.
# Большие буквы только в начале слов. Цифры не должны быть частями слов, а стоять отдельно.
# Знаки пр

# import random
#
# def string_creation(min_len, max_len):
#     my_string = [chr(random.randint(97, 122)) for _ in range(random.randint(min_len, max_len))]
#     return ''.join(my_string)
#
# def digit_creation(min_len, max_len):
#     text_now = [str(random.randint(0, 9)) for _ in range(random.randint(min_len, max_len))]
#     return ''.join(text_now)
#
# def random_digit_creation(word):
#     if len(word) > 5:
#         return word
#     else:
#         return digit_creation(len(word), len(word))
#
# def last_letter(word):
#     signs = ".,:;!?"
#     if len(word) < 4:
#         return word
#     else:
#         return word[:-1] + random.choice(signs)
#
# def first_letter(word):
#     return word.replace(word[0], word[0].upper())
#
#
# def space_in_my_text(text_now):
#     quantity_space = len(text_now) // 8
#     spase_index = []
#     while len(spase_index) < quantity_space:
#         index = random.randint(1, len(text_now) - 2)
#         if (index not in spase_index and
#             index - 1 not in spase_index and
#             index + 1 not in spase_index):
#             spase_index.append(index)
#     for index in spase_index:
#         text_now = text_now[:index] + " " + text_now[index + 1:]
#     return text_now
#
# def new_string(new_word):
#     quantity_new_string = len(new_word) // 12
#     new_string_index = []
#     while len(new_string_index) < quantity_new_string:
#         index = random.randint(1, len(new_word) - 2)
#         if (index not in new_string_index and
#             index - 1 not in new_string_index and
#             index + 1 not in new_string_index):
#             new_string_index.append(index)
#     for index in new_string_index:
#         random_digit = random.randint(1, 5)
#         if random_digit == 1:
#             new_word = new_word[:index] + "\n" + new_word[index + 1:]
#     return new_word
#
# def text_creation(min_len=100, max_len=1000):
#     text_now = string_creation(min_len, max_len)
#     text_now = space_in_my_text(text_now)
#     new_word = []
#     for word in text_now.split():
#         random_digit = random.randint(1, 100)
#         if not random_digit % 5:
#             new_line = random_digit_creation(word)
#
#         elif not random_digit % 5:
#             new_line = first_letter(word)
#
#         elif not random_digit % 2:
#             new_line = last_letter(word)
#
#         else:
#             new_line = word
#         new_word.append(new_line)
#     new_word = " ".join(new_word)
#     new_word = new_string(new_word)
#
#     return new_word
# print(text_creation())

# Функция 3. Создает данные для записи в файл csv.
# Создает и возвращает список длинны n внутренних списков длинны m (таблица с n строк и m столбцов).
# Числа n и m выбираются случайно в диапазоне от 3 до 10.
# В таблицу записывать значения только 0 или 1.
# Заголовка у таблицы нет.

import random
import csv

# def write_csv(min_len=3, max_len=10):
#     with open(r"C:\Users\Zelia\PycharmProjects\Study_Hillel\StudiTest\Test.csv", "w") as write_in:
#         writer = csv.writer(write_in)
#         x = random.randint(min_len, max_len)
#         for i in range(random.randint(min_len, max_len)):
#             writer.writerow(random.randint(0, 1) for row in range(x))
# write_csv()

# def remove_all_before(items, border):
#     if border in items:
#         x = items.index(border)
#         value = items[x:]
#     else:
#         value = items
#     return value
#
#
# a, b = [], 1
# print(remove_all_before(a, b))
#
# data = [[5, 2], [3, 5], [5, 1]]
# def sort_list():
#     sort_key = data[1]
#     return sort_key
# print(sorted(data, key=sort_list))



# url = "http://api.forismatic.com/api/1.0/"
#
# params = {"method": "getQuote",
#           "format": "json",
#           "key": 1,
#           "lang": "ru"}
# for i in range(10):
#     params["key"] = i
#     r = requests.get(url, params=params)
#     quote = r.json()
#     print(quote)
#     # quote_text = quote["quoteText"]
#     # print(quote_text)
#     # quote_author = quote["quoteAuthor"]
#     # print(quote_author)
#
# res = params
# print(res)

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
            params["key"] = random.randint(1, 999999)
            result = requests.get(url, params=params)
            quote = result.json()
            quote_text = quote["quoteText"]
            quote_author = quote["quoteAuthor"]
            if quote_author == "" or quote_text in data_quote:
                continue
            else:
                data_quote.append(quote_text)
                data_author.append(quote_author)
                count += 1
        print(count)
        data = {}
        for i in range(len(data_author)):
            data[data_author[i]] = data_quote[i]
        print(len(data))

        # Сортировка данных
        def sorted_author_key(data):
            for key in range(len(data)):
                return data[key]

        sorted_data = dict(sorted(data.items(), key=sorted_author_key))
        print(sorted_data)

write_quotes(10)