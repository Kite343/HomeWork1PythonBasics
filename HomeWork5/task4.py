def code_RLE(text):
    if text == "":
        return ""
    cod_text = ""
    count = 0
    char = text[0]
    for i in range(len(text)):
        if text[i] == char:
            count += 1
        else:
            cod_text += str(count) + char
            char = text[i]
            count = 1
    cod_text += str(count) + char
    return cod_text

#  проверка функции
# my_text = "aaassddd"
# print(code_RLE(my_text))

def decode_RLE(text):
    if text == "":
        return ""
    decode_text = ""
    num = ""
    for i in range(len(text)):
        if text[i].isdigit():
            num += text[i]
        else:
            decode_text += int(num) * text[i]
            num = ""
    return decode_text

#  проверка функции
# my_text = "3a2s3d"
# print(decode_RLE(my_text))

with open("task4input.txt", "r", encoding='utf-8') as file:
    my_text = file.read()

my_text = code_RLE(my_text)
with open("task4cod.txt", "w", encoding='utf-8') as file:
    file.write(my_text)

my_text = decode_RLE(my_text)
with open("task4decod.txt", "w", encoding='utf-8') as file:
    file.write(my_text)