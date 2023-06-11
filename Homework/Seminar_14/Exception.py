class ValFormatError(Exception):
    def __str__(self):
        return f"Error: Невозможно сравнить. Матрицы разных размеров"