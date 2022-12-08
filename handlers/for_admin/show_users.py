from loader import *


@bot.message_handler(commands=['show_users'])
def show_users_command(message):
    id = init(message, 'id')

    if id != admin_id:
        bot.send_message(message.chat.id, 'Как тебе не стыдно? За это ты получишь штраф! В размере 1000 монет')

        cursor.execute(f"SELECT cash FROM info_users WHERE id = {id}")
        money = cursor.fetchone()[0]
        money = money - 1000

        cursor.execute(f"UPDATE info_users SET cash = {money} WHERE id = {id}")
        connect.commit()

    else:
        cursor.execute("SELECT * FROM info_users")
        table = cursor.fetchall()

        reply_message = "Це база даних \n\n"
        for i, item in enumerate(table):
            reply_message += f"{i + 1}. {item[1]} - ({item[0]}) - {item[2]} - "

        bot.send_message(message.chat.id, reply_message)