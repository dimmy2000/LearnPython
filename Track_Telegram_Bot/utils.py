from emoji import emojize
from random import randint, choice
from settings import USER_EMOJI
from telegram import ReplyKeyboardMarkup, KeyboardButton


def get_smile(user_data):
    # Функция, которая возвращает случайный смайлик из списка
    if 'emoji' not in user_data:
        smile = choice(USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']


def play_random_numbers(user_number):
    # Функция для игры в "угадай число"
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f"Ваше число {user_number}, мое {bot_number}. Вы выиграли."
    elif user_number == bot_number:
        message = f"Ваше число {user_number}, мое {bot_number}. Ничья."
    else:
        message = f"Ваше число {user_number}, мое {bot_number}. Вы проиграли."
    return message


def main_keyboard():
    return ReplyKeyboardMarkup(keyboard=[['Прислать котика', KeyboardButton('Мои координаты', request_location=True)]],
                               resize_keyboard=True)
