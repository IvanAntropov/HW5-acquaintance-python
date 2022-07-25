# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

def inputValue(text1: str, text2: str, min=0, max=1):
    check = False
    while not check:
        try:
            number = int(input(text1))
            if number >= min and number <= max:
                check = True
            else:
                print(text2)
        except ValueError:
            print(text2)
            number = int(input(text1))
    return number

def candysGame1(mainNumber: int):
    turn = random.randint(0, 1)
    print('\nNumber: \n', mainNumber)
    listForGame = ['First', 'Second']
    while mainNumber > 0:
            player = int(inputValue
            (
                f'\n{listForGame[turn]} player move: ',
                'Try again. You can pick up no more than 28 candies in one move: ',
                1, 28
            ))
            mainNumber = mainNumber - player
            if mainNumber <= 0:
                return '\n' + listForGame[turn] + ' player won!!!'
            print(mainNumber)
            if turn == 0:
                turn = 1
            else:
                turn = 0  

def candysGame2(mainNumber):
    turn = random.randint(0, 1)
    print('\nNumber: \n', mainNumber)
    while mainNumber > 0:
            if turn == 0:
                player1 = int(inputValue
                (
                    '\nPlayer move: ',
                    'Try again. You can pick up no more than 28 candies in one move: ',
                    1, 28
                ))
                mainNumber = mainNumber - player1
                if mainNumber <= 0:
                    return '\n' + 'Player won!!!'    
                print(mainNumber)
                turn = 1
            else:
                player2 = random.randint(1, 28)
                print(f'\nBot move -{player2}')
                mainNumber = mainNumber - player2
                if mainNumber <= 0:
                    return '\n' + 'Bot won!!!'
                print(mainNumber)
                turn = 0

def candysGame3(mainNumber):
    turn = random.randint(0, 1)
    print('\nNumber: \n', mainNumber)
    while mainNumber > 0:
            if turn == 0:
                player1 = int(inputValue
                (
                    '\nPlayer move: ',
                    'Try again. You can pick up no more than 28 candies in one move: ',
                    1, 28
                ))
                mainNumber = mainNumber - player1
                if mainNumber <= 0:
                    return '\n' + 'Player won!!!'    
                print(mainNumber)
                turn = 1
            else:
                player2 = mainNumber%29
                if player2 == 0:
                    player2 += 1
                print(f'\nBot move -{player2}')
                mainNumber = mainNumber - player2
                if mainNumber <= 0:
                    return '\n' + 'Bot won!!!'
                print(mainNumber)
                turn = 0

def finalGame(mainNumber):
    decision = int(inputValue
    (
    '\nChoose the game. \n1) Against person\n2) Against bot\n3) Against "smart" bot\nChoice: ',
    'Try again.\nChoose the game. \n1) Against person\n2) Against bot\n3) Against "smart" bot\nChoice: ',
    1,3
    ))
    if decision == 1:
        print(candysGame1(mainNumber))
    elif decision == 2:
        print(candysGame2(mainNumber))
    else:
        print(candysGame3(mainNumber))

stringForGame = '\nУсловие задачи: \nНа столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.\nПервый ход определяется жеребьёвкой.За один ход можно забрать не более чем 28 конфет. \nВсе конфеты оппонента достаются сделавшему последний ход.' 
check = 1
while check != 0:
    print(stringForGame)
    finalGame(2021)
    check = int(inputValue
    (
    'Wanna another try? \n0 - No \n1 - Yes\nChoice: ',
    'Try again.\n0 - No \n1 - Yes\nChoice: ',
    0,2
    ))