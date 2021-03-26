from typing import List
from typing import Type

from engine.ecs.component import Component
from engine.lib.matchable import Matchable


class ComponentKey:
    def __init__(self, keys: List[Type[Component]]):
        self.key = keys

    def get_keys(self) -> List[Type[Component]]:
        return self.key

    def __str__(self):
        return str(self.key)

    def __eq__(self, other):
        for component in self.key:
            if component not in other.key:
                return False
        return True

    def __ne__(self, other):
        for component in other.key:
            if component in self.key:
                return False
        return True

    @property
    def key(self) -> List[Type[Component]]:
        return self._key

    @key.setter
    def key(self, value: List[Type[Component]]):
        self._key = value
