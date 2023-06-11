'''
Задача 2
Создайте в переменной data список значений разных типов перечислив их через
запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
✔ порядковый номер начиная с единицы
✔ значение
✔ адрес в памяти
✔ размер в памяти
✔ хэш объекта
✔ результат проверки на целое число только если он положительный
✔ результат проверки на строку только если он положительный
Добавьте в список повторяющиеся элементы и сравните на результаты.
'''

x = [1, "1", False, 2.5, [1, 5], (1, 2, 3), {}]
print('{:<5}{:<10}{:<16}{:<10}{:<23}{:<10}{:<10}'.format('№', 'значение', 'адрес', 'размер', 'хэш', 'число', 'строка'))

# 1 способ
count = 0
for i in x:
    count += 1
    print('{:<5}{:<10}{:<16}{:<10}{:<23}{:<10}{:<10}'.format(count, str(i), str(id(i)), i.__sizeof__(),
                                                             hash(i) if isinstance(i, (int, str, float)) else "нет хеша",
                                                             True if isinstance(i, int) and i >= 0 else False,
                                                             True if isinstance(i, str) else False))
# 2 способ
for i in range(len(x)):

    print('{:<5}{:<10}{:<16}{:<10}'.format(i+1, str(x[i]), str(id(x[i])), x[i].__sizeof__()), end="")

    if isinstance(x[i], list) or  isinstance(x[i], dict or set or frozenset):
        print('{:<23}'.format("нет хеша"), end="")
    else:
        print('{:<23}'.format(hash(i)), end="")
    if isinstance(x[i], int) and i >=0 :
        print('{:<10}'.format("True"), end="")
    else:
        print('{:<10}'.format("False"), end="")
    if isinstance(x[i], str):
        print('{:<10}'.format("True"))
    else:
        print('{:<10}'.format("False"))

# 3 способ
for i, elem in enumerate(x, 1):
    print(f'{i}, {elem =}, {id(elem)}, {sys.getsizeof(elem)}, {hash(elem)}, {True if isinstance(elem, int) else ""}, '
          f'{True if isinstance(elem, str) else ""}')
