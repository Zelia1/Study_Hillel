import random

# 1. Считать данные из файла domains.txt
# Названия интернет доменов сохранить их в виде списка строк (названия сохранить без точки).
with open("D:/Python/domains.txt", "r") as my_txt:
    data_domains = []
    for line in my_txt:
        data_domains.append(line[1:].rstrip())
    # print(data_domains)
# Я не совсем понял, что подразумевалось под "сохранить" так что оставлю это тут.
# with open("D:/Python/domains.txt", "w") as txt_file:
#     txt_file.write('\n'.join(data))
#############################################################
# 2. Считать данные из файла names.txt и сохранить в список только фамилии из файла.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Фамилия находится всегда на одной и той же позиции в строке.
with open("D:/Python/names.txt", "r") as my_names:
    data_names = []
    for line in my_names:
        data_names.append(line.split()[1])
    # print(data_names)
# И опять же с сохранением, если что пример с первого задания.
#############################################################
# 3. Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать из списков, полученных в задачах 1 и 2 и переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
# Буквы в строке МОГУТ повторяться (перемешивание алфавита не подойдет, так как буквы не смогут повторяться)

# Пример вызова функции:
# e_mail = create_email(domains, names)
# print(e_mail)
#
# >>>miller.249@sgdyyur.com

# Не понял насчёт фамилии и домена, брать из списков так же рандомно или выборочно, по этому сделаю с применением
# библиотеки random.
random_alphabet = ''.join([chr(random.randint(97, 122)) for index in range(random.randint(5, 7))])


def email_generator():
    e_mail = (f'{random.choice(data_names)}.{random.randint(100, 999)}@{random_alphabet}.{random.choice(data_domains)}')
    print(e_mail)


email_generator()

# Мог вынести все данные в отдельные переменные как показано ниже, но не увидел в этом смысла, если таковой имеется,
# не откажусь от объяснений.

# def random_data(names, domains):
#     random_name = random.choice(names)
#     random_domain = random.choice(domains)
#     return random_name, random_domain
# data_random = random_data(data_names, data_domains)