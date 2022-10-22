import view
import model_txt as m_txt
import model_csv as m_csv

def show_phonebook():
    # book = m_txt.read_file() # база телефонной книги в txt файле
    book = m_csv.read_file()  # база телефонной книги в csv файле
    view.show_data(book)

def copy_in_txt():
    # book = m_txt.read_file() # база телефонной книги в txt файле
    book = m_csv.read_file()  # база телефонной книги в csv файле
    view.print_text("В какой файл записать дынные?")
    new_name = view.name_file()
    m_txt.write_files(new_name, book)

def copy_in_csv():
    # book = m_txt.read_file() # база телефонной книги в txt файле
    book = m_csv.read_file()  # база телефонной книги в csv файле
    view.print_text("В какой файл записать дынные?")
    new_name = view.name_file()
    m_csv.write_files(new_name, book)

def add_data_phonebook():
    entry = view.new_entry()
    # m_txt.add_data(entry) # база телефонной книги в txt файле
    m_csv.add_data(entry)  # база телефонной книги в csv файле

def del_entry_phonebook():
    view.print_text("Для удаления записи необходимо ввести номер записи для удаления")
    # book = m_txt.read_file() # база телефонной книги в txt файле
    book = m_csv.read_file()  # база телефонной книги в csv файле

    view.print_text("Перед выбором номера записи показать телефонну книгу?")
    if view.yes_no():
        view.show_data(book)

    if isinstance(book, list):   # база телефонной книги в csv файле
        book = ["\n".join(i) for i in book]
    # elif isinstance(book, str):  # база телефонной книги в txt файле
    #   book = [i for i in book.split("\n\n")]
    number = view.num_entry(len(book))
    del book[number - 1]
    m_csv.update_phonebook(book) # база телефонной книги в csv файле
    m_txt.update_phonebook(book) # база телефонной книги в txt файле
    

def edit_entry_phonebook():
    view.print_text("Для редактирования записи необходимо ввести номер записи для редактирования")
    # book = m_txt.read_file() # база телефонной книги в txt файле
    book = m_csv.read_file()  # база телефонной книги в csv файле

    view.print_text("Перед выбором номера записи показать телефонну книгу?")
    if view.yes_no():
        view.show_data(book)

    number = view.num_entry(len(book))
    view.print_text("Какую часть записи отредактировать?\n 1 - фамилия, 2 - имя, 3 - номер телефона, 4 - комментарий")
    val = view.num_entry(4)

    if isinstance(book, str):   # база телефонной книги в csv файле
        book = [i.split("\n") for i in book.split("\n\n")]

    book[number - 1][val - 1] = view.new_string()
    
    book = ["\n".join(i) for i in book]
    m_csv.update_phonebook(book) # база телефонной книги в csv файле
    m_txt.update_phonebook(book) # база телефонной книги в txt файле
    
