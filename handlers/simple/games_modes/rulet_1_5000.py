from loader import *


@bot.message_handler(commands=['rulet1_5000'])
def rulet_command_1(message):
    id = init(message, 'id')
    money = init(message, 'cash')

    num = random.choice(rulet_1)

    if money >= 5000:

        money = money - 5000
        bot.send_message(message.chat.id, f'🎰Крутим барабан\nВаш баланс {money}')
        money = money + num

        cursor.execute(f"UPDATE info_users SET cash = {money} WHERE id = {id}")
        connect.commit()



        if num >= 5000:
            bot.send_message(message.chat.id, f'🏆Поздравляю, вы выйграли {num}\nВаш баланс: {money}')

        else:
            bot.send_message(message.chat.id, f'😢К сажелению вы выйграли только {num}\nВаш баланс: {money}')


    else:
        bot.send_message(message.chat.id, '⛔Недостаточно монет')