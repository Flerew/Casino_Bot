from loader import *

@bot.message_handler(commands=['🎰Рулетки'])
def rulets(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = ('/rulet1_5000')
    item2 = ('/rulet2_20000')
    item3 = ('/rulet3_70000')
    item4 = ('/Выход_в_меню')

    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, '🤔Выберите режим рулетки', reply_markup=markup)