n = int(input("Введите число\n"))
n_list =[(1 + 1 / i)**i for i in range(1, n + 1)]
print(n_list)
print(sum(n_list))