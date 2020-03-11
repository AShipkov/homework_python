'''
1. Напишите код, моделирующий выпадение поля в рулетке (с учетом поля зеро).

'''
import numpy as np
bet = 0
while True:
    bet = input ('Введите ставку:')
    try:
        bet = int(bet)
        if bet > 36:
            print('Ошибка ставки')
            break
        bet_1 = round(np.random.uniform (0,36))
        if bet == bet_1:
            print(bet_1, 'Вы выиграли')
        else:
            print(bet_1, 'Вы проиграли')
    except ValueError:
        if bet == 'красное' or bet == 'черное':
            bet_2 = round(np.random.uniform (0,36))
            if bet_2 % 2 != 0 and bet == 'черное':
                print(bet_2, 'черное','Вы выиграли')
            elif bet_2% 2 ==0 and bet =='красное' and bet_2 !=0:
                print(bet_2, 'красное', 'Вы выиграли')
            else:
                print(bet_2, 'Вы проиграли')
        else:
            print('Ошибка ставки')
            break



