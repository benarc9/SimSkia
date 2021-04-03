from abc import ABC
from abc import abstractmethod
from typing import Dict
from typing import List
from typing import Type

from engine.ecs.system import System
from engine.ecs.entity import Entity

import loguru


class Scene(ABC):
    def __init__(self, system_types: List[Type[System]], entity_types: List[Type[Entity]]):
        self._system_types = system_types
        self.entity_types = entity_types
        self.systems = {}
        self.entities = {}

    def start(self):
        for system_type in self.systems.keys():
            sys = self.systems[system_type]
            sys.start()

    def update(self):
        for system in self.systems.values():
            system.update()

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

    @property
    def systems(self) -> Dict[Type[System], System]:
        return self._systems

    @systems.setter
    def systems(self, value: Dict[Type[System], System]):
        self._systems = value

    @property
    def entities(self) -> Dict[Type[Entity], Entity]:
        return self._entities

    @entities.setter
    def entities(self, value: Dict[Type[Entity], Entity]):
        self._entities = value
