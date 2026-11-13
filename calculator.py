"""Простейшие операции учебного калькулятора."""


def add(first: float, second: float) -> float:
    """Возвращает сумму двух чисел."""
    return first + second


def subtract(first: float, second: float) -> float:
    """Возвращает разность двух чисел."""
    return first - second


def multiply(first: float, second: float) -> float:
    """Возвращает произведение двух чисел."""
    return first * second


def power(first: float, second: float) -> float:
    """Возвращает число, возведённое в степень."""
    return first ** second


def divide(first: float, second: float) -> float:
    """Возвращает частное двух чисел."""
    if second == 0:
        raise ValueError("На ноль делить нельзя")
    return first / second
