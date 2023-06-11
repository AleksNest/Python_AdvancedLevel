class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_info(self) -> str:
        return (f'{"Class:":8}{type(self).__name__}'
                f'\n{"Name:":8}{self.name}'
                f'\n{"Age:":8}{self.age} years')


class Mammal(Animal):

    def __init__(self, name: str, age: int, hair: str, voice: str, color: str):
        super().__init__(name, age)
        self.hair = hair
        self.voice = voice



    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Hair:":8}{self.hair}'
                f'\n{"Voice:":8}{self.voice}\n'
                )


class Bird(Animal):

    def __init__(self, name: str, age: int, color: str, voice: str):
        super().__init__(name, age)
        self.color = color
        self.voice = voice



    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Color:":8}{self.color}'
                f'\n{"Voice:":8}{self.voice}\n'
                )


class Fish(Animal):

    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)
        self.color = color

    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Color:":8}{self.color}\n'
                )


# if __name__ == '__main__':
#     bird = Bird('ворон', 2, "серая", "kar-kar")
#
#     print(f' {bird.name = }, {bird.age = }, {bird.voice = }, {bird.color = }, {bird.get_info()}')