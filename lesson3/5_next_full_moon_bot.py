import logging
from time import strftime, strptime

import ephem
from datetime import datetime
from settings import API_KEY, PROXY_URL, PROXY_USERNAME, PROXY_PASSWORD
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename='bot.log', format='%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S', level=logging.INFO)

# Настройки прокси
PROXY = {'proxy_url': PROXY_URL,
         'urllib3_proxy_kwargs': {'username': PROXY_USERNAME,
                                  'password': PROXY_PASSWORD}}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def get_next_full_moon(update, context):
    get_date = update.message.text.split()
    if len(get_date) > 1:
        some_date = get_date[1]
    else:
        some_date = datetime.now().strftime('%Y-%m-%d')
    update.message.reply_text(f'Следующее полнолуние будет {ephem.next_full_moon(some_date)}')
    print(f'Следующее полнолуние будет {ephem.next_full_moon(some_date)}')


def main():
    mybot = Updater(API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("next_full_moon", get_next_full_moon))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
