"""
1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""
lines = []
while True:
    lines.append(input('Введите данные записи: '))
    if ' ' in lines:
        break
with open("text.txt", "w") as file:
    for  line in lines:
        file.write(line + '\n')

