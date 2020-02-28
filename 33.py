"""
3. Задание (в программе)
Напишите код на Python, реализующий построение графиков:
окружности,
эллипса,
"""
import numpy as np
from matplotlib import pyplot as plt
from math import pi
#Введение параметров элипса, при а1=а2 b1=b2 получается круг
# с центром (a1, b1) и диаметром d
a1 = int(input('Введите a1: '))
b1 = int(input('Введите b1: '))
a2 = int(input('Введите a2: '))
b2 = int(input('Введите b2: '))
d = int(input('Введите c: '))
# Полуглавная ось абсцисс по а
a = d / 2
x0 = (a1 + a2) / 2
y0 = (b1 + b2) / 2
#Расстояние от центра до фокуса при окружности
f = np.sqrt((a1 - x0)**2 + (b1 - y0)**2) # Distance from center to focus
# Полуглавная ось абсцисс по b
b = np.sqrt(a**2 - f**2)
#Угол между главной осью и осью x
phi = np.arctan2((b2 - b1), (a2 - a1))
resolution = 1000
t = np.linspace(0, 2*np.pi, resolution)
x = x0 + a * np.cos(t) * np.cos(phi) - b * np.sin(t) * np.sin(phi)
y = y0 + a * np.cos(t) * np.sin(phi) + b * np.sin(t) * np.cos(phi)
plt.plot(x, y)
# Усли есть необходимость показать фокус
#plt.plot(a1, b1, 'bo')
#plt.plot(a2, b2, 'bo')
plt.axis('equal') #выравнивает оси абсцисс и ординат
plt.show()

