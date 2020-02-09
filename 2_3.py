"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""
list_month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
season_list = ['зима', 'весна', 'лето', 'осень']
input_month = int(input('Введите целое число от 1 до 12, соответствующее месяцу: '))
if input_month == 1 or input_month==2 or input_month==12:
    print('Сезон:', season_list[0], 'Месяц:', list_month [input_month-1])
if input_month == 3 or input_month==4 or input_month==5:
    print('Сезон:', season_list[1], 'Месяц:', list_month [input_month-1])
if input_month == 6 or input_month==7 or input_month==8:
    print('Сезон:', season_list[2], 'Месяц:', list_month [input_month-1])
if input_month == 9 or input_month==10 or input_month==11:
    print('Сезон:', season_list[3], 'Месяц:', list_month [input_month-1])
dict_month = {
    1:'январь',
    2:'февраль',
    3:'март',
    4:'апрель',
    5:'май',
    6:'июнь',
    7:'июль',
    8:'август',
    9:'сентябрь',
    10:'октябрь',
    11:'ноябрь',
    12:'декабрь'
}
dict_season = {
    1:'зима',
    2:'зима',
    3:'весна',
    4:'весна',
    5:'весна',
    6:'лето',
    7:'лето',
    8:'лето',
    9:'осень',
    10:'осень',
    11:'осень',
    12:'зима'
}
print ('ВРЕМЯ ГОДА:', dict_season[input_month],'МЕСЯЦ:',dict_month[input_month])

