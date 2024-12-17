"""Модуль с меню редактирования человека"""
from typing import Optional

from family_tree import Person
from output_tools import display_menu, display_people
from utils import required_input, require_date
from constants import (
    PERSON_MENU_OPTIONS,
    REQUIRE_PERSON_PROMPT,
    REQUIRE_ACTION_PROMPT
)


def change_name(person: Person) -> None:
    """Запрашивает у пользователя новое имя человека
    с клавиатуры и изменяет его имя"""
    new_name = required_input('Введите новое имя: ')
    person.name = new_name
    print(f'Имя успешно изменено на {person.name}!')


def require_child(people: list[Person]) -> Optional[Person]:
    """Выводит на экран доступных людей и предлагает выбрать
    из них определенного человека"""
    display_people(people)

    if not people:
        return None

    child_idx = required_input(REQUIRE_PERSON_PROMPT, int,
                               value_range=(0, len(people))) - 1
    if child_idx == -1:
        return None

    return people[child_idx]


def add_child_to_person(person: Person, people: list[Person]) -> None:
    """Получает объект ребенка у пользователя с клавиатуры
    и добавляет его в список детей человека, если это возможно"""
    child = require_child(people)

    try:
        person.add_child(child)
    except ValueError as e:
        print(e)
    else:
        print(f'{child.name} теперь ребенок {person.name}!')


def remove_child_from_person(person: Person, people: list[Person]) -> None:
    """Получает объект ребенка у пользователя с клавиатуры
    и удаляет его из списка детей человека, если это возможно"""
    child = require_child(people)

    try:
        person.remove_child(child)
    except ValueError as e:
        print(e)
    else:
        print(f'{child.name} больше не ребенок {person.name}!')


def add_died_date(person: Person) -> None:
    """Запрашивает у пользователя дату смерти человека и добавляет
    ее к нему"""
    died_date = require_date('смерти')

    try:
        person.add_died_date(died_date)
    except ValueError as e:
        print(e)
    else:
        print('Дата смерти успешно добавлена!')


def start_menu(people: list[Person]) -> None:
    """Запускает меню редактирования человека"""
    display_people(people)

    if not people:
        return None

    person_idx = required_input(REQUIRE_PERSON_PROMPT,
                                int, value_range=(0, len(people))) - 1
    if person_idx == -1:
        return

    person = people[person_idx]
    menu_actions = (
        lambda: change_name(person),
        lambda: add_child_to_person(person, people),
        lambda: remove_child_from_person(person, people),
        lambda: add_died_date(person)
    )
    display_menu(PERSON_MENU_OPTIONS, 'РЕДАКТИРОВАНИЕ ЧЕЛОВЕКА')
    option_idx = required_input(REQUIRE_ACTION_PROMPT, int,
                                value_range=(1, len(PERSON_MENU_OPTIONS))) - 1

    if option_idx == len(PERSON_MENU_OPTIONS) - 1:
        return

    action = menu_actions[option_idx]
    action()
