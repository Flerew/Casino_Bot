from loader import *

@bot.message_handler(commands=['📨Перевод'])
def transfer_command(message):
    if check_registration(message) is False:
        bot.send_message(message.chat.id, '⛔Нужно зарегестрироваться.\n/start\n/reg')
    else:
        i = bot.send_message(message.chat.id, 'Введи ник игрока которому хотите перевести деньги')
        bot.register_next_step_handler(i, transfer_1)

def transfer_1(message):
    global recipient
    recipient = message.text

    cursor.execute(f"SELECT id FROM info_users WHERE nik_name = '{recipient}'")
    if cursor.fetchone():
        i = bot.send_message(message.chat.id, 'Выберите сумму')
        bot.register_next_step_handler(i, last_transfer)

    else:
        bot.send_message(message.chat.id, '⛔Такого игрока не существует')


def last_transfer(message):
    amount = message.text
    if amount.isdigit():
        amount = int(amount)
        id = init(message, 'id')
        cursor.execute(f"UPDATE info_users SET cash = cash - {amount} WHERE id = {id}")
        cursor.execute(f"UPDATE info_users SET cash = cash + {amount} WHERE nik_name = '{recipient}'")
        connect.commit()

        bot.send_message(message.chat.id, 'Перевод прошел успешно!')

    else:
        bot.send_message(message.chat.id, '⛔Вы ввели не число')

