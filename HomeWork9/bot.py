#name bot Kite_training1_bot
# Use this token to access the HTTP API:
# 5557533810:AAGljPN-5omvkqL18kzN5CHyOjeCbf-64ns

import telebot
import controller as c

bot = telebot.TeleBot('5557533810:AAGljPN-5omvkqL18kzN5CHyOjeCbf-64ns')

@bot.message_handler(commands=['start'])
def start_message(message):
    c.phone_book()

bot.polling(none_stop=True, interval=0)
