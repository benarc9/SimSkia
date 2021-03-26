import uuid
from typing import Dict
from typing import List
from typing import Type

import loguru
from pyeventbus3 import pyeventbus3

from engine.ecs.component import Component
from engine.ecs.component_key import ComponentKey
from engine.ecs.entity import ComponentRemovedEvent, ComponentAddedEvent
from engine.ecs.entity import Entity

from pyeventbus3.pyeventbus3 import PyBus

from engine.lib.event import Event


class EntityAddedEvent(Event):
    def __init__(self, ecs, entity: Entity):
        super(EntityAddedEvent, self).__init__(ecs)
        self.entity = entity

    @property
    def entity(self) -> Entity:
        return self._entity

    @entity.setter
    def entity(self, value: Entity):
        self._entity = value


class EntityRemovedEvent(Event):
    def __init__(self, ecs, entity: Entity):
        super(EntityRemovedEvent, self).__init__(ecs)
        self.entity = entity

    @property
    def entity(self) -> Entity:
        return self._entity

    @entity.setter
    def entity(self, value: Entity):
        self._entity = value


class System:
    def __init__(self, key: List[Type[Component]]):
        super(System, self).__init__()
        self.key = ComponentKey(key)
        self._entities: Dict[uuid.UUID, Entity] = {}
        PyBus.Instance().register(self, self.__class__.__name__)

    def __str__(self):
        return "System[{}]".format(self.__class__.__name__)

    def start(self, ecs=None):
        pass

    def update(self, ecs=None):
        pass

    def check_entity(self, entity: Entity=None) -> bool:
        if entity is not None:
            loguru.logger.info("Checking Component Key Match")
            loguru.logger.info("\tSystem: {}\tEntity: {}".format(self.__class__.__name__, entity.__class__.__name__))
            loguru.logger.info("\tEntity Key: {}".format(entity.key))
            loguru.logger.info("\tSystem Key: {}".format(self.key))
            loguru.logger.info("Matched?: {}".format(self.key == entity.key))
            return self.key == entity.key

    @pyeventbus3.subscribe(onEvent=EntityAddedEvent)
    def on_entity_added_event(self, event: EntityAddedEvent):
        loguru.logger.info("EntityAddedEvent")
        if self.check_entity(event.entity):
            self._entities[event.entity.id] = event.entity
            loguru.logger.info("Entity Added: {}".format(event.entity))
        else:
            loguru.logger.info("Entity Not Added: {}".format(event.entity))

    @pyeventbus3.subscribe(onEvent=EntityRemovedEvent)
    def on_entity_removed_event(self, event: EntityRemovedEvent):
        if event.entity.id in self.entities.keys():
            del self.entities[event.entity.id]
            loguru.logger.info("Entity removed: {}".format(event.entity))
        else:
            loguru.logger.info("Cannot remove entity that does not exist")

    @pyeventbus3.subscribe(onEvent=ComponentAddedEvent)
    def on_component_added_event(self, event: ComponentAddedEvent):
        if event.source.id not in self.entities.keys():
            if self.check_entity(event.source):
                self.entities[event.source.id] = event.source
                loguru.logger.info("System[{}]: Entity Added: {}".format(self.__class__.__name__, event.source.__class__.__name__))

    @pyeventbus3.subscribe(onEvent=ComponentRemovedEvent)
    def on_component_removed_event(self, event: ComponentRemovedEvent):
        if event.source.id in self.entities.keys():
            if not self.check_entity(event.source):
                del self.entities[event.source.id]
                loguru.logger.info("System[{}]: Entity Removed: {}".format(self.__class__.__name__, event.source.__class__.__name__))

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
