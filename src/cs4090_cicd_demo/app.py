import math
from typing import Union

Number = Union[int, float]


def multiply(a: Number, b: Number) -> Number:
    return a * b


def add(a: Number, b: Number) -> Number:
    return a + b


def divide(a: Number, b: Number) -> float:
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def sub(a: Number, b: Number) -> Number:
    return a - b


def log(x: Number, base: Number = 10) -> float:
    if x <= 0:
        raise ValueError("logarithm undefined for non-positive numbers")
    if base <= 0 or base == 1:
        raise ValueError("base must be positive and not equal to 1")
    return math.log(x, base)


def square(x: Number) -> Number:
    return x ** 2


def sin(x: Number) -> float:
    return math.sin(x)


def cos(x: Number) -> float:
    return math.cos(x)


def sqrt(x: Number) -> float:
    if x < 0:
        raise ValueError("square root undefined for negative numbers")
    return math.sqrt(x)


def percentage(value: Number, percent: Number) -> float:
    return (value * percent) / 100
