def superscript(n):
    return "".join(["⁰¹²³⁴⁵⁶⁷⁸⁹"[ord(c)-ord('0')] for c in str(n)])

def create_equation():             #создание уравнения с произвольными коэффициентами в виде строки
    from random import randint as r
    k = int(input("Задайте степень k для создания уравнения высшей степени\n"))
    a, b = int(input("Задайте начальную границу промежутка для выбора коэффициентов\n")), int(input("Задайте конечную границу промежутка для выбора коэффициентов\n"))
    coeffList = [r(a, b) for _ in range(k + 1)]
    equationStr = ""
    for i in range(k + 1):
        if (k - i) > 1:
            equationStr += str(coeffList[i]) + "x" + superscript(k - i)
            if coeffList[i + 1] >= 0:
                equationStr += "+"
        elif (k - i) == 1:
            equationStr += str(coeffList[i]) + "x"
            if coeffList[i + 1] >= 0:
                equationStr += "+"
        else:
            equationStr += str(coeffList[i])
    equationStr += "=0"

    return equationStr 

for i in range(1, 3):
    name = "equation" + str(i) + ".txt"
    with open(name, 'w', encoding='utf-8' ) as f:
        f.write(create_equation())
