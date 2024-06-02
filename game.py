import numpy as np
import sys


#проверка введенного значения
def hod1():
    print(np.array(matrix))
    try:
        move=int(input("Введи номер клетки: "))
    except ValueError:
        print('Это не цифра')
        pl1()
    if move<1 or move>9:
        print('Вне диапазона')
        pl1()
    else:
        return move
    
def hod2():
    print(np.array(matrix))
    try:
        move=int(input("Введи номер клетки: "))
    except ValueError:
        print('Это не цифра')
        pl2()
    if move<1 or move>9:
        print('Вне диапазона')
        pl2()
    else:
        return move

#Победа
def win1():
    print(np.array(matrix))
    print(f"{player1} победил!")
    again()

def win2():
    print(np.array(matrix))
    print(f"{player2} победил!")
    again()

#проверка выигрыша
def check():
    #проверка по строкам
    if lst1[0]==lst1[1]==lst1[2]=='X': return True
    elif lst1[0]==lst1[1]==lst1[2]=='O': return True
    elif lst2[0]==lst2[1]==lst2[2]=='X': return True
    elif lst2[0]==lst2[1]==lst2[2]=='O': return True
    elif lst3[0]==lst3[1]==lst3[2]=='X': return True
    elif lst3[0]==lst3[1]==lst3[2]=='O': return True
    #проверка по столбцам
    elif lst1[0]==lst2[0]==lst3[0]=='X': return True
    elif lst1[0]==lst2[0]==lst3[0]=='O': return True
    elif lst1[1]==lst2[1]==lst3[1]=='X': return True
    elif lst1[1]==lst2[1]==lst3[1]=='O': return True
    elif lst1[2]==lst2[2]==lst3[2]=='X': return True
    elif lst1[2]==lst2[2]==lst3[2]=='O': return True
    #проверка по диагоналям
    elif lst1[0]==lst2[1]==lst3[2]=='X': return True
    elif lst1[0]==lst2[1]==lst3[2]=='O': return True
    elif lst1[2]==lst2[1]==lst3[0]=='X': return True
    elif lst1[2]==lst2[1]==lst3[0]=='O': return True
    #проверка на ничью
    elif isinstance(lst1[0], str)==True and isinstance(lst1[1], str)==True and isinstance(lst1[2], str)==True and isinstance(lst2[0], str)==True and isinstance(lst2[1], str)==True and isinstance(lst2[2], str)==True and isinstance(lst3[0], str)==True and isinstance(lst3[1], str)==True and isinstance(lst3[2], str)==True:
        print("Ничья")
        again()

#ход 1 игрока
def pl1():
    print(f'{player1} делай ход')
    move=hod1()
    if 1<=move<=3:
        try:
            place=lst3.index(move)
        except ValueError:
            print("Невозможный ход. Попробуй еще раз.")
            pl1()
        lst3.pop(place)
        lst3.insert(place, 'X')
        if check()==True: win1()
        else:
            pl2()
    elif 4<=move<=6:
        try:
            place=lst2.index(move)
        except ValueError:
            print("Невозможный ход. Попробуй еще раз.")
            pl1()
        lst2.pop(place)
        lst2.insert(place, 'X')
        if check()==True: win1()
        else:
            pl2()
    elif 7<=move<=9:
        try:
            place=lst1.index(move)
        except ValueError:
            print("Невозможный ход. Попробуй еще раз.")
            pl1()
        lst1.pop(place)
        lst1.insert(place, 'X')
        if check()==True: win1()
        else:
            pl2()

#ход 2 игрока
def pl2():
    print(f'{player2} делай ход')
    move=hod2()
    if 1<=move<=3:
        try:
            place=lst3.index(move)
        except ValueError:
            print(f"{player2} невозможный ход. Попробуй еще раз.")
            pl2()
        lst3.pop(place)
        lst3.insert(place, 'O')
        if check()==True: win2()
        else:
            pl1()            
    elif 4<=move<=6:
        try:
            place=lst2.index(move)
        except ValueError:
            print(f"{player2} невозможный ход. Попробуй еще раз.")
            pl2()
        lst2.pop(place)
        lst2.insert(place, 'O')
        if check()==True: win2()
        else:
            pl1()
    elif 7<=move<=9:
        try:
            place=lst1.index(move)
        except ValueError:
            print(f"{player2} невозможный ход. Попробуй еще раз.")
            pl2()
        lst1.pop(place)
        lst1.insert(place, 'O')
        if check()==True: win2()
        else:
            pl1()

def start():
    print("Привет! Давайте сыграем в 'Крестики-нолики'. Первый игрок будет Х, а второй - О. Удачи =)")
    player1=input('Введите имя первого игрока: ')
    player2=input('Введите имя второго игрока: ')
    print(f"{player1} играет за Х\n{player2} игает за О")
    lst1=[7,8,9]
    lst2=[4,5,6]
    lst3=[1,2,3]
    matrix=[lst1,lst2,lst3]
    pl1()

def again():
    print("Хочешь сыграть еще раз?")
    ans=input("Введи [Y] - сыграть еще раз или [N] - закрыть игру: ")
    if ans.lower=='y':
        start()
    elif ans.lower=='n':
        sys.exit()
    else:
        again()

global player1
global player2
global lst1
global lst2
global lst3
global matrix

print("Привет! Давайте сыграем в 'Крестики-нолики'. Первый игрок будет Х, а второй - О. Удачи =)")
player1=input('Введите имя первого игрока: ')
player2=input('Введите имя второго игрока: ')
print(f"{player1} играет за Х\n{player2} игает за О")
lst1=[7,8,9]
lst2=[4,5,6]
lst3=[1,2,3]
matrix=[lst1,lst2,lst3]
pl1()