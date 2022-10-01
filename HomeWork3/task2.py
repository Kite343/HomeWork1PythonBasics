print("Задайте список целых чисел через пробел")
multList = list(map(int, input().split()))
# print(numsList)
n = len(multList)
sumPair = [multList[i] * multList[n - i - 1] for i in range(n // 2 + n % 2)]
print(sumPair)