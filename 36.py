#Напишите код, который будет переводить полярные координаты в декартовы.
#Напишите код, который будет рисовать график окружности в полярных координатах.
#Напишите код, который будет рисовать график отрезка прямой линии в полярных координатах.
import numpy as np
import pylab
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#def polar(r0, phi):
#    x = r0 * np.cos(phi)
#    y = r0 * np.sin(phi)
#    return x, y
#окружность
r0 = 20
a=30
phi = np.pi/10
n = 100
fig = plt.figure()
ax = fig.gca(projection='3d')
for k in np.linspace(0, 1, 1):
    theta = np.linspace(0, 2*np.pi, n)
    R = r0*np.cos(theta - np.pi) + np.sqrt(a**2 - r0**2 * np.sin(theta - np.pi)**2)
    X = R*np.cos(theta)
    Y = R*np.sin(theta)
    ax.plot(X, Y)
plt.show()
fig = plt.figure()
ax = fig.gca(projection='3d')
# параметры отрезка
x=np.linspace(30,40,1000)
y = (23-x*np.cos(np.pi/2))/np.sin(np.pi/2)
ax.plot(x,y)
plt.show()