"""Модуль класса Person"""
from datetime import date
from typing import Optional

from .exceptions import InvalidAgeError

ERROR_DEATH_BEFORE_BIRTH = 'Дата смерти не может быть раньше даты рождения!'
ERROR_ALREADY_DEAD = '{person} уже мертв!'


class Person:
    """Класс человека"""

    def __init__(self, name: str, born: date,
                 died: Optional[date] = None) -> None:
        """Создает объект класса"""
        if died and died < born:
            raise InvalidAgeError(ERROR_DEATH_BEFORE_BIRTH)

        self.name = name
        self._born = born
        self._died = died

    def __str__(self) -> str:
        """Строковая репрезентация объекта класса"""
        return f'{self.name} — {self.age} лет'

    @property
    def age(self) -> int:
        """Возраст"""
        now = date.today()
        delta = now.year - self._born.year

        if (now.month, now.day) < (self._born.month, self._born.day):
            delta -= 1

        return delta

    @property
    def is_alive(self) -> bool:
        """Булево значение обозначающее жив ли человек"""
        return self._died is None

    def add_died_date(self, date: date) -> None:
        """Позволяет добавить человеку дату смерти"""
        if date < self._born:
            raise InvalidAgeError(ERROR_DEATH_BEFORE_BIRTH)
        elif not self.is_alive:
            raise ValueError(ERROR_ALREADY_DEAD.format(person=self.name))

        self._died = date
