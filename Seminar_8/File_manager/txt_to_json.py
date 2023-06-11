'''
Задание 1
создание из файла txt нового файла json
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
'''

import json

def txt_to_json(txt_file: str, json_file: str):
    with (open (txt_file, 'r', encoding='utf-8') as fin,      #открываем  файл data.txt считываем в словарь my_dict
        open(json_file, "w", encoding='utf-8') as fout):      # создаем  data.json
        contents = fin.readlines()
        my_dict = {}
        for line in contents:                                   # данные из data.txt считываем в словарь my_dict
            key, val = line.split(": ")
            my_dict[key.title()] = int(val)

        json.dump(my_dict, fout, separators=(',\n', ':'))        #запись в  data.json словаря my_dict


