import unittest
from typing import Type
from unittest import mock
from uuid import uuid4

from engine.ecs.ecs import Ecs
from engine.ecs.entity import Entity
from engine.ecs.scene import Scene
from engine.ecs.system import System


class TestEcs(unittest.TestCase):
    def setUp(self) -> None:
        self.ecs = Ecs()

    @mock.patch('engine.ecs.ecs.Scene')
    def test_ecs_created(self, scene):
        ecs = Ecs(scene)
        self.assertIsNotNone(ecs, "Ecs should be created")

    @mock.patch('engine.ecs.system.System')
    def test_load_system_adds_system_to_ecs(self, system_type):
        self.ecs.load_system(system_type)
        self.assertIn(system_type, self.ecs.current_scene.systems)

    @mock.patch('engine.ecs.entity.Entity')
    def test_instantiate_creates_entity(self, entity_type):
        mock_prop = uuid4()
        entity_type.id = mock_prop
        self.ecs.instantiate(entity_type)
        self.assertEqual(len(self.ecs.current_scene.entities.items()), 1)

if __name__ == '__main__':
    unittest.main()
