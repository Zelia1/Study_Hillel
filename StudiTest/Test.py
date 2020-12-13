# объявление функции
def is_correct_bracket(text):
    count = 0
    for i in range(len(text)):
        if count >= 0:
            if text[i] == '(':
                count += 1
            if text[i] == ')' and count >= 0:
                count -= 1
        else:
            return False

    return count == 0


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))