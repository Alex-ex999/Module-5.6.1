maps = [1,2,3,
        4,5,6,
        7,8,9]

win_combinations = [[0,1,2],
                    [3,4,5],
                    [6,7,8],
                    [0,3,6],
                    [1,4,7],
                    [2,5,8],
                    [2,4,6],
                    [0,4,8]]

def print_maps():
    print(maps[0], end = " ")
    print(maps[1], end = " ")
    print(maps[2])

    print(maps[3], end = " ")
    print(maps[4], end = " ")
    print(maps[5])

    print(maps[6], end = " ")
    print(maps[7], end = " ")
    print(maps[8])
def get_result():
    win = ""

    for i in win_combinations:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"

    return win
def ask_step():
    while True:
        step = input()  #получили ввод
        if not step.isdigit():  # проверили, число ли
            print('Введите цифру: ')
            continue
        step = int(step)
        if step < 1 or step > 9:  # проверили, в пределах ли поля
            print("Что-то пошло не так! Введите корректное значение: ")
            continue
        step -= 1
        if maps[step] == "X" or maps[step] == "O":  # проверили не занята ли клетка
            print("Выберите другой вариант хода: ")
            continue
        return step


game_over = False
player1 = True

while game_over == False:

    print_maps()

    if player1:
        symbol = 'X'
    else:
        symbol = '0'

    print(f'Игрок {symbol}, введите цифру:')
    step = ask_step()


    maps[step] = symbol
    win = get_result()
    if win != "":
        game_over = True
    else:
        game_over = False


    player1 = not (player1)


print_maps()
print("Победа", win)

