"""Модуль с основным меню"""
from typing import Optional

from family_tree import Person
from family_tree.exceptions import InvalidAgeError, InvalidTreeDepth
from output_tools import display_menu, display_people
from person_menu import start_menu as start_person_menu
from utils import required_input, require_date, wait_for_input
from constants import (
    MAIN_MENU_OPTIONS,
    REQUIRE_PERSON_PROMPT,
    REQUIRE_ACTION_PROMPT
)


def display_person_tree(people: list[Person]) -> None:
    """Запрашивает у пользователя данные о человеке и выводит
    его семейное дерево на экран"""
    display_people(people)

    if not people:
        return None

    person_idx = required_input(REQUIRE_PERSON_PROMPT,
                                int, value_range=(0, len(people))) - 1
    if person_idx == -1:
        return None

    person: Person = people[person_idx]
    depth = required_input('Введите глубину дерева: ', int)

    try:
        person.display_family_tree(depth)
    except InvalidTreeDepth as e:
        print(e)


def create_person() -> Optional[Person]:
    """Запрашивает у пользователя данные о новом человеке
    и возвращает созданный объект"""
    name = required_input('Введите имя: ')
    born_date = require_date('рождения')

    is_alive = required_input('Жив ли сейчас человек (y/N): ',
                              allowed_values=('y', 'n'),
                              value_modifier=lambda s: s.lower())
    if is_alive == 'n':
        died_date = require_date('смерти')
        try:
            new_person = Person(name, born_date, died_date)
        except InvalidAgeError as e:
            return print(e)
        else:
            return new_person

    return Person(name, born_date)


def start_menu(people: list[Person]) -> bool:
    """Запускает основное меню программы"""
    menu_actions = (
        lambda: display_people(people),
        lambda: display_person_tree(people),
        lambda: create_person(),
        lambda: start_person_menu(people)
    )
    display_menu(MAIN_MENU_OPTIONS, 'МЕНЮ')
    option_idx = required_input(REQUIRE_ACTION_PROMPT, int,
                                value_range=(1, len(MAIN_MENU_OPTIONS))) - 1

    if option_idx == len(MAIN_MENU_OPTIONS) - 1:
        return False

    action = menu_actions[option_idx]
    result = action()

    if isinstance(result, Person):
        people.append(result)
        print(f'{result.name} успешно добавлен!')

    wait_for_input()
    return True
