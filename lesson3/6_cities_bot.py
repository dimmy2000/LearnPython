from cities import cities_list
import logging
from settings import API_KEY, PROXY_URL, PROXY_USERNAME, PROXY_PASSWORD
from telegram.ext import Updater, CommandHandler

logging.basicConfig(filename='bot.log', format='%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S', level=logging.INFO)

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


class WrongLetterError(Exception):
    pass


def cities_game(update, context):
    if context.args:
        # ввести город игрока
        user_city = ' '.join(context.args).title()
        print(user_city)
        print(context.user_data)


        # если игра продолжается
        if 'start_letter' in context.user_data.keys():
            start_letter = context.user_data['start_letter']
            # проверяем совпадает ли первая буква в городе игрока с последней буквой города бота
            if user_city[0].upper() != start_letter.upper():
                update.message.reply_text(f'Выбранный Вами город {user_city} начинается не с буквы '
                                          f'<b><i>{start_letter.upper()}</i></b>.\n'
                                          'Вы проиграли',
                                          parse_mode="HTML")
                context.user_data.clear()
                print('Defeat')
                print(context.user_data)
                raise WrongLetterError()
        else:
            update.message.reply_text('Добро пожаловать в игру')
            print(context.user_data)

        # старт игры
        context.user_data['cities'] = playing_intensifies(context.user_data)
        cities = context.user_data['cities']
        print(context.args)

        if user_city in cities:
            # удалить город из списка
            cities.remove(user_city)
            print(len(cities))
            # найти последнюю букву в названии города
            context.user_data['end_letter'] = get_letter(user_city)
            end_letter = context.user_data['end_letter']
            bot_city = []

            for city in cities:
                # если город начинающийся с "буквы" в списке городов
                if city[0].upper() == end_letter.upper():
                    bot_city.append(city)

            if len(bot_city) > 0:
                # продолжаем играть
                bot_city = bot_city[0]
            else:
                # иначе игрок победил
                update.message.reply_text(f"Не могу найти слово, начинающееся на букву "
                                          f"<b><i>{end_letter.upper()}</i></b>\n"
                                          f"Победа за вами.")
                context.user_data.clear()
                print('Victory')

            # удалить город из списка
            cities.remove(bot_city)
            print(len(cities))
            # город игрока должен начинаться с "буквы"
            context.user_data['start_letter'] = get_letter(bot_city).upper()
            start_letter = context.user_data['start_letter']
            # вывести сообщение
            update.message.reply_text(f'Вы ввели город: <b>{user_city}</b>.\nМне надо выбрать город, начинающийся '
                                      f'на букву <b><i>{end_letter.upper()}</i></b>.\n'
                                      f'Мой город: <b>{bot_city}</b>.\nВведите город, начинающийся с буквы '
                                      f'<b><i>{start_letter.upper()}</i></b>.',
                                      parse_mode="HTML")
        else:
            # вывести сообщение
            update.message.reply_text('Не могу найти такой город в списке. Вы проиграли')
            context.user_data.clear()
            print('Defeat')
    else:
        update.message.reply_text('Чтобы поиграть со мной в "города" - введи название российского города после '
                                  'команды /cities')


def playing_intensifies(user_data):
    # создаем для конкретного пользователя игральные переменные
    if 'cities' not in user_data:
        # загрузка списка городов
        cities = cities_list.copy()
        print(len(cities))
        return cities
    return user_data['cities']


def get_letter(cityname):
    index = -1
    list_of_wrong_endings = ["ц", "ъ", "ы", "ь"]
    # если "буква" не "ц, ъ, ы, ь"
    if cityname[index].lower() not in list_of_wrong_endings:
        return cityname[index]
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
