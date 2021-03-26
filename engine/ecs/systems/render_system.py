import skia

from engine.ecs.components.transform import Transform
from engine.ecs.system import System
from engine.ecs.components.sprite_renderer import SpriteRenderer
from engine.graphics.sprite import Sprite

import loguru


class RenderSystem(System):
	def __init__(self):
		super(RenderSystem, self).__init__([SpriteRenderer])

	def start(self, ecs=None):
		loguru.logger.info("Entity Count: {}".format(len(self.entities.keys())))

	def update(self, ecs=None):
		for ent in self.entities.values():
			loguru.logger.info("Entity: {}".format(ent.__class__.__name__))
			sr: SpriteRenderer = ent.get_component(SpriteRenderer)
			if sr.sprite is None:
				tr: Transform = ent.get_component(Transform)
				sr.sprite = Sprite(tr.position, sr.image)
			ecs.engine.draw(sr.layer, sr.sprite)



