#Нарисуйте трехмерный график двух параллельных плоскостей.
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from  pylab import *
import matplotlib.pyplot as plt
fig = figure()
ax = Axes3D(fig)
x = np.arange(-100,100,5)
y = np.arange(-100,100,5)
x, y = np.meshgrid(x,y)
z = 5*x+4*y
n=int(input('Введите расстояние между плоскостями: '))
ax.plot_wireframe(x,y,z)
ax.plot_surface(x+n, y+n, z+n, cmap='magma')
show()