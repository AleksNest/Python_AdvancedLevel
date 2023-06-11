'''
Задание №6
Проверить, что выкидываются правильные исключения (файл Exceptions.py) для кода Semin_13Task5
Напишите 3-7 тестов pytest для данного проекта.
Используйте фикстуры (предварительные конкретные данные для теста).
'''

import pytest                      # необходимо установить в окружение


from Seminar_14.Semin13_Task5 import UserWorkshop, User
from Seminar_14.Exceptions import AccesErorr, LevelError
from Seminar_14.Semin13_User import User
@pytest.fixture()
def set_up():
    return UserWorkshop()   # данные для теста


def test_access_fail_1(set_up):                               # тест на проверку того, что  будет выброс исключения AccesErorr при вводе невалидных данных, AccesErorr  прописан в Exceptions.py

    with pytest.raises(AccesErorr, match='Access denied'):
        set_up.login('Nesterovs', '1')                      # передаются невалидные данные


def test_access(set_up):                                    # тест на проверку валидных данных, то что должна вернуться
    assert set_up.login('Nesterov', '1') == '5'             # вводятся валидные двнные и проверяем на совпадение с результатом


def test_access_fail_2(set_up):                                    # тест на проверку того, что  будет выброс исключения AccesErorr при вводе невалидных данных, AccesErorr  прописан в Exceptions.py
    with pytest.raises(LevelError):
        set_up.login('Nesterov', '1')
        set_up.create_user('New_user', '1', '3')



if __name__ == '__main__':
    pytest.main(['-v'])