"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    school = [{'school_class': '1a', 'scores': [5, 4, 4, 5, 5]},
              {'school_class': '3a', 'scores': [5, 2, 3, 5, 4]},
              {'school_class': '4a', 'scores': [5, 4, 4, 5, 4]},
              {'school_class': '4b', 'scores': [3, 4, 4, 5, 2]}, ]

    average_score = {}
    school_average_score = 0

    for this_class in school:
        average_score[this_class['school_class']] = \
            sum(this_class['scores']) / len(this_class['scores'])
        school_average_score += sum(this_class['scores']) / \
            len(this_class['scores'])

    print('Средний балл по школе: ', school_average_score)

    for some_class in average_score:
        print(f'Средний балл в {some_class} классе: ',
              average_score[some_class])


if __name__ == "__main__":
    main()
