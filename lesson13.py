# Основа ДЗ - ДЗ №8 https://github.com/30nt/IntroPython_18_11/blob/main/Homeworks/lesson8.txt
#
# Суть задания - сздать класс EmailGenerator
#
# 1. При инициализации класса передавать два параметра - путь к файлу domains.txt и путь к файлу names.txt
# Пример:
# email_generator = EmailGenerator("domains.txt", "names.txt")
#
# 2. Атрибуты экземпляра класса: domains и names.
# Получаются с помощью методов get_domains() и get_names(). (описание и реализацию нужно взять из ДЗ №8)
# Пример:
# self.domains = self.get_domains()
# self.names = self.get_names()
#
# 3. При выводе на печать экземпляра класса вывести количество элементов в атрибутах domains и names
# Пример:
# print(email_generator)
# >>>len domains = 8, len names = 34
#
# 4. Написать метод экземпляра класса generate_email() (описание и реализацию нужно взять из ДЗ №8)
# Пример:
# email = email_generator.generate_email()
# print(email)
# >>>miller.249@sgdyyur.com

import random


class EmailGenerator:

    def __init__(self, domains_path, names_path):
        self.path_domains = domains_path
        self.path_names = names_path
        self.domains = self.get_domains()
        self.names = self.get_names()

    def __repr__(self):
        return f"len domains = {len(self.domains)}, len names = {len(self.names)}"

    def get_domains(self):
        with open(self.path_domains, "r") as my_txt:
            data_domains = []
            for line in my_txt:
                data_domains.append(line[1:].rstrip())
        return data_domains

    def get_names(self):
        with open(self.path_names, "r") as my_names:
            data_names = []
            for line in my_names:
                data_names.append(line.split()[1])
        return data_names

    def generate_email(self):
        random_alphabet = ''.join([chr(random.randint(97, 122)) for index in range(random.randint(5, 7))])
        e_mail = (
            f'{random.choice(self.names)}.{random.randint(100, 999)}@{random_alphabet}.{random.choice(self.domains)}')
        return e_mail


path_domains = "D:/Python/domains.txt"
path_names = "D:/Python/names.txt"

email_generator = EmailGenerator(path_domains, path_names)
e_mail = email_generator.generate_email()
print(email_generator, e_mail, sep="\n")
