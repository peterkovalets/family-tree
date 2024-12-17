"""Модуль с новыми исключениями"""


class InvalidAgeError(Exception):
    """Исключение на случай, если дата смерти раньше даты рождения"""
    pass


class InvalidTreeDepth(Exception):
    """Исключение на случай, если глубина дерева не положительная"""
    pass
