"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
 Если в слово длинное, выводить только первые 10 букв в слове.
"""
input_str = input('Введите строку из нескольких слов, разделённых пробелами: ')
list = input_str.split()
for i in range(0, int(len(list))):
    if int(len(list[i])) >= 10:
        print(list[i][:10])
        continue
    else:
        print(list[i])




