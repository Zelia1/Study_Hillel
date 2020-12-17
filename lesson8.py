# 1. Считать данные из файла domains.txt
# Названия интернет доменов сохранить их в виде списка строк (названия сохранить без точки).
with open("D:/Python/domains.txt", "r") as my_txt:
    data = []
    for line in my_txt:
        data.append(line[1:].rstrip())
    print(data)
# with open("D:/Python/domains.txt", "w") as txt_file:
#     txt_file.write(data)