from typing import List
from typing import Type

from engine.ecs.component import Component


class Matchable:
    def __init__(self, key: List[Type[Component]]):
        self.key = key

    @property
    def key(self) -> List[Type[Component]]:
        return self._key

    @key.setter
    def key(self, value: List[Type[Component]]):
        self._key = value

    def __eq__(self, other):
        for component in other.key:
            if component not in self.key:
                return False
        return True

    def __ne__(self, other):
        for component in other.key:
            if component in self.key:
                return False
        return True
