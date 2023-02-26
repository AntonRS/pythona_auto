import pytest
from src.Rectangle import Rectangle


def test_rectangle_init():
    r = Rectangle(2, 3)
    assert r.width == 2
    assert r.height == 3
    assert r.name == "Rectangle"


def test_rectangle_area():
    r = Rectangle(2, 3)
    assert r.area == 6


def test_rectangle_perimeter():
    r = Rectangle(2, 3)
    assert r.perimeter == 10


def test_rectangle_add_area_with_non_figure_raises_value_error():
    r = Rectangle(2, 3)
    with pytest.raises(ValueError):
        r.add_area("not a figure")


def test_rectangle_add_area_returns_sum_of_areas():
    r1 = Rectangle(2, 3)
    r2 = Rectangle(4, 5)
    assert r1.add_area(r2) == 26
