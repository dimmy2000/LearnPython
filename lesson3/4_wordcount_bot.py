import logging
import string

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from settings import API_KEY, PROXY_URL, PROXY_USERNAME, PROXY_PASSWORD

logging.basicConfig(filename='bot.log', format='%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S', level=logging.INFO)

# Настройки прокси
PROXY = {'proxy_url': PROXY_URL,
         'urllib3_proxy_kwargs': {'username': PROXY_USERNAME,
                                  'password': PROXY_PASSWORD}}

# список окончаний
word_completion = ["о", "а", "" ]

# список спецсимволов
spec_char = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start\n'
                              f'Ну и {update.message.from_user.first_name} же ты. Восхитительно!')


def word_count(update, context):
    user_text = update.message.text

    # Проверка на спецсимволы
    for symbol in user_text:
        if symbol in string.punctuation:
            user_text = user_text.replace(symbol, "")

    user_text = user_text.split()[1:]

    # Проверка пустой строки
    if len(user_text) > 0:
        update.message.reply_text(f'{len(user_text)} слов' + completion(len(user_text)))
    else:
        update.message.reply_text('Пожалуйста, введите фразу, количество слов в которой нужно посчитать, '
                                  "после команды /wordcount")
    # print(user_text)


# Проверка окончаний слова
def completion(number):
    if number % 10 == 1 and number % 100 != 11:
        return word_completion[0]
    elif number % 10 >= 2 and number % 10 <= 4:
        if number % 100 < 12 or number % 100 > 14:
            return word_completion[1]
        else:
            return word_completion[2]
    else:
        return word_completion[2]


def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", word_count))

    logging.info("Бот стартовал")

    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()


if __name__ == "__main__":
    main()
