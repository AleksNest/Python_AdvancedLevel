'''
Создайте класс с базовым исключением и дочерние классыисключения:
○ ошибка уровня,
○ ошибка доступа.!
'''

class BaseExeption(Exception):
    pass

class LevelError(BaseExeption):
    def __init__(self):
        self.value = value
        self.value_min = value_min

    def __str__(self):
        return f"Ошибка уровня - {self.value} > минимального уровня {self.value_min}"

# class AccesErorr(BaseExeption):
#     def __init__(self, value):
#         self.value = value
#     def __str__(self):
#         return f"Ошибка доступа - {self.value}"

class AccesErorr(BaseExeption):

    def __str__(self):
        return f"Ошибка доступа "




def fun(num):
    if num < 2:
        raise AccesErorr
    elif num > 5:
        raise LevelError
    else:
        print('все ок')


if __name__ == '__main__':
    raise LevelError(4)
    fun(1)