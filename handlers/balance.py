from loader import *

@bot.message_handler(commands=['💰баланс'])
def balance_command(message):
    if check_registration(message) is False:
        bot.send_message(message.chat.id, '⛔Нужно зарегестрироваться.\n/start\n/reg')

    else:
        id = init(message, 'id')
        balance = init(message, 'cash')
        bot.send_message(message.chat.id, f'Ваш баланс: {balance}')