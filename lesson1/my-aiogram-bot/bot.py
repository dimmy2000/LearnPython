import logging
import aiohttp
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.builtin import CommandStart
from settings import API_KEY, PROXY_PASSWORD, PROXY_URL, PROXY_USERNAME

logging.basicConfig(filename='bot.log', format='%(asctime)s %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S', level=logging.INFO)

# Настройки прокси
PROXY_AUTH = aiohttp.BasicAuth(login=PROXY_USERNAME, password=PROXY_PASSWORD)


def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Bot(token=API_KEY, proxy=PROXY_URL, proxy_auth=PROXY_AUTH)
    dp = Dispatcher(mybot)

    @dp.message_handler(CommandStart())
    async def greet_user(message: types.Message):
        await message.answer('Привет, пользователь! Ты вызвал команду /start')
        print('Вызван /start')

    @dp.message_handler()
    async def talk_to_me(message: types.Message):
        await message.answer(message.text)
        print(message.text)

    if __name__ == '__main__':

        logging.info("Бот стартовал")

        # Командуем боту начать ходить в Telegram за сообщениями
        executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
