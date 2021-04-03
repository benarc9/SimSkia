import uuid
from typing import Dict
from typing import List
from typing import Type

from engine.ecs.component import Component
from engine.ecs.component_key import ComponentKey
from engine.ecs.components.transform import Transform

import loguru

from pyeventbus3.pyeventbus3 import PyBus

from engine.ecs.events.component_added_event import ComponentAddedEvent
from engine.ecs.events.component_removed_event import ComponentRemovedEvent


class Entity:
    def __init__(self, components: List[Type[Component]]):
        super(Entity, self).__init__()
        loguru.logger.info("Entity created [{}]".format(self.__class__.__name__))
        components.append(Transform)
        self.key = ComponentKey(components)
        self.components = {}
        self.id = uuid.uuid4()

        for component in components:
            self.components[component] = component()

    def __str__(self):
        return "Entity: [{}]".format(self.__class__.__name__)

    def get_component(self, comp_type: Type[Component]):
        return self.components[comp_type]

    def add_component(self, comp_type: Type[Component]):
        if comp_type not in self.components.keys():
            keys = self.key.get_keys()
            keys.append(comp_type)
            self.key = ComponentKey(keys)
            self.components[comp_type] = comp_type()
            PyBus.Instance().post(ComponentAddedEvent(self))

    def remove_component(self, comp_type: Type[Component]):
        if comp_type in self.components.keys():
            del self.components[comp_type]
            keys = self.key.get_keys()
            keys.remove(comp_type)
            self.key = ComponentKey(keys)
            PyBus.Instance().post(ComponentRemovedEvent(self))

    @property
    def components(self) -> Dict[Type[Component], Component]:
        return self._components

    @components.setter
    def components(self, value: Dict[Type[Component], Component]):
        self._components = value

    @property
    def key(self) -> ComponentKey:
        return self._key

    @key.setter
    def key(self, value: ComponentKey):
        self._key = value

    @property
    def id(self) -> uuid.UUID:
        return self._id

    @id.setter
    def id(self, value: uuid.UUID):
        self._id = value
