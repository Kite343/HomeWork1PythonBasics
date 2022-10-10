import task2def as t2

def answer12():
    while True:
        print("Введите 1 или 2")
        answ = input()
        if answ in ("1", "2"):
            return answ
        else:
            print("Некорректное значение")


start = True
while start:
    print("хотите сиграть в игру 'Кто последний возьмет конфету'? ответьте да или нет")
    answer1 = input().lower()
    if answer1 not in ("да", "нет"):
        print("Введите только да или нет")
        continue
    if answer1 == "да":
        print("Вы будете играть с 1.другом или 2. с ботом?")
        answer2 = answer12()
        if answer2 == "1":
            t2.game_candies_bplayers()
        else:
            t2.game_candies_bot()
    else:
        start = False