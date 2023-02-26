import math

from src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
        self.name = "Circle"

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius
