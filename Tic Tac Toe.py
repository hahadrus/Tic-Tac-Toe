'''
Крестики-нолики
Автор: Андрей Субботкин
'''

import time

board=[ 1, 2, 3, 4, 5, 6, 7, 8, 9]

def display(board):
    '''Выводим игровое поле'''
    print('   |   |')
    print(' ' + str(board[6]) + ' | ' + str(board[7]) + ' | ' + str(board[8]))
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + str(board[3]) + ' | ' + str(board[4]) + ' | ' + str(board[5]))
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + str(board[0]) + ' | ' + str(board[1]) + ' | ' + str(board[2]))
    print('   |   |')


def game_step(index, char):
    '''Проверка выполнения хода'''
    if index>9 or index<1 or board[index-1] in ('X','O'):
        return False
    
    board[index-1]=char
    return True


def check_win():
    '''Проверка выигрыша'''
    # по горизонтали
    if board[0] == board[1] == board[2]: return False
    elif board[3] == board[4] == board[5]: return False
    elif board[6] == board[7] == board[8]: return False
    # по вертикали
    elif board[0] == board[3] == board[6]: return False
    elif board[1] == board[4] == board[7]: return False
    elif board[2] == board[5] == board[8]: return False
    # по диагонали
    elif board[0] == board[4] == board[8]: return False
    elif board[2] == board[4] == board[6]: return False
    # если победы нет
    else: return True

def start():
    print("Привет! Давайте сыграем в 'Крестики-нолики'. Первый игрок будет играть за Х, а второй - за О. Удачи =)")
    time.sleep(1)
    pl1=input('Введите имя первого игрока: ')
    pl2=input('Введите имя второго игрока: ')
    print(f"{pl1} играет за Х\n{pl2} игает за О")
    time.sleep(1)
    display(board)
    step = 1 # номер шага
    current_pl=pl1
    symbol='X'

    while check_win() == True and step <= 9:
        index = input(f'Ходит игрок {current_pl}. Введи номер поля (0 - выход): ')
        
        if index=='0': break
        try:
            index=int(index)
        except:
            print('Невозможный ход. Введи номер клетки еще раз')
            continue
        if game_step(index, symbol) == True:
            display(board)
            print('Следующий ход')
            step+=1
            if current_pl==pl1:
                current_pl=pl2
                symbol='O'
            else:
                current_pl=pl1
                symbol='X'              
        else: 
            print('Невозможный ход. Введи номер клетки еще раз')

        
        
    
    if check_win() == False:
        print('Победил игрок ' + current_pl)
    elif check_win() == True and step>9:
        print('Ничья')
    elif index=='0':
        print('Конец игры. До свидания!')
    



start()

