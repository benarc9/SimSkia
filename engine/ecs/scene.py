from abc import ABC
from typing import List
from typing import Type

from engine.ecs.system import System
from engine.ecs.entity import Entity


class Scene(ABC):
    def __init__(self, system_types: List[Type[System]], entity_types: List[Type[Entity]]):
        self._system_types = system_types
        self.entity_types = entity_types

    @property
    def system_types(self) -> List[Type[System]]:
        return self._system_types

    @system_types.setter
    def system_types(self, value: List[Type[System]]):
        self._system_types = value

    @property
    def entity_types(self) -> List[Type[Entity]]:
        return self._entity_types

    @entity_types.setter
    def entity_types(self, value: List[Type[Entity]]):
        self._entity_types = value
