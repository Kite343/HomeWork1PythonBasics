from math import pi
print(pi)
# d = input("Задайте точность дробной части (колличество знаков после запятой\n")
# d = '{:.' + d +'f}'
# print(d.format(pi))
d = int(input("Задайте точность дробной части (колличество знаков после запятой\n"))
print(round(pi, d))