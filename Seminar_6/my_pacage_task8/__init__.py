'''
Задача 8
Создайте пакет с всеми модулями, которые вы создали за время занятия.
Добавьте в __init__ пакета имена модулей внутри дандер __all__.
В модулях создайте дандер __all__ и укажите только те функции, которые могут верно работать за пределами модуля.
'''

from Seminar_6.my_pacage_task8.module_task2_task3 import func
from Seminar_6.my_pacage_task8.module_task4_task5_task6 import show_rezult, puzzle_solver, puzzle_solut
from Seminar_6.my_pacage_task8.module_task7 import calend, is_leap_year

__all__ = ["func", "show_rezult", "puzzle_solver", "puzzle_solut", "calend", "is_leap_year"]