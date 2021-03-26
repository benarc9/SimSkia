import skia

from engine.lib.math import Vector


class Sprite:
	def __init__(self, position: Vector, image: skia.Image):
		self.position = position
		self.image = image.bitmap(image.colorType())

	@property
	def position(self) -> Vector:
		return self._position

	@position.setter
	def position(self, value: Vector):
		self._position = value

	@property
	def image(self) -> skia.Bitmap:
		return self._image

	@image.setter
	def image(self, value: skia.Bitmap):
		self._image = value
