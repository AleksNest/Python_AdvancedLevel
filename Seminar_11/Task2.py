'''
Задание №2
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списковархивов
list-архивы также являются свойствами экземпляра
'''

# вариант 1 решения
class Archive:

    numbers_archive = []
    some_strs_archive = []
    last_number = None
    last_str = None


    def __init__(self, number, some_str):
        self.number = number
        self.some_str = some_str

        if Archive.last_number is not None:
            Archive.numbers_archive.append(Archive.last_number)
            Archive.some_strs_archive.append(Archive.last_str)
        Archive.last_number = number
        Archive.last_str = some_str

    def __str__(self):
        return f'Number: {self.number}, string: {self.some_str}, archive: {list(zip(Archive.numbers_archive,Archive.some_strs_archive))} '


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



