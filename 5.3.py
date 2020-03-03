"""
Дополните код Монте-Карло последовательности независимых испытаний расчетом соответствующих вероятностей (через биномиальное распределение)
и сравните результаты.
4. Из урока по комбинаторике повторите расчеты, сгенерировав возможные варианты перестановок для других значений n и k

"""
import random
import matplotlib.pyplot as plt
import numpy as np
import math
for n in range (70, 130, 15):
    print()
    k, m = 0, 0
    for i in range(0, n):
        x = np.random.uniform(0, 10)
        if x<5:
            k = k + 1
        else:
            m = m + 1
    print (f'Количество выпадания орлов {k} и {m} решек при {n} попыток')
p =0.5 #успех
q = (1-p)
for n in range (70, 130, 15):
    print()
    for k in range (35, 60, 5):
        P=(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))*(p**k)*(q**(n-k))*100
        print (f'Вероятность выпадения {k} орлов при {n} попыток - {P:.5f} %')
X=[]
Y=[]
for n in range (75, 115):
    x, y = 0, 0
    for i in range(0, 30):
        k = np.random.uniform(0, 10)
        if k<5:
            x += 1
        else:
            y += 1
    X.append(x)
    Y.append(y)
print('\n',X,Y)
plt.hist(X, bins='auto')
plt.show()
#R = np.corrcoef (X,Y)
#print('\n', f'Kоэффициент корреляции равен {R}')
for i in range (1, len(X)):
    R1 = np.sum((X[i]-X[i-1])*(Y[i]-Y[i-1]))/np.sqrt((np.sum(X[i]-X[i-1])**2)*np.sum((Y[i]-Y[i-1])**2))
print('\n',f'Kоэффициент корреляции равен {R1}')