#Нарисуйте трехмерный график двух любых поверхностей второго порядка.
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
import matplotlib.pyplot as plt
fig = figure()
ax = Axes3D(fig)
x = np.arange(-5,5,0.5)
y = np.arange(-5,5,0.5)
x, y = np.meshgrid(x,y)
z = x**2/4-y**2/5
z1 = (x**2+y**2)+15
ax.plot_wireframe(x,y,z)
ax.plot_surface(x, y, z1, cmap='inferno')
show()
