'''Задание №5
✔ Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии.
'''

names = ['Alex', 'Adam', "eva"]
salaries = [15000, 20000, 25000]
awards = ['10.0%', '7.25%', '5%' ]

def calc_bonus(name: list[str], salary: list[int], award: list[str]) -> dict[str, float]:
    result = {}
    for name, salary, award in zip(names, salaries, awards):
        bonus_amount = salary * float(award[:-1]) / 100
        result[name] = bonus_amount
    return result
    #return {name: salary * float(award[:-1]) / 100 for name, salary, award in zip(names, salaries, awards)} #выше код записывается одной строкой

print(calc_bonus(names, salaries, awards))
