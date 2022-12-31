from loader import *

@bot.message_handler(commands=['▶️игры'])
def games_command(message):
    if check_registration(message) is False:
        bot.send_message(message.chat.id, '⛔Нужно зарегестрироваться.\n/start\n/reg')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('/🎲Колесо фортуны⛔')
    item2 = types.KeyboardButton('/🎰Рулетки')
    item3 = types.KeyboardButton('/✖️Множитель')
    item4 = types.KeyboardButton('/Выход_в_меню')

    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, "🤔Выберите режим игры", reply_markup=markup)

