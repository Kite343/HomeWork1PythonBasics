def howmuch(s, n):
    import random
    if n >= s:
        return s
    num = s % (n + 1)
    if num > 0:
        return num
    return random.randint(1, n)
    

def chek_nums(cand, m):
    while True:
        num = input("Сколько конфет хотите забрать?\n")
        if num.isdigit():
            num = int(num)
        else:
            print("Некорректный ввод. Вы уверены, что ввели число?\n")
            continue
        if num > cand:
            print("Конфет меньше, чем вы хотите взять")
            continue
        if num <= 0:
            print("Конфеты брать обязательно")
            continue
        if num > m:
            print(f"Нельзя брать больше {m} конфет")
            continue
        return num



def game_candies_bot():
    print("На столе лежит 2021 конфета. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.")
    candies = 2021
    max = 28
    count = 1
    while candies > 0:
        if count % 2 == 1:
            count += 1
            print("Ваш ход.")
            nums = chek_nums(candies, max)
            candies -= nums
            print(f"Вы взяли {nums} конфет, осталось {candies}")
            if candies  == 0:
                print("Вы победили!")
        else:
            count += 1
            print("Ходит бот Саша.")
            nums = howmuch(candies, max)
            candies -= nums
            print(f"Саша взял {nums} конфет, осталось {candies}")
            if candies  == 0:
                print("Победил бот Саша!")

def number1(p1, p2):
    import random
    numb1 = random.randint(1, 2)
    if numb1 == 1:
        print(f"{p1} будет игроком №1 и делает первый ход")
        return p1, p2
    else:
        print(f"{p2} будет игроком №1 и делает первый ход")
        return p2, p1


    

def game_candies_bplayers():
    print("На столе лежит 2021 конфета. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.")
    player1, player2 = number1(input("Введите имя игрока\n"), input("Введите имя игрока\n"))

    candies = 2021
    max = 28
    count = 1
    while candies > 0:
        if count % 2 == 1:
            count += 1
            print(f"Ходит {player1}")
            nums = chek_nums(candies, max)
            candies -= nums
            print(f"Вы взяли {nums} конфет, осталось {candies}")
            if candies  == 0:
                print(f"{player1}, Вы победили!")
        else:
            count += 1
            print(f"Ходит {player2}")
            nums = chek_nums(candies, max)
            candies -= nums
            print(f"Вы взяли {nums} конфет, осталось {candies}")
            if candies  == 0:
                print(f"{player2}, Вы победили!")

# game_candies_bplayers()


