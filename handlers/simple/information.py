from loader import *

@bot.message_handler(commands=['📜информация'])
def information_command(message):
    check_registration(message)
    id = init(message, 'id')
    nik = init(message, 'nik')

    bot.send_message(message.chat.id,  f"Ваш id: {id}\nВаш ник: {nik}\n/Сообщить об ошибке")
