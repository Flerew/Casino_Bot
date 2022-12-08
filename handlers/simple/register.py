from loader import *


@bot.message_handler(commands=['reg'])
def register(message):
    id = message.from_user.id
    cursor.execute(f"SELECT id FROM info_users WHERE id = {id}")
    if cursor.fetchone() is None:

        sent = bot.send_message(message.chat.id, 'Введите желаемый nik name')
        bot.register_next_step_handler(sent, last_reg)
    else:
        bot.send_message(message.chat.id, '⛔Вы уже зарегистрировались')


def last_reg(message):
    nik = message.text
    id = message.from_user.id

    if cursor.fetchone() is None:
        if nik in impos:
            bot.send_message(message.chat.id, '🚫Такой ник нельзя использовать или в нём есть запрещенные символы')


        else:
            cursor.execute("INSERT INTO info_users VALUES (?, ?, ?)", (id, str(nik), 5000))
            connect.commit()

        l = bot.send_message(message.chat.id, f'Регистрация завершена, вам начисленно 5000\n Ваш ник: {nik} \n Выход_в_меню')
        for value in cursor.execute("SELECT * FROM info_users"):
            print(value)
        print('\n')


    else:
        bot.send_message(message.chat.id, '🚫Такой ник уже есть')
        register(message)