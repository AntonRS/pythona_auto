class Figure:
    def __init__(self, name):
        self.name = name

    @property
    def area(self):
        raise NotImplementedError("Subclass must implement area property.")

    @property
    def perimeter(self):
        raise NotImplementedError("Subclass must implement perimeter property.")

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("Cannot add non-geometric shapes.")
        return self.area + figure.area
