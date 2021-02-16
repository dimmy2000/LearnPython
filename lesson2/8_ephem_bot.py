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

import ephem

import random

from datetime import datetime

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

    if planet == 'Mercury':
        mars = ephem.Mercury(today)
        constellation = ephem.constellation(mars)

    elif planet == 'Venus':
        mars = ephem.Venus(today)
        constellation = ephem.constellation(mars)

    elif planet == 'Mars':
        mars = ephem.Mars(today)
        constellation = ephem.constellation(mars)

    elif planet == 'Jupiter':
        mars = ephem.Jupiter(today)
        constellation = ephem.constellation(mars)

    elif planet == 'Saturn':
        mars = ephem.Saturn(today)
        constellation = ephem.constellation(mars)

    elif planet == 'Uranus':
        mars = ephem.Uranus(today)
        constellation = ephem.constellation(mars)

    elif planet == 'Neptune':
        mars = ephem.Neptune(today)
        constellation = ephem.constellation(mars)

    elif planet == 'Pluto':
        mars = ephem.Pluto(today)
        constellation = ephem.constellation(mars)

    print(constellation[1])
    update.message.reply_text(f'Планета {planet} сегодня находится в '
                              f'созвездии {constellation[1]}')


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
