import model_txt as m_txt
import model_csv as m_csv

def show_phonebook(): #1
    book = m_csv.read_file()  # база телефонной книги в csv файле
    book = "\n\n".join([str(i) + "\n" + "\n".join(val) for i, val in enumerate(book, start=1)])
    return book
    
def copy_in_txt(): #2
    book = m_csv.read_file()  # база телефонной книги в csv файле
    new_name = 'my_book.txt'
    m_txt.write_files(new_name, book)

def copy_in_csv(): #3
    book = m_csv.read_file()  # база телефонной книги в csv файле
    new_name = 'my_book.csv'
    m_csv.write_files(new_name, book)

def add_data_phonebook(entry): #4
    m_csv.add_data(entry)  # база телефонной книги в csv файле

def len_phonebook():
    book = m_csv.read_file()
    return(len(book))

def del_entry_phonebook(num): #5
    book = m_csv.read_file()  # база телефонной книги в csv файле
    del book[num - 1]
    m_csv.update_phonebook(book) # база телефонной книги в csv файле
 
def edit_entry_phonebook(num, i, text): #6
    book = m_csv.read_file()  # база телефонной книги в csv файле
    book[num - 1][i - 1] = text
    m_csv.update_phonebook(book) # база телефонной книги в csv файле

    
