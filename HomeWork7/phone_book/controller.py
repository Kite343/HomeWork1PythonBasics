import view
import model_txt as m_txt
import model_csv as m_csv

def phone_book():
    print("Начать работу с телефонной книгой?")
    start = view.yes_no()
    while start:
        action = view.show_menu()
        if action == 1:
            book = m_txt.read_file()
            view.show_data(book)
        elif action == 2:
            book = m_txt.read_file()
            print("В какой файл записать дынне?")
            new_name = view.name_file()
            m_txt.write_files(new_name, book)
        elif action == 3:
            book = m_txt.read_file()
            print("В какой файл записать дынне?")
            new_name = view.name_file()
            m_csv.write_files(new_name, book)
        elif action == 4:
            entry = view.new_entry()
            m_txt.add_data(entry)

        print("Продолжить работу с телефонной книгой?")
        start = view.yes_no()
