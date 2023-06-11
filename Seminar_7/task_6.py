'''
Задание №6
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
'''

from task_5 import gen_files
from pathlib import Path
import os


def create_dir(name_dir: str):
    #name = Path(name_dir)   # new
    #path = name.cwd() / name_dir  # C:\Users\Алексей\Desktop\GreekBrains\СЕМИНАРЫ\Python_advanced\pythonProject\new
    name = Path(Path.cwd() / name_dir) #C:\Users\Алексей\Desktop\GreekBrains\СЕМИНАРЫ\Python_advanced\pythonProject\new
    if not name.exists():       #проверка на наличие директория
        name.mkdir()            #создает директорий с именем name_dir в текущем директории

    os.chdir(name)          #переходим в созданный каталог сделав его текущим


if __name__ == '__main__':
    my_dict = {'.txt': 1, '.doc': 1, '.bin': 1, '.pdf': 1}
    gen_files(my_dict)
    create_dir('new')