'''
функция создания файла с расширением txt с данными:  рандомное слово: рандомное значение
'''
import random
import string

def create_file_txt(filename_txt: str, flag: str):
    with open(filename_txt, flag, encoding='utf-8') as fout:
        lenth = random.randint(4, 7)
        s =""
        for i in range(lenth):
            s += random.choice(string.ascii_lowercase)
        fout.write(f'{s}: {random.randint(1,100)}\n')
    print(f"записано в {filename_txt} ")