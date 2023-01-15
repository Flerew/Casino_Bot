from loader import *
text = {}

@bot.message_handler(commands=['Сообщить_об_ошибке'])
def errors_command(message):
    global text
    if text:
        pass
    else:
        text = {}
    mess_time = datetime.date.today()

    if mess_time != datetime.date.today():  # Если дата не сегодня, сбрасываем все сообщения
        text = {}
    if message.from_user.id not in text:  # Если пользователь не писал сообщения, то добавляем его ID в словарь и присваиваем 0 сообщений
        text[message.from_user.id] = 0
    if text[message.from_user.id] >= 2:  # Ставим ограничения на кол-во сообщений
        bot.send_message(message.from_user.id,
                         'Твой лимит исчерпан!\nПопробуй ' + str(datetime.date.today() + datetime.timedelta(days=1)))
    else:
        text[message.from_user.id] = qty_mess(text[message.from_user.id])
        print(text)
        i = bot.send_message(message.chat.id,
                             'Спасибо за обращение, пожалуйста подробно опишите при каких действиях произошла ошибка')
        bot.register_next_step_handler(i, last_errors_command)


def last_errors_command(message):
    report = message.text
    nik = init(message, 'nik')
    bot.send_message(admin_id, f'Жалоба от игрока "{nik}"\n{report}')