# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

print('====================')
names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print(name)
print('====================')


# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём.

names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print(name, len(name))
print('====================')


# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print(name, 'пол:', 'мужской' if is_male[name] is True else 'женский' )
print('====================')


# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# В группе 2 ученика.
# В группе 3 ученика.

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
group_counter = 0
member_counter = []

for group in groups:
    group_counter += 1
    member_counter.append(len(group))

print(f'Всего групп: {group_counter}')
for member in member_counter:
    print(f'В группе учеников: {member}')
print('====================')


# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят.
# Пример:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]

for index, group in enumerate(groups, start=1):
    print(f'Группа {index}:', end=' ')
    print(', '.join(group))
print('====================')
