'''
Задача 1
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку. .
'''
from sys import argv

def calend(date: str):
    day, month, year = map(int, date.split('.'))
    print (day, month, year)
    if 1 <= year <= 9999:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            return True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            return True
        elif 1 <= day <= 28 + is_leap_year(year):
            return True
        else:
            return False
    return False


def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def calend_tetminal():
    date = argv[1]
    print(calend(date))