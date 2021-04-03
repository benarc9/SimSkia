from typing import List

from engine.graphics.sprite import Sprite


class SpriteBatch:
	def __init__(self):
		self.sprites: List[Sprite] = []

	@property
	def sprites(self) -> List[Sprite]:
		return self._sprites

	@sprites.setter
	def sprites(self, value: List[Sprite]):
		self._sprites = value
