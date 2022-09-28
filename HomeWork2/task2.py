n = int(input("Введите число\n"))
n_mult = [1]
for i in range(2, n + 1):
    n_mult.append(n_mult[i - 2] * i)
print(n_mult)