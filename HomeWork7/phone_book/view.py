def show_data(text):
    print(text)

def check_show_menu():
    while True:
        n = input("Введите необходимое значение\n")
        try:
            n = int(n)
        except:
            print("Введите числовое значение")
            continue
        if n <= 0 or n > 4:
            print("Значение должно быть от 1 до 4")
        else:
            return n

def show_menu():
    print("Выберите необходимое действие:")
    # print('1 - Вывести на экран телефонную книгу\n2 - Скопировать телефонную книгу в txt файл\n3 - Скопировать телефонную книгу в csv файл')
    print("1 - Вывести на экран телефонную книгу",
          "2 - Скопировать телефонную книгу в txt файл",
          "3 - Скопировать телефонную книгу в csv файл",
          "4 - добавить данные в телефонную книгу", sep='\n')
    return check_show_menu()

def name_file():
    return input("Введите полное имя файла\n")

def yes_no():
    while True:
        n = input("Введите: для нет - 0, для да - 1\n")
        if n in ('0', '1'):
            return int(n)
        else:
            print("Такое значение не возможно")

def new_entry():
    text = []
    text.append(input("Введите фаимилию\n"))
    text.append(input("Введите имя\n"))
    text.append(input("Введите номер телефона\n"))
    text.append(input("Введите комментарий\n"))
    return text

