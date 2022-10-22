#name bot Kite_training1_bot
# Use this token to access the HTTP API:
# 5557533810:AAGljPN-5omvkqL18kzN5CHyOjeCbf-64ns

import telebot
from telebot import types 
import controller_def as c_d

entry = []
n = 0
num = 0
i = 0

bot = telebot.TeleBot('5557533810:AAGljPN-5omvkqL18kzN5CHyOjeCbf-64ns')

@bot.message_handler(commands=['start'])
def start_message(message):
    if message.text == '/start':
        menu = "Выбери необходимое действие:\n\
                1 - Вывести на экран телефонную книгу\n\
                2 - Скопировать телефонную книгу в txt файл\n\
                3 - Скопировать телефонную книгу в csv файл\n\
                4 - добавить данные в телефонную книгу\n\
                5 - удалить запись из телефонной книги\n\
                6 - редактировать запись в телефонной книге"
        bot.send_message(message.chat.id, menu)
        @bot.message_handler(content_types=['text'])
        def menu(message):
            if message.text in ('1', '2', '3', '4', '5', '6'):
                if message.text == '1':
                    text =  c_d.show_phonebook()
                    bot.send_message(message.chat.id, text)
                if message.text == '2':
                    c_d.copy_in_txt()
                    file = open('my_book.txt', 'rb')
                    bot.send_document(message.chat.id, file)
                if message.text == '3':
                    c_d.copy_in_csv()
                    file = open('my_book.csv', 'rb')
                    bot.send_document(message.chat.id, file)
                if message.text == '4':
                    global entry
                    entry = []
                    bot.send_message(message.chat.id, "Введите фамилию\n")
                    bot.register_next_step_handler(message, get_surname)
                if message.text == '5':
                    global n
                    n = c_d.len_phonebook()
                    bot.send_message(message.chat.id, "Выберите номер записи для удаления")
                    bot.register_next_step_handler(message, del_entry_phonebook)
                if message.text == '6':
                    # global n
                    n = c_d.len_phonebook()
                    bot.send_message(message.chat.id, "Выберите номер записи для изменения")
                    bot.register_next_step_handler(message, edit_entry_phonebook)
                    
            else:
                bot.send_message(message.chat.id, "Введите число от 1 до 6")
    else:
        bot.send_message(message.chat.id, "Напиши '/start'")

def get_surname(message):
    global entry
    entry.append(message.text)
    bot.send_message(message.chat.id, "Введите имя\n")
    bot.register_next_step_handler(message, get_name)
def get_name(message):
    global entry
    entry.append(message.text)
    bot.send_message(message.chat.id, "Введите номер телефона\n")
    bot.register_next_step_handler(message, get_phone)
def get_phone(message):
    global entry
    entry.append(message.text)
    bot.send_message(message.chat.id, "Введите комментарий\n")
    bot.register_next_step_handler(message, get_comment)
def get_comment(message):
    entry.append(message.text)
    c_d.add_data_phonebook(entry)

def del_entry_phonebook(message):
    global num
    num = message.text
    if num.isdigit():
        num = int(num)
        if 0 < num <= n:
            c_d.del_entry_phonebook(num)
        else:
            bot.send_message(message.chat.id, "Только цифра больше 0 и меньше " + str(n))
            bot.register_next_step_handler(message, del_entry_phonebook)
    else:
        bot.send_message(message.chat.id, "Только номер записи, цифра, больше 0 и меньше " + str(n))
        bot.register_next_step_handler(message, del_entry_phonebook)

def edit_entry_phonebook(message):
    global num
    num = message.text
    if num.isdigit():
        num = int(num)
        if 0 < num <= n:
            bot.send_message(message.chat.id, "Изменить:\n\
                1 - Фамилию\n\
                2 - Имя\n\
                3 - Номер телефона\n\
                4 - Комментарий\n ")
            bot.register_next_step_handler(message, edit_entry)
        else:
            bot.send_message(message.chat.id, "Только цифра больше 0 и меньше " + str(n))
            bot.register_next_step_handler(message, edit_entry_phonebook)
    else:
        bot.send_message(message.chat.id, "Только номер записи, цифра, больше 0 и меньше " + str(n))
        bot.register_next_step_handler(message, edit_entry_phonebook)

def edit_entry(message):
    global i
    i = message.text
    if i.isdigit():
        i = int(i)
        if 0 < i <= 4:
            bot.send_message(message.chat.id, "Введите новое значение поля записи")
            bot.register_next_step_handler(message, edit)
        else:
            bot.send_message(message.chat.id, "Только цифра от 1 до 4")
            bot.register_next_step_handler(message, edit_entry)
    else:
        bot.send_message(message.chat.id, "Только цифра от 1 до 4")
        bot.register_next_step_handler(message, edit_entry)

def edit(message):
    global num
    global i
    c_d.edit_entry_phonebook(num, i, message.text)

# bot.polling(none_stop=True, interval=0)
bot.polling()