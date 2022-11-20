from loader import *

@bot.message_handler(commands=['start'])
def start(message):
    id = init(message, 'id')
    cursor.execute(f"SELECT id FROM info_users WHERE id = {id}")
    if cursor.fetchone() is None:
        register(message)

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('/📜информация')
        item2 = types.KeyboardButton('/💰баланс')
        item3 = types.KeyboardButton('/▶️игры')
        item4 = types.KeyboardButton('/🎰онлаин выйгрыши⛔')
        item5 = types.KeyboardButton('/💸Деньги в кредит⛔')
        item6 = types.KeyboardButton('/📨Перевод⛔')
        item7 = types.KeyboardButton('/🔑Промокоды⛔')

        markup.add(item1, item2, item3, item4, item5, item6, item7)
        bot.send_message(message.chat.id, 'Что будем делать?', reply_markup=markup)


@bot.message_handler(commands=['reg'])
def register(message):
    id = message.from_user.id
    cursor.execute(f"SELECT id FROM info_users WHERE id = {id}")
    if cursor.fetchone() is None:

        sent = bot.send_message(message.chat.id, 'Введите желаемый nik name')
        bot.register_next_step_handler(sent, last_reg)
    else:
        bot.send_message(message.chat.id, '⛔Вы уже зарегистрировались')
        start(message)


def last_reg(message):
    nik = message.text
    id = message.from_user.id

    if cursor.fetchone() is None:
        if nik in impos:
            bot.send_message(message.chat.id, '🚫Такой ник нельзя использовать или в нём есть запрещенные символы')


        else:
            cursor.execute("INSERT INTO info_users VALUES (?, ?, ?)", (id, str(nik), 5000))
            connect.commit()

        l = bot.send_message(message.chat.id, f'Регистрация завершена, вам начисленно 5000\n Ваш ник: {nik} ')
        for value in cursor.execute("SELECT * FROM info_users"):
            print(value)
        print('\n')
        start(message)

    else:
        bot.send_message(message.chat.id, '🚫Такой ник уже есть')
        register(message)
