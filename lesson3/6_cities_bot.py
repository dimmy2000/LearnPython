import logging
from time import strftime, strptime

import ephem
from datetime import datetime
from settings import API_KEY, PROXY_URL, PROXY_USERNAME, PROXY_PASSWORD
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

# Настройки прокси
PROXY = {'proxy_url': PROXY_URL,
         'urllib3_proxy_kwargs': {'username': PROXY_USERNAME,
                                  'password': PROXY_PASSWORD}}

# загрузка списка городов
with open('cities.txt', 'r', encoding='utf-8') as cities:
    cities_list = cities.read().split('\n')
    print(len(cities_list))

start_letter = 0
end_letter = 0


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def cities_game(update, context):
    # старт игры
    # ввести город игрока
    get_city = update.message.text.split()
    if len(get_city) > 1:
        user_city = ' '.join(get_city[1:]).title()
        print(user_city)
        if user_city in cities_list:
            # удалить город из списка
            user_city = cities_list.pop(cities_list.index(user_city))
            print(len(cities_list))
            # найти последнюю букву в названии города
            end_letter = get_end_letter(user_city)
            # если город начинающийся с "буквы" в списке городов
            # bot_city = [city for city in cities_list if city.lower().startswith(end_letter.lower())]
            bot_city = []
            for city in cities_list:
                if city[0].upper() == end_letter.upper():
                    bot_city.append(city)
            bot_city = bot_city[0]
            print(bot_city)
            # удалить город из списка
            cities_list.remove(bot_city)
            print(len(cities_list))
            # город игрока должен начинаться с "буквы"
            start_letter = get_end_letter(bot_city)
            # вывести сообщение
            update.message.reply_text(f'Вы ввели город: <b>{user_city}</b>.\nМне надо выбрать город, начинающийся '
                                      f'на букву <b><i>{end_letter.upper()}</i></b>.\nМой город: <b>{bot_city}</b>.\n'
                                      f'Введите город, начинающийся с буквы <b><i>{start_letter.upper()}</i></b>.',
                                      parse_mode="HTML")
        # иначе
        else:
            # вывести сообщение
            print('Не могу найти такой город в списке.')
            update.message.reply_text('Не могу найти такой город в списке.')
    else:
        update.message.reply_text('Чтобы поиграть со мной в "города" - введи название российского города после '
                                  'команды /cities')


def get_end_letter(cityname):
    index = -1
    list_of_wrong_endings = ["ъ", "ы", "ь"]
    # если "буква" не "ъ, ы, ь"
    if cityname[index].lower() not in list_of_wrong_endings:
        return cityname[index]
    # иначе
    else:
        # перейти к предыдущей букве
        cityname = cityname[:index]
        return get_end_letter(cityname)


def main():
    mybot = Updater(API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("cities", cities_game))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()