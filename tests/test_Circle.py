import pytest
import math
from src.Circle import Circle


def test_circle_init():
    c = Circle(2)
    assert c.radius == 2
    assert c.name == "Circle"


def test_circle_area():
    c = Circle(2)
    assert c.area == math.pi * 2 * 2


def test_circle_perimeter():
    c = Circle(2)
    assert c.perimeter == 2 * math.pi * 2


def test_circle_add_area_with_non_figure_raises_value_error():
    c = Circle(2)
    with pytest.raises(ValueError):
        c.add_area("not a figure")


def test_circle_add_area_returns_sum_of_areas():
    c1 = Circle(2)
    c2 = Circle(4)
    assert c1.add_area(c2) == (math.pi * 2 * 2) + (math.pi * 4 * 4)
