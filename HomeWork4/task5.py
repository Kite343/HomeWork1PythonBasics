def coeffList(eq):                 # функция извлекающая коэффициенты уравнения в список
    if eq[0] not in ("+", "-"):
        eq = "+" + eq
    n = len(eq)
    k_list = []
    temp = ""
    for i in range(n):
        if eq[i] == 'x' or i == (n - 2):
            if temp in ("+", "-"):
                temp += "1"
            k_list.append(int(temp))
            temp = ""
        elif temp == "" and (eq[i] in ("+", "-")):
            temp += eq[i]
        elif temp != "":
            temp += eq[i]
    return k_list

def superscript(n):
    return "".join(["⁰¹²³⁴⁵⁶⁷⁸⁹"[ord(c)-ord('0')] for c in str(n)])

def create_eq_str(coeffList):             # функция создающая уравнение по списку коэффициентов в строковом формате 
    k = len(coeffList) - 1
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

with open("equation1.txt", 'r', encoding='utf-8' ) as f:
    coeff1 = coeffList(f.readline().strip())
# print(coeff1)
with open("equation2.txt", 'r', encoding='utf-8' ) as f:
    coeff2 = coeffList(f.readline().strip())
# print(coeff2)

lenCoeff1 = len(coeff1)
lenCoeff2 = len(coeff2)
if lenCoeff1 > lenCoeff2:
    coeff2 = [0 for _ in range(lenCoeff1 - lenCoeff2)] + coeff2
    lenCoeff2 = lenCoeff1
    # print(coeff2)
elif lenCoeff1 < lenCoeff2:
    coeff1 = [0 for _ in range(lenCoeff2 - lenCoeff1)] + coeff1
    lenCoeff1 = lenCoeff2
    # print(coeff1)

newCoeff =[coeff1[i] + coeff2[i] for i in range(lenCoeff1)]
# print(newCoeff)

print(create_eq_str(newCoeff))
