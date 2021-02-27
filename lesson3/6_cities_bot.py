from cities import cities_list
import logging
from mybot.settings import API_KEY, PROXY_URL, PROXY_USERNAME, PROXY_PASSWORD
from telegram.ext import Updater, CommandHandler

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

# Настройки прокси
PROXY = {'proxy_url': PROXY_URL,
         'urllib3_proxy_kwargs': {'username': PROXY_USERNAME,
                                  'password': PROXY_PASSWORD}}


def greet_user(update, context):
    print('Вызван /start')
    chat_id = update.effective_chat.id
    file_id = "AgACAgIAAxkBAAEIYOJgOBL3LbcH5fVOAAG0BN36mKvs-2sAAmGyMRuOBcBJMVNMndUQ2S1U9hibLgADAQADAgADbQADoacCAAEeBA"
    context.bot.send_photo(chat_id=chat_id, photo=file_id)
    update.message.reply_text(f'Привет, пользователь! Ты вызвал команду /start\n'
                              f'Ну и {update.message.from_user.first_name} же ты. Восхитительно!')


def cities_game(update, context):
    if context.args:
        # старт игры
        print(context.user_data)
        context.user_data['cities'] = playing_intensifies(context.user_data)
        cities = context.user_data['cities']
        print(context.args)
        print(context.user_data)
        # ввести город игрока
        user_city = ' '.join(context.args).title()
        print(user_city)

        # if context.user_data['start_letter'] in context.user_data:
        #     try:
        #         update.message.reply_text('Продолжаем')
        #     except Exception as err:
        #         print(err)
        # else:
        #     update.message.reply_text('Добро пожаловать в игру')

        if user_city in cities:
            # удалить город из списка
            cities.remove(user_city)
            print(len(cities))
            # найти последнюю букву в названии города
            context.user_data['end_letter'] = get_letter(user_city)
            # если город начинающийся с "буквы" в списке городов
            # bot_city = [city for city in cities_list if city.lower().startswith(end_letter.lower())]
            bot_city = []
            for city in cities:
                if city[0].upper() == context.user_data['end_letter'].upper():
                    bot_city.append(city)
            bot_city = bot_city[0]
            print(bot_city)
            # удалить город из списка
            cities.remove(bot_city)
            print(len(cities))
            # город игрока должен начинаться с "буквы"
            context.user_data['start_letter'] = get_letter(bot_city)
            # вывести сообщение
            update.message.reply_text(f'Вы ввели город: <b>{user_city}</b>.\nМне надо выбрать город, начинающийся '
                                      f'на букву <b><i>{context.user_data["end_letter"].upper()}</i></b>.\n'
                                      f'Мой город: <b>{bot_city}</b>.\nВведите город, начинающийся с буквы '
                                      f'<b><i>{context.user_data["start_letter"].upper()}</i></b>.',
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
        cities = cities_list
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
