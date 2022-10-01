print("Задайте список целых чисел через пробел")
numsList = input().split()
# print(numsList)
# fractionalList = [float('0.' + i.split('.')[1]) if not i.isdigit() else 0.0 for i in numsList] № если 0 всё таки нужен
fractionalList = [float('0.' + i.split('.')[1]) for i in numsList  if not i.isdigit()] # 0 не учавствует в отборе, если судить по примеру
# print(fractionalList)

min_el, max_el = fractionalList[0], fractionalList[0]
for i in fractionalList:
    if i < min_el:
        min_el = i
    elif i > max_el:
        max_el = i

print(max_el - min_el)
