"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
 который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""
class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
         return '\n'.join(map(str, self.my_list))

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for a in range(len(other.my_list[i])):
                self.my_list[i][a] = self.my_list[i][a] + other.my_list[i][a]
        return Matrix.__str__(self)

M = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])  # матрица 3x3
new_M = Matrix([[1, 2, 3], [-4, -5, -6], [7, 8, 9]])
m = Matrix([[3, 5, 8, 3], [8,3,7,1]])                 # матрица 2х3
new_m = Matrix([[1, 2, 3, 4], [-1,-2,-3,-4]])
m1 = Matrix([[31, 22], [37, 43], [51,86]])            # матрица  3х2
new_m1 = Matrix([[3, 2], [7, 3], [-1,-6]])

print(M.__add__(new_M))
print('')
print(m.__add__(new_m))
print('')
print(m1.__add__(new_m1))