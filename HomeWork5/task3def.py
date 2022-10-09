def draw_field(field):
    print("-------------")
    for i in range(3):
        print("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
        print("-------------")
 

def position_select(token, field):
    valid = False
    while not valid:
        position = input("Куда поставим " + token+"?\n")
        if position.isdigit():
            position = int(position)
        else:
            print("Некорректный ввод. Вы уверены, что ввели число?\n")
            continue
        if position >= 1 and position <= 9:
            if (str(field[position-1]) not in "XO"):
                field[position-1] = token
                valid = True
            else:
                print("Эта клеточка уже занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

def check_win(field):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for combo in win_coord:
        if field[combo[0]] == field[combo[1]] == field[combo[2]]:
            return field[combo[0]]
    return False

def gameXO():
    game_field = [i for i in range(1,10)]
    counter = 0
    win = False
    print("Первый игрок играет за X, второй - за O")
    while not win:
        draw_field(game_field)
        if counter % 2 == 0:
            print("Ход 1 игрока")
            position_select("X", game_field)
        else:
            print("Ход 2 игрока")
            position_select("O", game_field)
        counter += 1
        if counter > 4:
            win = check_win(game_field)
            if win:
                draw_field(game_field)
                if win == "X":
                    print("1 игрок выиграл!")
                else:
                    print("2 игрок выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
