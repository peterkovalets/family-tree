"""Основной модуль программы"""
from family_tree import Person
import main_menu


def main() -> None:
    """Точка входа программы"""
    people: list[Person] = []
    is_running = True

    while is_running:
        is_running = main_menu.start_menu(people)


if __name__ == '__main__':
    main()
