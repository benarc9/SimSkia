from engine.ecs.component import Component
import skia

from engine.graphics.sprite import Sprite


class SpriteRenderer(Component):
	def __init__(self):
		super(SpriteRenderer, self).__init__()
		self.layer = 0
		self.sprite = None
		self.image = None

	@property
	def sprite(self) -> Sprite:
		return self._sprite

	@sprite.setter
	def sprite(self, sprite: Sprite):
		self._sprite = sprite

	@property
	def layer(self) -> int:
		return self._layer

	@layer.setter
	def layer(self, value: int):
		self._layer = value

	@property
	def image(self) -> skia.Image:
		return self._image

	@image.setter
	def image(self, value: skia.Image):
		self._image = value

