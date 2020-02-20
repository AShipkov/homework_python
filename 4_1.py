"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

"""
from sys import argv
script_name, first_param, second_param, third_param = argv
x = int(first_param)
y = int(second_param)
z = int(third_param)

def my_func (x, y, z):
    return x*y+z
print(my_func(x,y,z))

