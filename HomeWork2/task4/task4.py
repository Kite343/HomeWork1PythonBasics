n = int(input("Введите число\n"))
n_list = [i for i in range(-n, n + 1)]
print(n_list)
mult = 1
file = open('position.txt')
for line in file:
    print(int(line.strip()))
    mult *= n_list[int(line.strip())]        
file.close() 
print(mult)