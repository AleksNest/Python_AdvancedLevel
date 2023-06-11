'''Задание №7
✔ Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
'''


dict1 = {"company_1":[1, 2, 5, -8, 10, 36],
        "company_2":[-10, 2, -19, 7, -15, 36],
        "company_3":[10, 2, 19, -7, 11, 36]}

def income(input_dict: dict[str, list[int]]) -> bool:
    dict2 = {}
    for value, key in enumerate(input_dict):
        dict2[key] = sum(input_dict[key])

    print(dict2)
    if all(map(lambda x: x > 0, dict2.values())):
        return True
    else:
        return False

print(income(dict1))

# короткий вариант решения
def income1 (input_dict: dict[str, list[int]]) -> bool:
        for key in input_dict:
            if sum(input_dict[key]) <= 0:
                return False

        return True


print(income1(dict1))
