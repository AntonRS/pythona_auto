import pytest
from src.Triangle import Triangle


def test_triangle_init_valid_dimensions():
    t = Triangle(3, 4, 5)
    assert t.a == 3
    assert t.b == 4
    assert t.c == 5
    assert t.name == "Triangle"


def test_triangle_init_invalid_dimensions():
    with pytest.raises(ValueError):
        t = Triangle(1, 2, 3)


def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert t.area == 6.0


def test_triangle_perimeter():
    t = Triangle(3, 4, 5)
    assert t.perimeter == 12


def test_triangle_add_area_with_non_figure_raises_value_error():
    t = Triangle(3, 4, 5)
    with pytest.raises(ValueError):
        t.add_area("not a figure")


def test_triangle_add_area_returns_sum_of_areas():
    triangle1 = Triangle(2, 2, 2)
    triangle2 = Triangle(4, 4, 4)
    assert triangle1.add_area(triangle2) == 9
