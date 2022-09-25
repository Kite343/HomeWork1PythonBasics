day = int(input("Введите номер дня - "))
if day < 1 or day > 7:
    print("Такого дня недели нет")
else:
    print(("Да", "Нет")[day < 6])