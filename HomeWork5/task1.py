# вариант 1, но возможно удаление части слова, а не всего слова, если одно из слов будет являться частью другого
# with open("task1input.txt", "r", encoding='utf-8') as file:
#     text = file.read()
#     # print(text)
# word_del = list(map(lambda c: c.strip('.,?!:;'), (filter(lambda x: 'ава' in x.lower() , text.split()))))
# # print(word_del)
# for word in word_del:
#     text = text.replace(word, "")
# # print(text)
# with open("task1print.txt", 'w', encoding='utf-8') as new_file:
#     new_file.write(text)


with open("task1input.txt", "r", encoding='utf-8') as file:
    text = file.read()
    # print(text)
text_list = text.split()
# print(text_list)
for i in range(len(text_list)):
    if "ава" in text_list[i].lower():
        text_list[i] = text_list[i].replace(text_list[i].strip('.,?!:;'), "")
text = " ".join(text_list)


# print(text)
with open("task1print.txt", 'w', encoding='utf-8') as new_file:
    new_file.write(text)
