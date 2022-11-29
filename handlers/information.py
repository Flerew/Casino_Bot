from loader import *

@bot.message_handler(commands=['📜информация'])
def information_command(message):
    check_registration(message)
    id = init(message, 'id')
    nik = init(message, 'nik')

    bot.send_message(message.chat.id,  f"Этот бот создан для улучшения качества программирования одного дурочка\nВаш id: {id}\nВаш ник: {nik}")
