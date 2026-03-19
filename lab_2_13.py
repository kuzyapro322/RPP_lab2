# ==============================
# Пункт 2.13 — Работа со строками в Python
# ==============================

string = input("Введите строку: ")

open_index = -1
close_index = -1
open_bracket = ""
close_bracket = ""

i = 0

for symbol in string:
    if symbol == "(":
        open_index = i
        open_bracket = "("
        close_bracket = ")"
    elif symbol == "[":
        open_index = i
        open_bracket = "["
        close_bracket = "]"
    i += 1

if open_index != -1:
    i = open_index + 1

    while i < len(string):
        if string[i] == close_bracket:
            close_index = i
            break
        i += 1

if open_index == -1 or close_index == -1:
    print("Скобки не найдены")
else:
    has_digit = False
    i = open_index + 1

    while i < close_index:
        if "0" <= string[i] <= "9":
            print(string[i], end="")
            has_digit = True
        i += 1

    if not has_digit:
        print("Не найдено чисел в скобках")
    else:
        print()