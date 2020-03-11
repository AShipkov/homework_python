#Нарисуйте график функции:
#y(x) = k∙cos(x – a) + b
#для некоторых (2-3 различных) значений параметров k, a, b
import numpy as np
import math
import pylab
k = int(input('Введите k: '))
a = int(input('Введите a: '))
b = int(input('Введите b: '))
def func(x,a,b,k):
    return k*math.cos(x-a)+b
xlist = np.arange(-20, 20, 0.1)
ylist = [func(x,a,b,k) for x in xlist]
pylab.plot(xlist, ylist)
pylab.show()
