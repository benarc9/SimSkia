import unittest
from typing import Type
from unittest import mock
from uuid import uuid4

from engine.ecs.ecs import Ecs
from engine.ecs.entity import Entity
from engine.ecs.scene import Scene
from engine.ecs.system import System


class TestComponent(unittest.TestCase):

	def setUp(self) -> None:
		pass

	def test_component_entity_attribute_not_none(self, ):
		pass
