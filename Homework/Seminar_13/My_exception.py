class ValError(Exception):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def __str__(self):
        if self.a <= 0 and self.b <= 0:
            return f"Ошибка ввода: обе стороны имеют невалидные значения = {self.a}; {self.b}"
        else:
            if self.a <= 0:
                return f"Ошибка ввода: сторона имеет невалидное  значение = {self.a} "
            else:
                return f"Ошибка ввода: сторона имеет невалидное  значение  = {self.b}"


class ValFormatError(Exception):
    def __init__(self, operation: str):
        self.operation = operation

    def __str__(self):
        if self.operation == '+':
            return f"Error: Невозможно сложить матрицы, матрицы разных размеров"
        elif self.operation == '*':
            return f"Error: Невозможно перемножить матрицы: не подходят размерности"
        else:
            return f"Error: Невозможно сравнить. Матрицы разных размеров"


class ValueBankError(Exception):
    def __init__(self, cash):
        self.cash = cash

    def __str__(self):
        return f"Ошибка ввода. Число {self.cash} < 0 "