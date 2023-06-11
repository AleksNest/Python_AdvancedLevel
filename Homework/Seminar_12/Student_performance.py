import csv
from functools import reduce
from pathlib import Path


class Validate:
    "Дескриптор на проверку в ФИО наличия первой заглавной буквы, а также что ФИО состоит только из букв"

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not value.isalpha():
            raise TypeError(f'Значение {value} должно содержать только буквы')
        if not value.istitle():
            raise TypeError(f'Значение {value} должно начинаться с заглавной буквы')


class Student:
    name = Validate()
    second_name = Validate()
    surname = Validate()
    _lessons = None

    def __init__(self, name: str, second_name: str, surname: str, lessons_file: Path):
        self.name = name
        self.second_name = second_name
        self.surname = surname
        self.lessons = lessons_file

    @property
    def lessons(self):
        return self._lessons

    @lessons.setter
    def lessons(self, lessons_file: Path):
        " Декоратор считывает с файла список предметов в словарь lessons"

        self._lessons = {"lessons": {}}
        with open(lessons_file, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                self._lessons["lessons"][row[0]] = {"assessments": [], "test_results": [], "average_test": None}
        self._lessons["middle_assessment"] = None
        self._lessons["middle_test"] = None

    def __call__(self, lesson: str, number: int, type_est: str = "lesson"):
        "Метод для сохранения новой оценки по предмету/тесту"

        if lesson not in self.lessons["lessons"].keys():
            raise AttributeError("Нет такого предмета")
        if type_est == "lesson":
            if number < 2 or number > 5:
                raise ValueError("Оценка должна быть от 2 до 5")
            self.lessons["lessons"][lesson]["assessments"].append(number)
            self.lessons["middle_assessment"] = self.calculate_middle_estimate(self.lessons)
        elif type_est == "test":
            if number < 0 or number > 100:
                raise ValueError("Оценка должна быть от 0 до 100")
            self.lessons["lessons"][lesson]["test_results"].append(number)

            # средний бал по тестам по каждому предмету:
            self.lessons["lessons"][lesson]["average_test"] = reduce(lambda x, y: x + y, self.lessons["lessons"][lesson]["test_results"]) / len(self.lessons["lessons"][lesson]["test_results"])
            self.lessons['middle_test'] = self.calculate_middle_test(self.lessons)

    @staticmethod
    def calculate_middle_estimate(lessons: dict) -> float:
        "Подсчет средней оценки по всем предметам"

        all_estimates = []
        [all_estimates.extend(lessons["lessons"][name]["assessments"]) for name in lessons["lessons"]]

        return reduce(lambda x, y: x + y, all_estimates) / len(all_estimates)

    @staticmethod
    def calculate_middle_test(lessons: dict) -> float:
        "Подсчет среднего бала по тестам по всем предметам"

        all_estimates = []
        [all_estimates.extend(lessons["lessons"][name]["test_results"]) for name in lessons["lessons"]]

        return reduce(lambda x, y: x + y, all_estimates) / len(all_estimates)

    def __repr__(self):
        result = f'ФИО студента = {self.name} {self.second_name} {self.surname}\nСредняя оценка по всем предметам = {self.lessons["middle_assessment"]}\nСредний бал по всем тестам = {self.lessons["middle_test"]}\n'
        result += "\nОценки по предметам:\n"

        for key, value in self.lessons["lessons"].items():
            result += f'{key} = {value["assessments"]}\n'
        result += "\nТесты по предметам:\n"
        for key, value in self.lessons["lessons"].items():
            result += f'{key} = {value["test_results"]}, ср.бал = {value["average_test"]}\n'

        return result


if __name__ == '__main__':
    student_1 = Student("Alexey", "Alexeevich", "Nesterov", Path('lessons.csv'))
    student_1("русский язык", 3)
    student_1("русский язык", 5)
    student_1("физика", 5)
    student_1("математика", 5)
    student_1("информатика", 35, "test")
    student_1("математика", 99, "test")
    student_1("химия", 50, "test")
    student_1("химия", 4)
    student_1("информатика", 4)
    student_1("информатика", 40, "test")
    print(student_1)

    student_2 = Student("Ivan", "Ivanjvich", "Ivanov", Path('lessons.csv'))
    student_2("русский язык", 4)
    student_2("история", 5)
    student_2("физика", 3)
    student_2("математика", 5)
    student_2("история", 40, "test")
    student_2("история", 98, "test")
    student_2("химия", 4)
    student_2("информатика", 3)
    student_2("информатика", 55, "test")
    student_2("история", 55, "test")
    print(student_2)