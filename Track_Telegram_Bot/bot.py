import logging
from handlers import greet_user, send_cat_picture, guess_number, user_coordinates, talk_to_me
from settings import API_KEY, PROXY_URL, PROXY_USERNAME, PROXY_PASSWORD
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

logging.basicConfig(filename='bot.log', format='%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S', level=logging.INFO)

# Настройки прокси
PROXY = {'proxy_url': PROXY_URL,
         'urllib3_proxy_kwargs': {'username': PROXY_USERNAME,
                                  'password': PROXY_PASSWORD}}


def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    my_bot = Updater(API_KEY, use_context=True, request_kwargs=PROXY)

    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("cat", send_cat_picture))
    dp.add_handler(MessageHandler(Filters.regex('^(Прислать котика)$'), send_cat_picture))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")

    # Командуем боту начать ходить в Telegram за сообщениями
    my_bot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    my_bot.idle()


if __name__ == "__main__":
    main()
