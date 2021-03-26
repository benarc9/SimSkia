from abc import ABC
from typing import List
from typing import Type
from typing import TypeVar

from engine.ecs.ecs import Ecs
from engine.ecs.scene import Scene
from engine.engine import Engine


T = TypeVar("T", bound=Scene)


class Game(ABC):
    def __init__(self, scenes: List[Type[T]]):
        self.ecs = Ecs(scenes)
        self.engine = Engine()
        self.ecs.engine = self.engine
        self.running = False

    def start(self):
        self.engine.start()
        self.ecs.start()

    def run(self):
        self.running = True
        while self.running:
            self.ecs.update()
            self.running = self.engine.update()

