'''
Задание №2
Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться.
'''
'''
есть внешний словарь working_dict[access_level] с ключом access_level. Внутри каждого ключа есть  словарь с  ключом  Id, значением имя
'''

import json
import os
from pathlib import Path


def get_ids(filename)-> set:                                                     # возвращает все уникальные id из файла json
    file = open(filename, 'r', encoding='utf-8')
    all_ids = set()
    try:                                                                    # если файл пустой - возникает ошибка и тогда пропускает этот блок и выполняется следом exept
        data = json.load(file)                                                  # записываем в data=словарь из json файла
        for level in data:
            for uid in level:
                all_ids.add(uid)                                            # получаем все id из json файла для того чтобы потом их не использовать, так как они уже заняты
    except:
        pass
    file.close()
    return all_ids


def get_data(all_ids:set, filename):                                            #добавление данных в словарь
    working_dict = {}                                                           #working_dict: dict[int: dict[int, str]]= {}    словарь верхнего уровня ключ access level
    while True:
        name = input("введите имя: ")
        if name == "":
            break                                                               #выход из цикла
        user_id = -1
        while user_id < 0 or user_id in all_ids:
            user_id = int(input("ввеедите id "))
        all_ids.add(user_id)                                                    # добавляем во множестово id чтобы потом исключить их в использовании

        access_level = 0
        while not 1 <= access_level <= 7:
            access_level = int(input('введите уровень доступа (1-7) '))
        if working_dict.get(access_level):                                      # если есть значение во внешнем словаре по данному ключу access_level
            working_dict.get(access_level).update({user_id: name})              # добавляем еще значение внешнего словаря(ключ = id значение = name)
        else:
            working_dict[access_level] = {user_id: name}
        fun_dump_json(working_dict, filename)                                       # добавляем обновленный словарь в файл
        if input("продолжить ввод? y/n") != 'y':
            break


def fun_dump_json(working_dict, filename):                                          #функция записи словаря в json файл
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(working_dict, f)

def func(json_file: str):
    if not os.path.isfile(Path.cwd() / json_file):
        with open(json_file, 'w', encoding='utf-8') as f:
            f.write('')
        print(f'создан новый файл файл {json_file}')

    all_ids = get_ids(json_file)                                                   #записываем во множество все id, которые в json файле
    get_data(all_ids, json_file)                                                     #заполняем словарь в словаре для json файла


