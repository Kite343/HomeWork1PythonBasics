import controller_def as c_d
import view

action_def = {1: c_d.show_phonebook,
              2: c_d.copy_in_txt,
              3: c_d.copy_in_csv,
              4: c_d.add_data_phonebook,
              5: c_d.del_entry_phonebook,
              6: c_d.edit_entry_phonebook}


def phone_book():
    view.print_text("Начать работу с телефонной книгой?")
    start = view.yes_no()
    while start:
        action = view.show_menu()
        action_def[action]()

        view.print_text("Продолжить работу с телефонной книгой?")
        start = view.yes_no()