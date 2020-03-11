import math
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.linalg as sl
from scipy import optimize
#2
A=np.array([[1,2,-1],[3,-4,0],[8,-5,2],[2,0,-5],[11,4,-7]])
B=np.array([1,7,12,7,15])
print('Псевдорешение','\n',np.linalg.lstsq(A,B))
"""
3. Сколько решений имеет линейная система:
Если ноль – то измените вектор правой части так, чтобы система стала совместной, и решите ее
"""
# Матрица A1 вырожденная(ингулярная) поэтому меняем в ней любой елемент
A1 = np.array([[9,2,3],[4,5,6],[7,8,9]])
B1= np.array([12,2,1])
print('Измененная матрица решение','\n',np.linalg.solve(A1, B1))

#4
A = np.array([[1,2,3],[2,16,21],[4,28,73]])
P,L,U = sl.lu(A)
print('P','\n',P,'\n')
print('L','\n',L,'\n')
print('U','\n',U,'\n')
"""
5. Найдите нормальное псевдорешение недоопределенной системы:
x + 2y – z = 1
8x – 5y + 2z = 12
Для этого определите функцию Q(x,y,z), равную норме решения, и найдите ее минимум. 
"""
def Q(x):
    return (x**2+(10*x-14)**2+(11*x-15)**2)
a=[]
for x in range (0,3):
    a.append(Q(x))
print('min Q(x)', min(a))
print(f'Псевдорешение',2,10*2-14,11*2-15)
""""
6. Найдите одно из псевдорешений вырожденной системы
"""
A3 =np.array([[1,2,3],[4,5,6],[7,8,9]])
B3 = np.array([2,5,11])
#A3*x=B3
print('Псевдорешение','\n',np.linalg.lstsq(A3,B3))


