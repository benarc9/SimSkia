from engine.game import Game
from engine.ecs.scene import Scene
from engine.ecs.entity import Entity
from engine.ecs.components.sprite_renderer import SpriteRenderer
from engine.ecs.systems.world_system import WorldSystem
from engine.ecs.systems.render_system import RenderSystem

import skia


class OtherPlayer(Entity):
	def __init__(self):
		super(OtherPlayer, self).__init__([SpriteRenderer])
		sr: SpriteRenderer = self.get_component(SpriteRenderer)
		sr.image = skia.Image.open('./tests/resources/pic.jpeg')


class Player(Entity):
	def __init__(self):
		super(Player, self).__init__([SpriteRenderer])
		sr: SpriteRenderer = self.get_component(SpriteRenderer)
		sr.image = skia.Image.open('./tests/resources/pic.jpeg')


class TestScene(Scene):
	def __init__(self):
		super(TestScene, self).__init__([WorldSystem, RenderSystem], [Player])



class SimGame(Game):
	def __init__(self):
		super(SimGame, self).__init__([TestScene])
