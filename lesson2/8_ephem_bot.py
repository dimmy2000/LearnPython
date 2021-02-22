"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import random
from datetime import datetime

import ephem
from settings import token
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}

planets = [
    'Mercury', 'Venus', 'Mars', 'Jupiter',
    'Saturn', 'Uranus', 'Neptune', 'Pluto'
]


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def get_constellation(update, context):
    get_planet = update.message.text.split()
    if len(get_planet) > 1:
        planet = get_planet[1].capitalize()
    else:
        planet = planets[random.randint(0, 7)]

    today = datetime.today().strftime(r'%Y/%m/%d')

    if planet in planets:
        some_planet = getattr(ephem, planet)(today)
        constellation = ephem.constellation(some_planet)
        print(constellation[1])
        update.message.reply_text(f'Планета {planet} сегодня находится в '
                                  f'созвездии {constellation[1]}')
    else:
        update.message.reply_text('Не могу найти планету. Проверьте наличие '
                                  'опечаток в названии или планеты на небе')


def main():
    mybot = Updater(token, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
