'''
Задание №2
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списковархивов
list-архивы также являются свойствами экземпляра

Добавьте  строки документации для классов.

'''

class Archive:
    """
    Архив, который хранит пару свойств. При нового экземпляра класса, старые данные из ранее
    созданных экземпляров сохраняются в пару списковархивов  list-архивы также являются свойствами экземпляра
    добавить repr
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        СИНГЛТОН ПАТТЕРН
        :param args:
        :param kwargs:
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.numbers_archive = []
            cls.some_strs_archive = []
        else:
            cls._instance.numbers_archive.append(cls._instance.number)
            cls._instance.some_strs_archive.append(cls._instance.some_str)
        return cls._instance

    def __init__(self, number, some_str):
        """
        init
        :param number:
        :param some_str:
        """
        self.number = number
        self.some_str = some_str

    def __str__(self):
        """
        Human-readable representation
        :return:
        """
        return f'Number: {self.number}, string: {self.some_str}, archive: {list(zip(self.numbers_archive,self.some_strs_archive))} '

    def __repr__(self):
        return f'Archive({self.number},{self.some_str})'


if __name__ == '__main__':
    arc1 = Archive(1, "str1")
    print(arc1)
    # print(arc1.number, arc1.numbers_archive, Archive.numbers_archive)
    arc2 = Archive(2, "str2")
    print(arc2)
    # print(arc2.number, arc2.numbers_archive, Archive.numbers_archive)
    arc3 = Archive(3, "str3")
    print(arc3)
    # print(arc3.number, arc3.numbers_archive, Archive.numbers_archive)

    print(Archive.__doc__)
    print(Archive.__new__.__doc__)
    # print(help(Archive))

    print(arc1.__repr__())
    print(arc2.__repr__())
    print(arc3.__repr__())