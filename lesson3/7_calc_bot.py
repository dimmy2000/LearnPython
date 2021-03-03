import logging
from operator import pow, truediv, mul, add, sub
from settings import API_KEY, PROXY_URL, PROXY_USERNAME, PROXY_PASSWORD
from telegram.ext import Updater, CommandHandler

logging.basicConfig(filename='bot.log', format='%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S', level=logging.INFO)

# Настройки прокси
PROXY = {'proxy_url': PROXY_URL,
         'urllib3_proxy_kwargs': {'username': PROXY_USERNAME,
                                  'password': PROXY_PASSWORD}}

# Список поддерживаемых символов математических операций
operators = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
    '^': pow
}


def calculate(calc_expr):
    if calc_expr.isdigit():
        return float(calc_expr)
    for key in operators.keys():
        left, operator, right = calc_expr.partition(key)
        if operator in operators:
            return operators[operator](calculate(left), calculate(right))


def greet_user(update, context):
    print('Вызван /start')
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open('images/Scream.jpg', 'rb'))
    update.message.reply_text(
        f'Привет, пользователь! Ты вызвал команду /start\n'
        f'Ну и {update.message.from_user.first_name} же ты. Восхитительно!'
    )


def get_calc_result(update, context):
    if context.args:
        calc_expr = ''.join(context.args)
        # print('выражение:', calc_expr)
        try:
            if calc_expr.isalpha():
                raise TypeError
            # print('результат: ', calculate(calc_expr))
            update.message.reply_text(f'Результат вычисления: {calculate(calc_expr)}')
        except ZeroDivisionError:
            update.message.reply_text('Ошибка деления: на ноль делить нельзя.\nВведите другое выражение')
        except TypeError:
            update.message.reply_text('Ошибка: неподдерживаемое выражение.\nДля получения результата расчета '
                                      'используйте только числа и поддерживаемые операторы. Для получения списка '
                                      'поддерживаемых операторов введите /calc')
    else:
        update.message.reply_text('Нет данных для расчета. После команды /calc нужно указать выражение, которое хотите '
                                  'рассчитать. Используйте операторы:\n'
                                  '"+" - для сложения,\n'
                                  '"-" - для вычитания,\n'
                                  '"*" - для умножения,\n'
                                  '"/" - для деления,\n'
                                  '"^" - для возведения в степень\n')


def main():
    mybot = Updater(API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("calc", get_calc_result))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
