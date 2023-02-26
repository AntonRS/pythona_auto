import pytest
from src.Figure import Figure


def test_figure_area_not_implemented():
    f = Figure(name="Template")
    with pytest.raises(NotImplementedError):
        f.area()


def test_figure_perimeter_not_implemented():
    f = Figure(name="Template")
    with pytest.raises(NotImplementedError):
        f.perimeter()


def test_figure_add_area_with_non_figure_raises_value_error():
    f1 = Figure(name="Template")
    with pytest.raises(ValueError):
        f1.add_area("not a figure")
