from engine.ecs.ecs import Ecs
from engine.ecs.scene import Scene
from engine.engine import Engine
from abc import ABC


class Game(ABC):
    def __init__(self, engine: Engine, ecs: Ecs):
        self.engine = engine
        self.ecs = ecs
        self.running = False

    def start(self):
        self.ecs.start()
        self.engine.start()

    def run(self):
        self.running = True
        while self.running:
            self.ecs.update()
            self.running = self.engine.update()

