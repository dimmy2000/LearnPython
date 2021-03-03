from glob import glob
from random import choice
from telegram import ReplyKeyboardRemove
from utils import get_smile, play_random_numbers, main_keyboard


def greet_user(update, context):
    # Функция для приветствия пользователя
    print('Вызван /start')
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open('images/Scream.jpg', 'rb'))
    context.user_data['emoji'] = get_smile(context.user_data)
    start_keyboard = main_keyboard()
    update.message.reply_text(
        f'Привет, пользователь! {context.user_data["emoji"]} Ты вызвал команду /start\n'
        f'Ну и {update.message.from_user.first_name} же ты. Восхитительно!',
        reply_markup=start_keyboard
    )


def talk_to_me(update, context):
    # Функция эхо - повторяем сообщения пользователя
    context.user_data['emoji'] = get_smile(context.user_data)
    username = update.effective_user.first_name
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(
        f'Отличная работа, {username} {context.user_data["emoji"]}! Ты написал: {user_text}',
        reply_markup=ReplyKeyboardRemove
    )


def guess_number(update, context):
    # Игра "Угадай число": пользователь выбирает число, бот выбирает случайное число - победа достается тому, у кого
    # больше величина.
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


def send_cat_picture(update, context):
    # Функция передающая по запросу случайную картинку с котиком из папки на компьютере
    cat_photos_list = glob('images/cat*.jp*g')
    cat_pic_filename = choice(cat_photos_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pic_filename, 'rb'), reply_markup=main_keyboard())


def user_coordinates(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    coords = update.message.location
    update.message.reply_text(
        f"Ваши координаты {coords} {context.user_data['emoji']}!",
        reply_markup=main_keyboard()
    )
