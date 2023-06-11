'''
Задание №5
Доработаем задачи 3 и 4. Создайте класс проекта, который
имеет следующие методы:
загрузка данных (функция из задания 4)
вход в систему - требует указать имя и id пользователя. Для
проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из
множества пользователей.
добавление пользователя. Если уровень пользователя
меньше, чем ваш уровень, вызывайте исключение уровня
доступа.
'''
import json
from Seminar_13.Task4 import  User

from Seminar_13.Task3 import AccesErorr, LevelError

class UserWorkshop:
    user_list = set()

    def __init__(self):
        UserWorkshop.load_users()
        pass


    @staticmethod
    def load_users(path: str = 'users2.json'):
        with open(path, 'r', encoding='UTF-8') as f:
            user_dict = json.load(f)
        for level, user_list in user_dict.items():
            for id, name in user_list.items():
                UserWorkshop.user_list.add(User(name, str(id), str(level)))  # создали объекты User и записали во множество


    def login(self, name: str, id: str) -> str:                 #авторизация пользователя, если есть такой то возвращает уровень пользователя
        login_user = User(name, id)
        for user in UserWorkshop.user_list:
            if login_user == user:                  # проверка осуществляется благодаря __eq__ и __hash__ в классе User (равны когда имя и id равны)
                return user.level
        else:
            raise AccesErorr(name)                  # возбуждение  ошибки прописанной в модуле task3.py

    def create_user(self, name: str, id: str, level: str):                      # создает пользоваетля если уровень меньше чем ваш уровень
        cur_name, cur_id = input("Введите имя авторизированного пользователя и его id через пробел").split()        #авторизация пользователя (который есть в базе)
        if current_level := self.login(cur_name, cur_id):                        # если есть пользователь и уровень у него не 0
            if int(current_level) > int(level):
                return User(name, id, level)                            # создаем новго пользователя, если уровень авторизированного пользователя выше уровня создаваемого пользов
            else:
                raise LevelError(current_level, level)


b = UserWorkshop()
print(b.login('Nesterov', '1')) #(имя, id)  уровень = 5
print(b.create_user('New_user', '1', '3'))  #создаст нового пользователя (имя, id, уровень) в случае если его уровень меньше, чем уровень указанного авторизированного пользователя