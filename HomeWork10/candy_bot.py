import logging
import candy_def as c_d

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

reply_keyboard = [['/play', '/info', '/close']]
stop_keyboard = [['/stop']]

markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
stop_markup = ReplyKeyboardMarkup(stop_keyboard, resize_keyboard=True, one_time_keyboard=False)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '5557533810:AAGljPN-5omvkqL18kzN5CHyOjeCbf-64ns'

candy = 0
take_max = 0
def start(update, context):
    update.message.reply_text(
        "Привет! Я игровой бот.\nЯ знаю игру: кто последний возьмёт конфеты!\nДавай играть!",
        reply_markup=markup
    )

def play(update, context):
    update.message.reply_text('Введите колличество конфет в игре (не меньше 10)', reply_markup=stop_markup)
    return 1
    
def play_candy(update, context):
    global candy
    num = c_d.chek_candy(update.message.text, 10)
    if num:
        candy = num
    else:
        update.message.reply_text('Введите колличество конфет в игре (не меньше 10)')
        return 1
    update.message.reply_text('Сколько максимум конфет можно брать за 1 ход? (не меньше 3)')
    return 2

def play_candy_take(update, context):
    global candy
    global take_max
    num = c_d.chek_candy(update.message.text, 3)
    if num:
        take_max = num
    else:
        update.message.reply_text('Сколько максимум конфет можно брать за 1 ход? (не меньше 3)')
        return 2
    update.message.reply_text(f'На столе лежит {candy} конфета.\n За один ход можно забрать не более {take_max} конфет.\n Все конфеты оппонента достаются сделавшему последний ход.\nСколько конфет вы возьмете?')
    return 3

def game_candy(update, context):
    global candy
    global take_max
    num = c_d.chek_nums(update.message.text, candy, take_max)
    if num:
        candy -= num
        update.message.reply_text(f'Конфет осталось: {candy}')
        if candy == 0:
            update.message.reply_text(f'Вы победили 🥳', reply_markup=markup)
            context.bot.send_document(chat_id=update.effective_chat.id, document='https://tenor.com/view/panda-mini-panda-gif-25524945')
            return ConversationHandler.END
        else:
            num = c_d.howmuch(candy, take_max)
            candy -= num
            update.message.reply_text(f'Бот взял {num} и конфет осталось: {candy}')
            if candy == 0:
                update.message.reply_text(f'Победил бот 💔', reply_markup=markup)
                context.bot.send_document(chat_id=update.effective_chat.id, document='https://i.gifer.com/IN3.gif')
                return ConversationHandler.END
            else:
                update.message.reply_text('Сколько конфет вы возьмете?')
                return 3
    else:
        update.message.reply_text(f'''Введите корректное значение
        \nЭто должно быть число,
        \nне больше {take_max}
        \nи не превышать количество оставшихся конфет ({candy})
        \nСколько конфет вы возьмете?''')
        return 3

def stop(update, context):
    update.message.reply_text("Всего доброго!", reply_markup=markup)
    return ConversationHandler.END

def info(update, context):
    update.message.reply_text(
        "На столе лежит некоторое количество конфет\n\nЗа один ход можно забрать не более чем n конфет.\n\nНачальное количество конфет и сколько конфет можно взять за 1 раз определяется в начале игры.\n\nПобеждает тот, кто сделает последний ход.")

def close(update, context):
    update.message.reply_text(
        "Спасибо за игру!",
    reply_markup=ReplyKeyboardRemove())


play_handler = ConversationHandler(
        entry_points=[CommandHandler('play', play)],

        # Состояние внутри диалога.
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, play_candy)],
            2: [MessageHandler(Filters.text & ~Filters.command, play_candy_take)],
            3: [MessageHandler(Filters.text & ~Filters.command, game_candy)],
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(play_handler)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("info", info))
    dp.add_handler(CommandHandler("close", close))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()