'''
Задание №3
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
'''
'''
Задание №4
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь

'''

from random import randint
class Person:


    def __init__(self, last_name, first_name, age):
        self._last_name, self._first_name, self.__age = \
            last_name, first_name, age

    def get_birthday(self):
        return self.__age

    def add_birthday(self):
        self.__age += 1

    def get_fullname(self):
        return f'{self._last_name}, {self._first_name}'

class Employee(Person):

    def __init__(self, *args):
        super().__init__(*args)
        self.__id = randint(10 ** 5, 10 ** 6)
        self.__level = sum(int(i) for i in str(self.__id)) % 7

    def get_id(self):
        return self.__id

    def get_level(self):
        return self.__level

if __name__ == "__main__":
#для задачи 3
    person = Person('Иванов', 'Иван', 35)
    print(person.get_birthday())
    person.add_birthday()

    print(person.get_fullname())
    print(person._last_name)
    print(person.get_birthday())

#для задачи 4
    employee = Employee('Иванов', 'Иван', 45)
    print(employee.get_birthday())
    employee.add_birthday()

    print(employee.get_fullname())
    print(employee._last_name)
    print(employee.get_birthday())
    print(employee.get_id())
    print(employee.get_level())



