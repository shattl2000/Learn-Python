# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
for i in names:
  print(i)


# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём.

names = ['Оля', 'Петя', 'Вася', 'Маша']
for i in names:
  print(i, len(i))


# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']

for i in names:
  if is_male.get(i):
    print(i,'Man')
  else:
    print(i,'Woman')


# Даны группы учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# В группе 2 ученика.
# В группе 3 ученика.

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]

print('Всего', len(groups), 'группы')
for i in groups:
  print('В группе', len(i), 'ученика')


# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят.
# Пример:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]

for i in groups:
  num_group = groups.index(i)+1
  print("Группа", str(num_group) + ':', ', '.join(i))

    





