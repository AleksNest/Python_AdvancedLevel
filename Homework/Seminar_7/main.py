from files_manager.create_dir import create_dir
from files_manager.gen_files import gen_files
from files_manager.group_file import group_file_in_dir
from files_manager.group_rename import group_rename

if __name__ == '__main__':

    create_dir('new')                               # создание директории с переходом в него(текущий)

    my_dict = {'.txt': 2, '.zip': 1,
               '.rar': 1, '.avi': 2,
               '.mp4': 2, '.pop': 2,
               '.gif': 2, '.mpeg': 2,
               '.jpg': 2}
    gen_files('new', my_dict)                       #создание файлов с расширением и кол, указанном в ловаре с рондомными именами

    group_file_in_dir('new', 'rezult')              #группировака файлов из одного директория в другой по типу расширения (Video, photos....)

    group_rename(4, 'pip', 'zip', [2, 4], "new")    #групповое переименование файлов в текущем каталоге

