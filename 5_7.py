"""
7. Создать (не программно) текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json
from itertools import groupby
average_profit = 0
list_profit = {}
dict_average_profit = {}
with open('list7.txt') as f:
    for line in f:
        i=1
        a = line.split(' ')
        key = a[0]
        b = [int(''.join(i)) for is_digit, i in groupby(line, str.isdigit) if is_digit]
        profit = b[0]-b[1]
        list_profit[key]=profit
        if profit >=0:
            average_profit += profit/i
            i+=1
        else:
            pass
    keys = 'average_profit'
    dict_average_profit[keys]=average_profit
    a=[list_profit, dict_average_profit]
    print(a)
with open("list.json", "w", encoding = "utf-8") as write_file:
    json.dump(a, write_file, ensure_ascii=False)

#Если ensure_ascii = True, все не-ASCII символы в выводе будут экранированы последовательностями \uXXXX
#и результатом будет строка, содержащая только ASCII символы. Если ensure_ascii = False, строки запишутся как есть.
