"""Модуль с переиспользуемыми функциями вывода на экран"""
from typing import Optional

from family_tree import Person


def display_menu(options: tuple[str, ...],
                 header: Optional[str] = None) -> None:
    """Выводит опции меню на экран"""
    header_to_display = f'*--------------- {header} ---------------*'

    if header:
        print(header_to_display)
    for num, option in enumerate(options, start=1):
        print(f'{num}) {option}')
    if header:
        print('*' + '-' * (len(header_to_display) - 2) + '*')


def display_people(people: list[Person]) -> None:
    """Выводит список людей на экран, если они существуют"""
    if not people:
        return print('Не найдено ни одного человека!')

    print('Доступные люди:')
    for num, person in enumerate(people, start=1):
        print(f'{num}) {person}{"" if person.is_alive else " (умер)"}')
