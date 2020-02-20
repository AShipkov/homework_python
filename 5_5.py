"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import os
with open ('list3.txt', 'w') as f:
    f.write(input('Введите числа, разделенные пробелами: '))
with open('list3.txt') as file:
    for i in file:
        a =i.split()
    try:
        print(sum(map(int, a)))
    except ValueError:
        print('Ошибка ввода!')
        os.remove('list3.txt')