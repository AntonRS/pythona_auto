import pytest
from src.Square import Square


def test_square_init():
    s = Square(4)
    assert s.width == 4
    assert s.height == 4
    assert s.name == "Square"


def test_square_area():
    s = Square(4)
    assert s.area == 16


def test_square_perimeter():
    s = Square(4)
    assert s.perimeter == 16


def test_square_add_area_with_non_figure_raises_value_error():
    s = Square(4)
    with pytest.raises(ValueError):
        s.add_area("not a figure")


def test_square_add_area_returns_sum_of_areas():
    s1 = Square(4)
    s2 = Square(5)
    assert s1.add_area(s2)
