# HomeWork3 task1
# print("Задайте список целых чисел через пробел")
# numsList = list(map(int, input().split()))
# # print(numsList)
# sum = 0
# for i in range(1, len(numsList), 2):
#     sum += numsList[i]
# print(sum)

print("Задайте список целых чисел через пробел")

numsList = list(map(int, input().split()))
print(sum(numsList[i] for i in range(1, len(numsList), 2)))