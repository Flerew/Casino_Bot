from loader import *


@bot.message_handler(commands=['Выход_в_меню'])
def exit_to_menu_command(message):
    id = init(message, 'id')
    if check_registration(message) is False:
       bot.send_message(message.chat.id, '⛔Нужно зарегестрироваться.\n/start\n/reg')

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('/📜информация')
        item2 = types.KeyboardButton('/💰баланс')
        item3 = types.KeyboardButton('/▶️игры')
        item4 = types.KeyboardButton('/🎰онлаин выйгрыши⛔')
        item5 = types.KeyboardButton('/💸Деньги в кредит⛔')
        item6 = types.KeyboardButton('/📨Перевод⛔')
        item7 = types.KeyboardButton('/🔑Промокоды⛔')
        item8 = types.KeyboardButton('/show_users')
        item9 = types.KeyboardButton('/edit_money')

        if id != admin_id:
            markup.add(item1, item2, item3, item4, item5, item6, item7)
        else:
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
            
        bot.send_message(message.chat.id, 'Что будем делать?', reply_markup=markup)