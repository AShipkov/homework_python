"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
my_list = []
while True:
    a = input('Введите данные списка, если список закончен введите +: ')
    if a != '+':
        my_list.append(a)
    else:
        break
print(my_list)
new_list = []
i=0
a = int(len(my_list))
if a % 2 != 0:
    new_list.insert(-1, my_list[-1])
    a-=1
while i < a:
    if i%2 == 0:
        new_list.insert(i, my_list[i+1])
        i+=1
    else:
        new_list.insert(i, my_list[i-1])
        i+=1
print(new_list)


