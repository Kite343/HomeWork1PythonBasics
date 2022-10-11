def chek_num():
    while True:
        n = input("Введите число или пустую строку, если вам необходимо прервать ввод\n")
        if n.isdigit():
            n = int(n)
            return n
        if n == "":
            return n
        else:
            print("Некорректный ввод. Вы уверены, что ввели число или пустую строку?\n")
            continue

def nums_list():
    n_lst = []
    num = chek_num()
    while num != "":
        n_lst.append(int(num))
        num = chek_num()
    return n_lst

def nod_mums():
    import math
    from functools import reduce
    print("Для нахождения НОД нескольких чисел вводите их поочередно.")
    nums_lst = nums_list()
    if nums_lst == []:
        return 0
    if len(nums_lst) == 1:
        return nums_lst[0]
    nod = reduce(math.gcd, nums_lst)
    return nod

print("Наибольший общий делитель (НОД) введенных чисел:", nod_mums())
