from loader import *
from handlers.exit_to_menu import *

@bot.message_handler(commands=['✖️Множитель'])
def multiplier_command(message):
    cash = init(message, 'cash')

    msg = bot.send_message(message.chat.id, f"Ты можешь выйграть множитель твоей ставки, от 0 до 10.\nТвой баланс: {cash}\nВыбери сумму ставки, чем больше ставка, тем больше шанс.\n\n0 - для отмены")
    bot.register_next_step_handler(msg, casino)


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

        else:
            bot.send_message(message.chat.id, '⛔Недостаточно монет для ставки')
    else:
        bot.send_message(message.chat.id, '⛔Вы ввели не число')
