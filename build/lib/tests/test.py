import unittest
from unittest import mock
from engine import Ecs
from engine.ecs import Ecs, System, Entity, ECS
from engine.game import Game
from engine.engine import Engine
from pyserve.pyservable import Observer, Observable


class TestEcs(unittest.TestCase):
    def setUp(self) -> None:
        self.scenes = [mock.Mock(), mock.Mock()]

    @mock.patch('engine.ecs.Scene')
    def test_ecs_created(self, scene):
        ecs = ECS([scene])
        print(ecs.current_scene)
        self.assertIsNotNone(ecs, "Ecs should be created")

    @mock.patch('engine.ecs.Scene')
    def test_init_ecs_loads_first_scene(self, newScene):
        ecs = ECS([newScene])
        print(ecs.current_scene)
        self.assertTrue(newScene == ecs.current_scene, "Ecs should load the first passed in scene")

if __name__ == '__main__':
    unittest.main()
