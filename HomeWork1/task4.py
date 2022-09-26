quarter = int(input("Введите номер четверти \n"))
if quarter < 1 or quarter > 4:
    print("Такой четверти нет")
elif quarter == 1:
    print("y > 0 x > 0")
elif quarter == 2:
    print("y > 0 x < 0")
elif quarter == 3:
    print("y < 0 x < 0")
elif quarter == 4:
    print("y < 0 x > 0")
