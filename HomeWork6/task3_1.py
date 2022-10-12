#  HomeWork2 task1
# n = input("Введите вещественное число:\n")
# sum = 0
# for i in n:
#     if i.isdigit():
#         sum += int(i)
# print(sum)

print(sum(map(int, filter(lambda x: x.isdigit(), input("Введите вещественное число:\n")))))