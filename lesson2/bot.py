from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text('Какой-то ответ бота')

def greet_user(bot, update):
    print (update)
    update.message.reply_text('Приветствую тебя!')

def main():
    mybot = Updater("762100811:AAEyhuem2xz8Okqs2tMk5MJGhNGsBXpG7bo", request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

main()