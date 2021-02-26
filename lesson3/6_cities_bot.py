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


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def cities_game(update, context):
    '''
    игра в города

    старт игры
    загрузка списка городов
    ввести город
        если город в списке городов
            найти последнюю букву в названии города
            удалить город из списка
            если "буква" не "ъ, ы, ь" иначе перейти к предыдущей букве
                если город начинающийся с "буквы" в списке городов
                    вывести название города
                    удалить город из списка
                    ввести город
                    если город начинается с "буквы"
                        если город в списке городов
                            найти последнюю букву в названии города
                            удалить город из списка
                            если "буква" не "ъ, ы, ь" иначе перейти к предыдущей букве
                            если город начинающийся с "буквы" в списке городов
                                вывести название города
                                удалить город из списка
                                ввести город
                                если город начинается с "буквы"
                                    <...>
                    иначе
                        Вы выиграли
                        конец игры
        иначе
            вывести сообщение "Не могу найти такой город в списке. Вы проиграли"
            конец игры
    '''


    if context.args:
        # старт игры
        context.user_data['cities'] = playing_intensifies(context.user_data)
        cities = context.user_data['cities']
        print(context.args)
        # ввести город игрока
        user_city = ' '.join(context.args).title()
        print(user_city)
        if user_city in cities:
            # удалить город из списка
            cities.remove(user_city)
            print(len(cities))
            # найти последнюю букву в названии города
            end_letter = get_letter(user_city)
            # если город начинающийся с "буквы" в списке городов
            # bot_city = [city for city in cities_list if city.lower().startswith(end_letter.lower())]
            bot_city = []
            for city in cities:
                if city[0].upper() == end_letter.upper():
                    bot_city.append(city)
            bot_city = bot_city[0]
            print(bot_city)
            # удалить город из списка
            cities.remove(bot_city)
            print(len(cities))
            # город игрока должен начинаться с "буквы"
            start_letter = get_letter(bot_city)
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


def playing_intensifies(user_data):
    # создаем для конкретного пользователя игральные переменные
    if 'cities' not in user_data:
        # загрузка списка городов
        with open('cities.txt', 'r', encoding='utf-8') as file:
            cities = file.read().split('\n')
            print(len(cities))
        return cities
    return user_data['cities']


def get_letter(cityname):
    index = -1
    list_of_wrong_endings = ["ъ", "ы", "ь"]
    # если "буква" не "ъ, ы, ь"
    if cityname[index].lower() not in list_of_wrong_endings:
        return cityname[index]
    # иначе
    else:
        # перейти к предыдущей букве
        cityname = cityname[:index]
        return get_letter(cityname)


def main():
    mybot = Updater(API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("cities", cities_game))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()