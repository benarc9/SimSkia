import uuid
from abc import abstractmethod
from typing import Dict
from typing import List
from typing import Type
from abc import ABC

import loguru

from pyeventbus3 import pyeventbus3

from engine.ecs.component import Component
from engine.ecs.component_key import ComponentKey
from engine.ecs.entity import ComponentRemovedEvent, ComponentAddedEvent
from engine.ecs.entity import Entity

from engine.ecs.events.entity_added_event import EntityAddedEvent
from engine.ecs.events.entity_added_to_system_event import EntityAddedToSystemEvent
from engine.ecs.events.entity_removed_event import EntityRemovedEvent


class System(ABC):
    def __init__(self, key: List[Type[Component]]):
        super(System, self).__init__()
        self.key = ComponentKey(key)
        self.entities = {}

    def __add_entity__(self, entity: Entity):
        self.entities[entity.id] = entity

    def __remove_entity__(self, entity: Entity):
        if entity.id in self.entities.keys():
            del self.entities[entity.id]

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def update(self):
        pass

    def check_entity(self, entity: Entity) -> bool:
        return self.key == entity.key

    @pyeventbus3.subscribe(onEvent=EntityAddedEvent)
    def on_entity_added_event(self, event):
        if self.check_entity(event.entity):
            self.entities[event.entity.id] = event.entity

    @pyeventbus3.subscribe(onEvent=EntityRemovedEvent)
    def on_entity_removed_event(self, event):
        if event.entity.id in self.entities.keys():
            if not self.check_entity(event.entity):
                del self.entities[event.entity.id]

    @pyeventbus3.subscribe(onEvent=ComponentAddedEvent)
    def on_component_added_event(self, event: ComponentAddedEvent):
        if event.source.id not in self.entities.keys():
            if self.check_entity(event.source):
                self.__add_entity__(event.source)

    @pyeventbus3.subscribe(onEvent=ComponentRemovedEvent)
    def on_component_removed_event(self, event: ComponentRemovedEvent):
        if event.source.id in self.entities.keys():
            if not self.check_entity(event.source):
                self.__remove_entity__(event.source)

    @property
    def key(self) -> ComponentKey:
        return self._key

    @key.setter
    def key(self, value: ComponentKey):
        self._key = value

    @property
    def entities(self) -> Dict[uuid.UUID, Entity]:
        return self._entities

    @entities.setter
    def entities(self, value: Dict[uuid.UUID, Entity]):
        self._entities = value
