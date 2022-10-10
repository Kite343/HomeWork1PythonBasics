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
word_del = list(map(lambda c: c.strip('.,?!:;'), (filter(lambda x: 'ава' in x.lower() , text_list))))
# print(word_del)
for w_d in word_del:
    for i in range(len(text_list)):
        if w_d == text_list[i].strip('.,?!:;'):
            text_list[i] = text_list[i].replace(w_d, "")
text = " ".join(text_list)


# print(text)
with open("task1print.txt", 'w', encoding='utf-8') as new_file:
    new_file.write(text)
