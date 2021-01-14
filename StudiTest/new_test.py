import requests
import random
import csv
import re
import json


def read_and_filter(path):
    with open(path, "r", encoding="utf-8") as read_file:

        data = []

        for line in read_file.readlines():
            if ("birthday" in line.lower()) or ("death" in line.lower()):
                data.append(line.split("\n"))

    return data


def creat_dict_authors(data):
    reg_exp_name = r"[-\w.']+"
    reg_exp_date = r"[0-9]+"
    month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November",
                  "December"]

    temporary_dict = {}
    data_authors = []

    for list_index in range(len(data)):
        x = str(data[list_index]).split("-")
        temporary_dict["author"] = x[1].split("'")[0].strip()
        date_list = x[0][2:].split()
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

def write_dict_in_json_file(path, dict):
    with open(path, "w") as write_in_json:
        json.dump(dict, write_in_json, indent=2)


file_path = r"C:\Users\Zelia\PycharmProjects\Study_Hillel\StudiTest\authors.txt"
data_from_file = read_and_filter(file_path)
path_in_json = r"C:\Users\Zelia\PycharmProjects\Study_Hillel\StudiTest\Authors.json"
data_to_write = creat_dict_authors(data_from_file)
write_dict_in_json_file(path_in_json, data_to_write)
#
