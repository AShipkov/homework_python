"""
2. Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
"""
def lines ():
    with open('text.txt') as file:
        reader = file.readlines()
        return len(reader)
def words ():
    word = 0
    with open('text.txt') as file:
        for line in file:
            word += int(len(line.split()))
        return word
def letters ():
    with open('text.txt') as file:
        a = [i for i in file.read() if i != ' ' and i!='\n']
    return len(a)
print('Количество строк: ', lines())
print('Количество слов: ', words())
print('Количество букв: ',letters())