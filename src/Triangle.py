from math import sqrt
from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Triangle with the given sides cannot be created.")
        self.a = a
        self.b = b
        self.c = c
        self.name = "Triangle"

    @property
    def area(self):
        return self.perimeter / 2

    @property
    def perimeter(self):
        return self.a + self.b + self.c