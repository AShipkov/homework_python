"""
y = x2 – 1
exp(x) + x∙(1 – y) = 1
y = x2 – 1
exp(x) + x∙(1 – y) > 1

"""
from scipy.optimize import fsolve
import math

def equations(p):
    x, y = p
    return (y-x**2+1, math.exp(x) + x -x*y - 1)
x, y =  fsolve(equations, (2, 5))
print (equations((round(x), round(y))))

def equations1(p):
    x, y >= p
    return (y-x**2+1, math.exp(x) + x -x*y - 1)
x, y =  fsolve(equations, (5, 10))
print (equations((round(x), round(y))))