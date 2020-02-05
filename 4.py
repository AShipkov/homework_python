"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
"""

input_number = input('Ведите целое положительное число: ')
i = len(input_number)
#print(i)
a = int(input_number[i-1])
while i> 0:
    i = i-1
    if a >= int(input_number [i]):
        continue
    else: a = int(input_number [i])
print (a)



