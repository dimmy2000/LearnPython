"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься
  пользователь: учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат
  работы функции в переменную
* Вывести содержимое переменной на экран

"""


def prognose_activity(age):
    if age < 7:
        return 'Вы ходите в детский сад.'
    elif 6 < age < 18:
        return 'Вы учитесь в школе.'
    elif 17 < age < 23:
        return 'Вы студент ВУЗа.'
    else:
        return 'Опять работать?'


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    user_age = int(input('Введите ваш возраст: '))
    activity = prognose_activity(user_age)
    print(activity)


if __name__ == "__main__":
    main()
