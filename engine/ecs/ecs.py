from typing import Type, List, Dict
from typing import TypeVar

from engine.ecs.entity import Entity
from engine.ecs.events.entity_added_event import EntityAddedEvent
from engine.ecs.events.entity_removed_event import EntityRemovedEvent
from engine.ecs.scene import Scene

import loguru

from pyeventbus3.pyeventbus3 import PyBus

from engine.ecs.system import System


E = TypeVar("E", bound=Entity)
S = TypeVar("S")


class Ecs:
    def __init__(self, scenes: List[Type[Scene]]=None):
        super(Ecs, self).__init__()
        loguru.logger.info("Ecs started...")
        self.scenes = scenes
        self.scene_index = 0
        self.current_scene = None
        self.engine = None
        if self.scenes is not None:
            self.load_scene(0)

    def load_scene(self, index: int) -> None:
        self.scene_index = index
        self.current_scene = self.scenes[self.scene_index]()
        loguru.logger.info("Loading Scene: [{}]".format(self.current_scene))

        for system_type in self.current_scene.system_types:
            self.load_system(system_type)

        for entity_type in self.current_scene.entity_types:
            self.instantiate(entity_type)

    def start(self) -> None:
        self.current_scene.start()

    def update(self) -> None:
        self.current_scene.update()

    def load_system(self, system_type: [Type[S]]) -> S:
        if system_type not in self.current_scene.systems.keys():
            new_sys: S = system_type()
            PyBus.Instance().register(new_sys, system_type)
            self.current_scene.systems[system_type] = new_sys
            return system_type()

    def instantiate(self, entity: Type[E]) -> E:
        new_ent: E = entity()
        self.current_scene.entities[new_ent.id] = new_ent
        PyBus.Instance().post(EntityAddedEvent(self, new_ent))
        return new_ent

    def destroy(self, entity: Entity):
        del self.current_scene.entities[entity.id]
        PyBus.Instance().post(EntityRemovedEvent(self, entity))

    def get_system(self, system_type: Type[S]) -> S:
        return self.current_scene.systems[system_type]

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


_ecs: Ecs = None


def ECS(scenes: List[Type[Scene]]=None):
    global _ecs
    if _ecs is None:
        _ecs = Ecs(scenes)
    return _ecs
