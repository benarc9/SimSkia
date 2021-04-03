from engine.ecs.entity import Entity
from engine.ecs.system import System

from engine.ecs.components.transform import Transform
from engine.lib.math import Vector

import loguru


class WorldSystem(System):
	def __init__(self):
		super(WorldSystem, self).__init__([Transform])

	def start(self, ecs=None):
		pass

	def update(self, ecs=None):
		pass

	def translate(self, entity: Entity, vector: Vector):
		transform: Transform = entity.get_component(Transform)
		transform.position = transform.position.translate(vector)
