'''
Задание №2
Погружение в Python | Коллекции
Пользователь вводит данные. Сделайте проверку данных
и преобразуйте если возможно в один из вариантов ниже:
✔ Целое положительное число
✔ Вещественное положительное или отрицательное число
✔ Строку в нижнем регистре, если в строке есть
хотя бы одна заглавная буква
✔ Строку в нижнем регистре в остальных случаях
'''

user = input('введите данные')

if user.isdigit():
    print(int(user))
elif user.find('.') !=-1 and user.replace('.', '').replace('-', '').isdigit():
    print(float(user), 'dddd')
elif any([sym.isupper() for sym in user]):   # any[True, False, False -> True; all[True, True, True -> True;]
    print(user.lower())
else:
    print(user)

