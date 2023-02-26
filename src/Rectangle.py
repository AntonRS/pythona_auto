from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.name = "Rectangle"

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)
