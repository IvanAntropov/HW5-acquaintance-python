# Создайте программу для игры в "Крестики-нолики".

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

def theGame(grid, listOfXO):
    count = 0
    listOfPosition = [0,0,0,0,0,0,0,0,0]
    forWin = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]] 
    playersList = [[],[]]
    print('\nИгроки по очереди ставят на свободные клетки крестики и нолики.\nПервый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает.')
    print(grid[0] + 
        '1' + grid[1] + '2' + grid[2] + '3' + grid[3] + 
        '4' + grid[4] + '5' + grid[5] + '6' + grid[6] + 
        '7' + grid[7] + '8' + grid[8] + '9' + grid[9])
    turn = random.randint(1, 2)
    print(f'Первый ход за {listOfXO[turn]}.\n')
    while count != 9:

        print(grid[0] + 
        listOfXO[listOfPosition[0]] + grid[1] + listOfXO[listOfPosition[1]] + grid[2] + listOfXO[listOfPosition[2]] + 
        grid[3] + 
        listOfXO[listOfPosition[3]] + grid[4] + listOfXO[listOfPosition[4]] + grid[5] + listOfXO[listOfPosition[5]] + 
        grid[6] + 
        listOfXO[listOfPosition[6]] + grid[7] + listOfXO[listOfPosition[7]] + grid[8] + listOfXO[listOfPosition[8]] + 
        grid[9])
        check = False
        while not check:
            player = int(inputValue(
            f'Ход игрока {listOfXO[turn]}\nВыбери квадрант 1 - 9: ',
            'Пробуй снова.\nВыбери квадрант 1 - 9: ', 
            1,9))
            if listOfPosition[player - 1] == 0:
                check = True
            else:
                print('\nПозиция занята!\n')
        playersList[turn - 1].append(player)
        for i in forWin:
            if all(j in playersList[turn - 1] for j in i):
                return f'\n Игрок {listOfXO[turn]} победил!'
        listOfPosition[player - 1] = turn

        turn = turn%2 + 1 
        count+=1

    return '\n Победила дружба!'


listOfXO = [' ', 'x', 'o']
grid = ['          \n   ',' | ',' | ',' \n  -----------  \n   ',' | ',' | ',' \n  -----------  \n   ',' | ',' | ',' \n          ']
check = 1
while check != 0:   
    print(theGame(grid, listOfXO))
    check = int(inputValue(
        '\nЕще один раунд?\n 0) Нет\n 1) Да\nВвод: ',
        'Пробуй снова.\n0) Нет\n 1) Да\nВвод: ', 
        0,1))


