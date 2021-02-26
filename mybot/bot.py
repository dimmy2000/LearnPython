from glob import glob
from emoji import emojize
import logging
from random import randint, choice

from settings import API_KEY, PROXY_URL, PROXY_USERNAME, PROXY_PASSWORD, USER_EMOJI
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

logging.basicConfig(filename='bot.log', format='%(asctime)s %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S', level=logging.INFO)

# Настройки прокси
PROXY = {'proxy_url': PROXY_URL,
         'urllib3_proxy_kwargs': {'username': PROXY_USERNAME,
                                  'password': PROXY_PASSWORD}}


def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(CommandHandler("cat", send_cat_picture))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")

    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()


def greet_user(update, context):
    # функция для приветствия пользователя
    print('Вызван /start')
    chat_id = update.effective_chat.id
    file_id = "AgACAgIAAxkBAAEIYOJgOBL3LbcH5fVOAAG0BN36mKvs-2sAAmGyMRuOBcBJMVNMndUQ2S1U9hibLgADAQADAgADbQADoacCAAEeBA"
    context.bot.send_photo(chat_id=chat_id, photo=file_id)
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f'Привет, пользователь! {context.user_data["emoji"]} Ты вызвал команду /start\n'
                              f'Ну и {update.message.from_user.first_name} же ты. Восхитительно!')


def talk_to_me(update, context):
    # функция эхо - повторяем сообщения пользователя
    context.user_data['emoji'] = get_smile(context.user_data)
    username = update.effective_user.first_name
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(f'Отличная работа, {username} {context.user_data["emoji"]}! Ты написал: {user_text}')


def guess_number(update, context):
    '''
    Игра "Угадай число": пользователь выбирает число, бот выбирает случайное число - победа достается тому, у кого
    больше величина.
    '''
    print(context.args)
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except (TypeError, ValueError):
            message = "Введите целое число"
    else:
        message = "Введите число"
    update.message.reply_text(message)


def play_random_numbers(user_number):
    # функция для игры в "угадай число"
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f"Ваше число {user_number}, мое {bot_number}. Вы выиграли."
    elif user_number == bot_number:
        message = f"Ваше число {user_number}, мое {bot_number}. Ничья."
    else:
        message = f"Ваше число {user_number}, мое {bot_number}. Вы проиграли."
    return message


def send_cat_picture(update, context):
    # функция передающая по запросу случайную картинку с котиком из папки на компьютере
    cat_photos_list = glob('images/cat*.jp*g')
    cat_pic_filename = choice(cat_photos_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pic_filename, 'rb'))

def get_smile(user_data):
    # функция, которая возвращает случайный смайлик из списка
    if 'emoji' not in user_data:
        smile = choice(USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']


if __name__ == "__main__":
    main()
