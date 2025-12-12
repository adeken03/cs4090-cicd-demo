import math
import sys
from pathlib import Path

import pytest

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from cs4090_cicd_demo.app import (
    add,
    divide,
    multiply,
    sub,
    log,
    square,
    sin,
    cos,
    sqrt,
    percentage,
)


def test_add_basic():
    assert add(5, 6) == 11
    assert add(-2, 2) == 0
    assert add(1.5, 2.5) == 4.0


def test_sub_basic():
    assert sub(10, 3) == 7
    assert sub(-1, -1) == 0


def test_multiply_basic():
    assert multiply(3, 4) == 12
    assert multiply(7, 0) == 0


def test_divide_basic():
    assert divide(6, 3) == 2
    assert divide(-9, 3) == -3
    assert divide(1, 4) == 0.25


def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_log_default_base10():
    assert log(100) == pytest.approx(2.0)


def test_log_custom_base():
    assert log(8, 2) == pytest.approx(3.0)


def test_log_non_positive_raises():
    with pytest.raises(ValueError):
        log(0)
    with pytest.raises(ValueError):
        log(-5)


def test_log_invalid_base_raises():
    with pytest.raises(ValueError):
        log(10, 1)
    with pytest.raises(ValueError):
        log(10, 0)


def test_square():
    assert square(5) == 25
    assert square(-3) == 9


def test_sin_cos():
    assert sin(0) == pytest.approx(0.0)
    assert cos(0) == pytest.approx(1.0)
    assert sin(math.pi / 2) == pytest.approx(1.0)
    assert cos(math.pi) == pytest.approx(-1.0)


def test_sqrt():
    assert sqrt(9) == pytest.approx(3.0)
    assert sqrt(0) == pytest.approx(0.0)


def test_sqrt_negative_raises():
    with pytest.raises(ValueError):
        sqrt(-1)


def test_percentage():
    assert percentage(200, 10) == pytest.approx(20.0)
    assert percentage(50, 0) == pytest.approx(0.0)
    assert percentage(100, -5) == pytest.approx(-5.0)
