print("Задайте список целых чисел через пробел")
numsList = list(map(int, input().split()))
# print(numsList)
sum = 0
for i in range(1, len(numsList), 2):
    sum += numsList[i]
print(sum)