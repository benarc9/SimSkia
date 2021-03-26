from engine.ecs.component import Component

from engine.lib.math import Vector, Translation


class Transform(Component):
	def __init__(self):
		super(Transform, self).__init__()
		self.position = Vector(0,0)
		self.scale = Vector(1,1)
		self.rotation = Vector(0,0)

	@property
	def position(self) -> Vector:
		return self._position

	@position.setter
	def position(self, value: Vector):
		self._position = value

	@property
	def scale(self) -> Vector:
		return self._scale

	@scale.setter
	def scale(self, value: Vector):
		self._scale = value

	@property
	def rotation(self) -> Vector:
		return self._rotation

	@rotation.setter
	def rotation(self, value: Vector):
		self._rotation = value

