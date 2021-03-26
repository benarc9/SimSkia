from typing import Type, List, Dict
from typing import TypeVar

from engine.ecs.entity import Entity
from engine.ecs.scene import Scene
from engine.ecs.system import EntityRemovedEvent
from engine.ecs.system import System, EntityAddedEvent

import loguru

from pyeventbus3.pyeventbus3 import *


E = TypeVar("E", bound=Entity)
S = TypeVar("S", bound=System)


class Ecs:
    def __init__(self, scenes: List[Type[Scene]]=None):
        super(Ecs, self).__init__()
        loguru.logger.info("Ecs started...")
        self.scenes = scenes
        self.entities = {}
        self.systems = {}
        self.scene_index = 0
        self.current_scene = None
        self.engine = None
        if self.scenes is not None:
            self.load_scene(0)

    def __str__(self):
        systems = []
        ents = []

        if self.systems.values() is None:
            systems = "No systems loaded"
        else:
            for system in self.systems.values():
                systems.append(system.__class__.__name__)

        if len(self.entities.values()) == 0:
            ents = "No entities loaded"
        else:
            for ent in self.entities.values():
                ents.append(ent.__class__.__name__)

        return "ECS\n" \
               "\tSystems:\n" \
               "\t\t{}" \
               "\n\tEntities:\n" \
               "\t\t{}".format(systems, ents)

    def load_scene(self, index: int) -> None:
        self.scene_index = index
        self.current_scene = self.scenes[self.scene_index]()
        loguru.logger.info("Loading Scene: [{}]".format(self.current_scene))

        for system_type in self.current_scene.system_types:
            self.load_system(system_type)

        for entity_type in self.current_scene.entity_types:
            self.instantiate(entity_type)

    def start(self) -> None:
        loguru.logger.info("Starting Ecs...\nStarting systems...")
        for system in self.systems.values():
            system.start(ecs=self)

    def update(self) -> None:
        # loguru.logger.info("Updating systems...")
        for system in self.systems.values():
            system.update(ecs=self)

    def load_system(self, system_type: [Type[S]]) -> S:
        if system_type not in self.systems.keys():
            new_sys: S = system_type()
            self.systems[system_type] = new_sys
            loguru.logger.info("System Loaded: [{}]".format(new_sys))
            return system_type()

    def instantiate(self, entity: Type[E]) -> E:
        loguru.logger.info("Instantiate called for entity type: {}".format(entity))
        new_ent: Entity = entity()
        self.entities[new_ent.id] = new_ent
        PyBus.Instance().post(EntityAddedEvent(self, new_ent))

    def destroy(self, entity: Entity):
        del self.entities[entity.id]
        PyBus.Instance().post(EntityRemovedEvent(self, entity))

    def get_system(self, system_type: Type[S]) -> S:
        return self.systems[system_type]

    @property
    def systems(self) -> Dict[Type[System], System]:
        return self._systems

    @systems.setter
    def systems(self, value: Dict[Type[System], System]):
        self._systems = value

    @property
    def scene_index(self) -> int:
        return self._scene_index

    @scene_index.setter
    def scene_index(self, value: int):
        self._scene_index = value

    @property
    def current_scene(self) -> Scene:
        return self._current_scene

    @current_scene.setter
    def current_scene(self, value: Scene):
        self._current_scene = value

    @property
    def scenes(self) -> List[Type[Scene]]:
        return self._scenes

    @scenes.setter
    def scenes(self, value: List[Type[Scene]]):
        self._scenes = value

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, value):
        self._engine = value



