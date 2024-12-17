"""Модуль с утилитами"""
from datetime import datetime, date
from calendar import monthrange
from typing import Any

from constants import START_YEAR


def wait_for_input() -> None:
    """Создаёт задержку, чтобы пользователь успел прочитать текст выше"""
    input('Нажмите Enter чтобы продолжить...')


def required_input(prompt: str = '', var_type: type = str, **kwargs) -> Any:
    """Обязательный для ввода input с расширенными опциями"""
    value_range = kwargs.get('value_range')
    allowed_values = kwargs.get('allowed_values')
    value_modifier = kwargs.get('value_modifier')

    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print('Ошибка! Ввод не может быть пустым.')
            continue

        try:
            value = var_type(user_input)
            if value_modifier:
                value = value_modifier(value)
            if (value_range and
                    not value_range[0] <= value <= value_range[1]):
                print(f'Ошибка! Введите значение в диапазоне от'
                      f' {value_range[0]} до '
                      f'{value_range[1]}.')
                continue
            if allowed_values and value not in allowed_values:
                print('Ошибка! Введите допустимое значение.')
                continue

            return value
        except ValueError:
            print(f'Ошибка! Ожидался тип {var_type.__name__}.')


def require_date(event_name: str) -> date:
    """Запрашивает у пользователя данные о дате с клавиатуры, создает
    объект даты и возвращает его"""
    current_year = datetime.today().year
    year = required_input(f'Введите год {event_name}: ', int,
                          value_range=(START_YEAR, current_year))
    month = required_input(f'Введите номер месяца {event_name}: ', int,
                           value_range=(1, 12))
    days_in_month = monthrange(year, month)[1]
    day = required_input(f'Введите номер дня {event_name}: ', int,
                         value_range=(1, days_in_month))

    return date(year, month, day)
