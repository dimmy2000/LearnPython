"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import datetime, timedelta
import locale
from time import strptime, strftime

locale.setlocale(locale.LC_ALL, "russian")


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    dt_now = datetime.now()
    delta_yesterday = timedelta(days=-1)
    delta_30_days_ago = timedelta(days=-30)
    dt_yesterday = dt_now + delta_yesterday
    dt_30_days_ago = dt_now + delta_30_days_ago

    print('Сегодня', dt_now.strftime('%A %d %B %Y'))
    print('Вчера', dt_yesterday.strftime('%A %d %B %Y'))
    print('30 дней назад', dt_30_days_ago.strftime('%A %d %B %Y'))


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    dt_from_str = strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
    return strftime('%A %d %B %Y %H:%M:%S', dt_from_str)

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
