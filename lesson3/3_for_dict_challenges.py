# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

name_repetition = {} # Повторение имен
for name in students:
    if name['first_name'] in name_repetition:
        name_repetition[name['first_name']] += 1
    else:
        name_repetition[name['first_name']] = 1

for key in name_repetition:
    print(key, name_repetition[key], sep=': ')
print('====================')


# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]

name_repetition = {} # Повторение имен
for name in students:
    if name['first_name'] in name_repetition:
        name_repetition[name['first_name']] += 1
    else:
        name_repetition[name['first_name']] = 1

for key in name_repetition.keys():
    if name_repetition[key] is max(name_repetition.values()):
        print(f'Самое частое имя среди учеников: {key}')
print('====================')

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]

name_repetition = {} # Повторение имен
class_counter = 0 # Номер класса

for some_class in school_students:
    class_counter += 1
    if class_counter not in name_repetition:
        name_repetition[class_counter] = {}
    for name in some_class:
        if name['first_name'] in name_repetition[class_counter]:
            name_repetition[class_counter][name['first_name']] += 1
        else:
            name_repetition[class_counter][name['first_name']] = 1

for some_class in name_repetition.keys():
    for key in name_repetition[some_class]:
        if name_repetition[some_class][key] is max(name_repetition[some_class].values()):
            print(f'Самое частое имя среди учеников в классе {some_class}: {key}')
print('====================')

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

for some_class in school:
    girl_counter = 0
    boy_counter = 0
    for student in some_class['students']:
        if is_male[student['first_name']] == True:
            boy_counter += 1
        else:
            girl_counter += 1
    print('В классе', some_class['class'], girl_counter, 'девочки и', boy_counter, 'мальчика.')
print('====================')

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

class_counter = {}

for some_class in school:
    girl_counter = 0
    boy_counter = 0
    for student in some_class['students']:
        if is_male[student['first_name']] == True:
            boy_counter += 1
        else:
            girl_counter += 1
    class_counter[some_class['class']] = {'girls': girl_counter, 'boys': boy_counter}

# print(max((value['girls']) for value in class_counter.values()))

max_count = 0
for some_class, some_value in class_counter.items():
    if some_value['boys'] > max_count:
        max_count = some_value['boys']
for key in class_counter.keys():
    if class_counter[key]['boys'] == max_count:
        print(f'Больше всего мальчиков в классе {key}')

max_count = 0
for some_class, some_value in class_counter.items():
    if some_value['girls'] > max_count:
        max_count = some_value['girls']
for key in class_counter.keys():
    if class_counter[key]['girls'] == max_count:
        print(f'Больше всего девочек в классе {key}')

print('====================')

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
