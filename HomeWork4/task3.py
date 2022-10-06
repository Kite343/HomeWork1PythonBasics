def multipliers(n):
    multList = []
    i = 2
    while i < n:
        if n % i == 0:
            multList.append(i)
            n //= i 
        else:
            i += 1
    if n > 1:
        multList.append(n)
    return multList

num = int(input("Введите число\n"))
print(f"Список простых множителей числа {num}:\n{multipliers(num)}")
