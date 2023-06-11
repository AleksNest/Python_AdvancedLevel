'''
Задание №8
Погружение в Python | Коллекции
✔ Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей.
'''


diction = {"friend1": ('фонарик', 'тушенка', 'удочка', 'спальник', 'лопата', 'отвертка', 'топор'),
            "friend2": ('котелок', 'пила', 'удочка', 'спальник', 'лопата', 'фонарик'),
            "friend3": ('фонарик', 'палатка', 'удочка', 'спальник', 'лопата')
           }

set1 = set()
for k in diction:
    if not set1:
        set1 = set(diction[k])
    else:
        set1 &= set(diction[k])
print("какие вещи взяли все три друга:", set1)

my_tuple = diction.keys()

my_set = set()
for friend in my_tuple:
    my_set = set(diction[friend])

    for other_friends in [i for i in my_tuple if i != friend]:
        my_set = my_set - set(diction[other_friends])
    if my_set:
        print("Какие вещи есть у всех друзей кроме одного:", my_set)

for friend in my_tuple:
    to_remove = set(diction[friend])
    my_set = set()
    for other_friends in [i for i in my_tuple if i != friend]:
        if not my_set:
            my_set = set(diction[other_friends])
        else:
           my_set = my_set & set(diction[other_friends])

    my_set -= to_remove

    if my_set:
        print(f'{friend} не взял \'t {my_set}')
