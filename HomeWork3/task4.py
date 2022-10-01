n = int(input("Введите число, которое необходимо перевести в двоичную систему\n"))
nKod2str = ""
while n != 0:
    nKod2str += str(n%2)
    n //= 2

nKod2 = int(nKod2str[::-1])
print(nKod2)