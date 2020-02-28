"""
3. Задание (в программе)
Напишите код на Python, реализующий построение графиков:
гиппербола
"""

import matplotlib.pyplot as plt
def f(start, stop, step):
    while start < stop:
        yield start
        start += step
def asymptote_check(arg, function):
    try:
        function(arg)
        return True
    except ZeroDivisionError:
        return False
hyperbola = lambda x: 1 / x
xmin = -25
xmax = 25
dx = 0.2
xlist = [round(x, 4) for x in f(xmin, xmax, dx)]
ylist = [hyperbola(x) if asymptote_check(x, hyperbola) else float('nan') for x in xlist]
plt.plot(xlist, ylist)
plt.axis('equal')
plt.show()
