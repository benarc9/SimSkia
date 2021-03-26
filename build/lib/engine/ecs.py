from typing import Type, List, Dict
import uuid
from engine.engine import Engine
from abc import ABC
from pyserve.pyservable import Observer, Observable


class EcsInterface(ABC):
    def __init__(self, engine: Engine):
        self.engine = engine
        self.engine.ecs_update = self.update

    def start(self) -> None:
        raise NotImplementedError("ECS start method not implemented!")

    def update(self) -> None:
        raise NotImplementedError("ECS update method not implemented!")

    @property
    def engine(self) -> Engine:
        return self._engine

    @engine.setter
    def engine(self, value: Engine):
        self._engine = value


class Assignable:
    def assign(self, target):
        raise NotImplementedError("Object must implement assign method!")


class Component(ABC):
    def __init__(self):
        super(Component, self).__init__()

    def __str__(self):
        return "Component [{}]".format(self.__class__.__name__)


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


class ComponentKey(Matchable):
    def __init__(self, keys: List[Type[Component]]):
        super(ComponentKey, self).__init__(keys)
        self.key = []

    def get_keys(self) -> List[Type[Component]]:
        return self.key

    def __str__(self):
        return "\n".join(self.key)


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


class Entity(Observable):
    def __init__(self, components: List[Type[Component]]):
        super(Entity, self).__init__()
        self.key = ComponentKey(components)
        self.components = {}
        self.ecs = _ecs
        self.id = uuid.uuid4()

        for component in components:
            self.components[component] = component()

    def __str__(self):
        id = self.id.__str__()
        key = self.key.__str__()
        out = [self.__class__.__name__, id, key]
        return "\n".join(out)

    def get_component(self, comp_type: Type[Component]):
        return self.components[comp_type]

    def add_component(self, comp_type: Type[Component]):
        if comp_type not in self.components.keys():
            keys = self.key.get_keys()
            keys.append(comp_type)
            self.key = ComponentKey(keys)
            self.components[comp_type] = comp_type()
            self.notify_observers(self, self)

    def remove_component(self, comp_type: Type[Component]):
        if comp_type in self.components.keys():
            del self.components[comp_type]
            keys = self.key.get_keys()
            keys.remove(comp_type)
            self.key = ComponentKey(keys)
            self.notify_observers(self, self)


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


class System(Observer):
    def __init__(self, key: List[Type[Component]]):
        super(System, self).__init__()
        self.key = ComponentKey(key)
        self.entities: Dict[uuid.UUID, Entity] = {}

    def __str__(self):
        key = self.key.__str__()
        ents = []
        if len(self.entities.values()) == 0:
            ents = "No entities"
        else:
            for ent in self.entities.values():
                ents.append(ent)

        return "System [ {} ] \n" \
               "\tComponent Key: \n" \
               "\tEntities: \n" \
               "\t{}".format(self.__class__.__name__, self.key, ents)

    def update(self, observable, *args):
        target: Entity = None

        if isinstance(observable, Entity):
            target = observable
        elif isinstance(observable, Ecs):
            target: Entity = args[0]

        if target is not None:
            if self.key.__eq__(target.key):
                self.entities[target.id] = target
                target.add_observer(self)
            else:
                del self.entities[target.id]
                target.delete_observer(self)

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


class Scene(ABC):
    def __init__(self, systems_types: List[Type[System]], entity_types: List[Type[Entity]]):
        self._system_types = systems_types
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


class Ecs(Observable):
    def __init__(self, scenes: List[Type[Scene]], debug: bool=False):
        Observable.__init__(self)
        self.scenes = scenes
        self.entities: Dict[int, Entity] = {}
        self.systems = {}
        self.scene_index = 0
        self.current_scene = None
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

        for system_type in self.current_scene.system_types:
            self.systems[system_type] = system_type()
            self.add_observer(self.systems[system_type])

        for entity_type in self.current_scene.entity_types:
            newEnt: Entity = entity_type()
            self.entities[newEnt.id] = newEnt

    def start(self) -> None:
        print("Starting ECS")

    def update(self) -> None:
        pass

    def instantiate(self, entity: Type[Entity]):
        new_ent: Entity = entity()
        self.notify_observers(self, new_ent)

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


_ecs: Ecs = None


def ECS(scenes, debug=False):
    global _ecs
    if _ecs is None:

        _ecs = Ecs(scenes, debug)
    return _ecs
