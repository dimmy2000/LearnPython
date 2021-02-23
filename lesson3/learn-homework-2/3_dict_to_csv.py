"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    list_of_dicts = [
        {'name': 'John', 'age': 23, 'job': 'tough guy'},
        {'name': 'Mary', 'age': 41, 'job': 'strong woman'},
        {'name': 'Isaac', 'age': 66, 'job': 'retired jew'},
        {'name': 'Bert', 'age': 14, 'job': 'schoolkid'},
        {'name': 'Olorin', 'age': 11000, 'job': 'Istar'},
    ]

    with open('list.csv', 'w', encoding='utf-8', newline='') as csv_file:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(csv_file, fields, delimiter=';')
        writer.writeheader()
        for person in list_of_dicts:
            writer.writerow(person)

if __name__ == "__main__":
    main()
