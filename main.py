from loader import *
from handlers import *

@bot.message_handler(commands=['💰баланс'])
def balance_command(message):
    if check_registration(message) is False:
        bot.send_message(message.chat.id, '⛔Нужно зарегестрироваться.\n/start\n/reg')

    else:
        id = init(message, 'id')
        balance = init(message, 'cash')
        bot.send_message(message.chat.id, f'Ваш баланс: {balance}')


@bot.message_handler(commands=['▶️игры'])
def games_command(message):
    check_registration(message)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('🎲Колесо фортуны⛔')
    item2 = types.KeyboardButton('🎰Рулетка⛔')
    item3 = types.KeyboardButton('✖️Множитель')
    item4 = types.KeyboardButton('Выход в меню')

    markup.add(item1, item2, item3, item4)
    choice_game = bot.send_message(message.chat.id, 'Выберите режим игры', reply_markup=markup)
    bot.register_next_step_handler(choice_game, games)



def games(message):
    # if message.text == '🎲Колесо фортуны':

    # i = bot.send_message(message.chat.id, 'Выбери рулетку, ниже указана стоимость🎰\n1)5000\n2)20000\n3)70000')
    # bot.register_next_step_handler(i, rulet)

    if message.text == '✖️Множитель':
        cash = init(message, 'cash')

        msg = bot.send_message(message.chat.id,
                               f"Ты можешь выйграть множитель твоей ставки, от 0 до 10.\nТвой баланс: {cash}\nВыбери сумму ставки, чем больше ставка, тем больше шанс.\n\n0 - для отмены")
        bot.register_next_step_handler(msg, casino)

    elif message.text == 'Выход в меню':
        start(message)


def casino(message):
    id = init(message, 'id')
    money = init(message, 'cash')

    bet = message.text

    if bet.isdigit():
        bet = int(bet)
        money = int(money)

        if bet == 0:
            pass

        elif bet <= money:
            num = random.randrange(0, 100)
            if num <= 65:
                xbet = 0
            elif num >= 66 and num <= 75:
                xbet = 1
            elif num >= 76 and num <= 80:
                xbet = 2
            elif num >= 81 and num <= 84:
                xbet = 3
            elif num >= 85 and num <= 89:
                xbet = 4
            elif num >= 90 and num <= 92:
                xbet = 5
            elif num >= 93 and num <= 94:
                xbet = 6
            elif num == 95:
                xbet = 7
            elif num == 96:
                xbet = 8
            elif num >= 97 and num <= 98:
                xbet = 9
            elif num >= 99 and num <= 100:
                xbet = 10

            print(num, xbet)
            if xbet == 0:
                money = money - bet

                bot.send_message(message.chat.id, f'😢К сажелению вы проиграли\nВаш баланс: {money}')


            elif xbet == 1:
                bot.send_message(message.chat.id,
                                 f'🙃Вы нечего не выйграли, но и не проиграли, ваш множитель: 1\nВаш баланс: {money}')


            else:
                money = money + bet * xbet
                bot.send_message(message.chat.id, f'💰Поздравляю, вы выйграли множитель: {xbet}\nВаш баланс: {money}')

            cursor.execute(f"UPDATE info_users SET cash = {money} WHERE id = {id}")
            connect.commit()
            start(message)

        else:
            bot.send_message(message.chat.id, '⛔Недостаточно монет для ставки')
    else:
        bot.send_message(message.chat.id, '⛔Вы ввели не число')


# def rulet(message):
# init(message)

# bet = message.text
# if bet.isdigit():
# bot.send_message(message.chat.id, 'Крутим барабан')
# ran = random.randrange(0, 10)


bot.polling(non_stop=True)