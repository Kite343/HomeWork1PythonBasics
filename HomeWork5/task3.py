import task3def

start = True
while start:
    print("хотите сиграть в крестики-нолики? ответьте да или нет")
    answer = input().lower()
    if answer not in ("да", "нет"):
        print("Введите только да или нет")
        continue
    if answer == "да":
        task3def.gameXO()
    else:
        start = False