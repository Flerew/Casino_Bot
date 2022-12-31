from loader import *

@bot.message_handler(commands=['edit_money'])
def edit_money(message):
    id = init(message, 'id')
    nik = init(message, 'nik')

    if id == admin_id:
        i = bot.send_message(message.chat.id, 'Введите имя')
        bot.register_next_step_handler(i, next_edit)


    else:
        bot.send_message(admin_id, f'Пользователь {nik} пытался использовать команду edit_money')

def next_edit(message):
    global player
    player = message.text
    user = cursor.execute(f"SELECT id FROM info_users WHERE nik_name = '{player}'")
    if cursor.fetchone()[0]:
        i = bot.send_message(message.chat.id, 'введите нужное кол-во')
        bot.register_next_step_handler(i, last_edit)


    else:
        bot.send_message(message.chat.id, 'Такого ника нет')


def last_edit(message):

    money = message.text


    if money.isdigit():
        int(money)
        cursor.execute(f"UPDATE info_users SET cash = {money} WHERE nik_name = '{player}'")
        connect.commit()
        bot.send_message(message.chat.id, 'Все изменено!')


    else:
        bot.send_message(message.chat.id, 'Не верный тип данных')


