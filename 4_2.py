"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""
a = [123,7654,76543,2345,1,7,9,3,0,34,87654,23456765]
b = [a[i] for i in range (1, len(a)) if a[i] > a[i-1]]
print(b)