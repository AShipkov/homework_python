"""
8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""
numbers = input('Введите 3 числа через запятые: ').split(',')
numbers = [int(i) for i in numbers]
numbers.sort()
print('Среднее число: ', numbers[1])