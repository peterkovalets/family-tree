"""Модуль класса CompoundPerson"""
from datetime import date
from typing import Optional

from .person import Person
from .exceptions import InvalidTreeDepth

ERROR_CHILD_EXISTS = '{child} уже добавлен как ребенок {parent}!'
ERROR_PARENT_YOUNGER_THAN_CHILD = '{child} не может быть старше чем {parent}!'
ERROR_CHILD_AFTER_PARENT_DEATH = ('{child} не может быть рожден '
                                  'после смерти {parent}!')
ERROR_SELF_AS_CHILD = '{person} не может быть ребенком самого себя!'
ERROR_CHILD_NOT_FOUND = '{child} не является ребенком {parent}!'
ERROR_INVALID_TREE_DEPTH = 'Глубина дерева должна быть положительной!'


class CompoundPerson(Person):
    """Класс, наследуемый от человека, позволяющий строить семейное дерево"""

    def __init__(self, name: str, born: date,
                 died: Optional[date] = None) -> None:
        """Создает объект класса"""
        super().__init__(name, born, died)
        self._children: list['CompoundPerson'] = []

    def add_child(self, child: 'CompoundPerson') -> None:
        """Позволяет добавить человеку ребенка"""
        if child in self._children:
            raise ValueError(ERROR_CHILD_EXISTS.format(child=child.name,
                                                       parent=self.name))
        elif child == self:
            raise ValueError(ERROR_SELF_AS_CHILD.format(person=self.name))
        elif child._born <= self._born:
            raise ValueError(ERROR_PARENT_YOUNGER_THAN_CHILD.format(
                child=child.name,
                parent=self.name
            ))
        elif (not self.is_alive) and (child._born > self._died):
            raise ValueError(ERROR_CHILD_AFTER_PARENT_DEATH.format(
                child=child.name,
                parent=self.name
            ))

        self._children.append(child)

    def remove_child(self, child: 'CompoundPerson') -> None:
        """Позволяет удалить ребенка у человека"""
        if child not in self._children:
            raise ValueError(ERROR_CHILD_NOT_FOUND.format(child=child.name,
                                                          parent=self.name))

        self._children.remove(child)

    def display_children_tree(self, depth: int = 1,
                              child_prefix: str = '\t') -> None:
        """Отображает семейное дерево без учета самого человека"""
        if depth < 1:
            raise InvalidTreeDepth(ERROR_INVALID_TREE_DEPTH)

        for child in self._children:
            print(child_prefix, child)
            if depth > 1:
                child.display_children_tree(depth - 1,
                                            child_prefix + child_prefix)

    def display_family_tree(self, depth: int = 1,
                            child_prefix: str = '\t') -> None:
        """Отображает семейное дерево с заданной глубиной"""
        print(self)
        self.display_children_tree(depth, child_prefix)
