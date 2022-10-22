def show_data(text):
    if isinstance(text, list):
        text = [str(i) + "\n" + "\n".join(val) for i, val in enumerate(text, start=1)]
    elif isinstance(text, str):
        text = [str(i) + "\n" + val for i, val in enumerate(text.split('\n\n'), start=1)]
    print("\n\n".join(text))

def check_num(num):
    while True:
        n = input("Введите необходимое значение\n")
        try:
            n = int(n)
        except:
            print("Введите числовое значение")
            continue
        if n <= 0 or n > num:
            print(f"Значение должно быть от 1 до {num}")
        else:
            return n

def show_menu():
    print("Выберите необходимое действие:")
    print("1 - Вывести на экран телефонную книгу",
          "2 - Скопировать телефонную книгу в txt файл",
          "3 - Скопировать телефонную книгу в csv файл",
          "4 - добавить данные в телефонную книгу",
          "5 - удалить запись из телефонной книги",
          "6 - редактировать запись в телефонной книге", sep='\n')
    return check_num(6)

def num_entry(n):
    print("Введите номер записи для удаления\n")
    return check_num(n)

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

def new_string():
    return input("Введите новое значение записи\n")

def print_text(text):
    print(text)