from engine.ecs.components.input_controller import InputController
from engine.ecs.components.transform import Transform
from engine.ecs.events.button_event import ButtonEvent
from engine.game import Game
from engine.ecs.scene import Scene
from engine.ecs.entity import Entity
from engine.ecs.components.sprite_renderer import SpriteRenderer
from engine.ecs.systems.world_system import WorldSystem
from engine.ecs.systems.render_system import RenderSystem
from engine.ecs.systems.input_system import InputSystem

from pyeventbus3.pyeventbus3 import PyBus, subscribe

import skia

from engine.input.control_layout import ControlLayout
from engine.ecs.events.key_event import Key
from engine.input.button import Button

from loguru import logger
log = logger.info


class OtherPlayer(Entity):
	def __init__(self):
		super(OtherPlayer, self).__init__([SpriteRenderer])
		sr: SpriteRenderer = self.get_component(SpriteRenderer)
		sr.image = skia.Image.open('./tests/resources/pic.jpeg')


class Player(Entity):
	def __init__(self):
		super(Player, self).__init__([SpriteRenderer, InputController])
		sr: SpriteRenderer = self.get_component(SpriteRenderer)
		sr.image = skia.Image.open('./tests/resources/pic.jpeg')
		controller = ControlLayout("Player")
		controller\
			.map(Key.W, Button.DIR_UP)\
			.map(Key.S, Button.DIR_DOWN)\
			.map(Key.A, Button.DIR_LEFT)\
			.map(Key.D, Button.DIR_RIGHT)
		input = self.get_component(InputController)
		input.control_layout = controller


class TestScene(Scene):
	def __init__(self):
		super(TestScene, self).__init__([WorldSystem, RenderSystem, InputSystem], [Player])
		PyBus.Instance().register(self, self.__class__.__name__)
		self.player: Player

	def start(self):
		super(TestScene, self).start()
		self.player = self.find_entity("Player")
		transform = self.player.get_component(Transform)
		if transform is not None:
			log("Transform NOT none")
			if transform.entity is None:
				log("Transform entity attribute IS none")
			else:
				log("Transform entity attribute is NOT none: {}".format(transform.entity))
		else:
			log("Transform IS none")

	def update(self):
		super(TestScene, self).update()

	@subscribe(onEvent=ButtonEvent)
	def on_button_event(self, event: ButtonEvent):
		if event.controller == "Player":
			if event.button is Button.DIR_UP:
				transform: Transform = self.player.get_component(Transform)
				if transform is not None:
					log("Transform = Position: {}\tScale: {}\tRotation: {}".format(transform.position, transform.scale, transform.rotation))
				else:
					log("Transform not found!")
		else:
			log("Controller: {}".format(event.controller))


class SimGame(Game):
	def __init__(self):
		super(SimGame, self).__init__([TestScene])
