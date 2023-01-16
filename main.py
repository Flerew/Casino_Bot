while True:
    try:
        from handlers import *
        from loader import *

        bot.polling(non_stop=True)

    except:
        print('Error')
        continue