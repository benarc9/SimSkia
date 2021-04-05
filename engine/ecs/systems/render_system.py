from engine.ecs.components.transform import Transform
from engine.ecs.system import System
from engine.ecs.components.sprite_renderer import SpriteRenderer
from engine.graphics.sprite import Sprite

from engine.ecs.ecs import ECS


class RenderSystem(System):
	def __init__(self):
		super(RenderSystem, self).__init__([SpriteRenderer])

	def start(self):
		self.ecs = ECS()

	def update(self):
		for ent in super().entities.values():
			sr: SpriteRenderer = ent.get_component(SpriteRenderer)
			tr: Transform = ent.get_component(Transform)
			sr.sprite = Sprite(tr.position, sr.image)

			self.ecs.engine.draw(sr.layer, sr.sprite)

