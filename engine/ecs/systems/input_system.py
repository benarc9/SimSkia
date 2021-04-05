from engine.ecs.events.button_event import ButtonEvent
from engine.ecs.events.key_event import KeyEvent, Key, KeyAction
from engine.ecs.system import System
from engine.ecs.ecs import ECS

from pyeventbus3.pyeventbus3 import PyBus, subscribe

from loguru import logger
log = logger.info


class InputSystem(System):

	def __init__(self):
		super(InputSystem, self).__init__([])

	def start(self):
		ECS().engine.set_key_callback(self.key_pressed)

	def update(self):
		pass

	def key_pressed(self, window, key, scancode, action, mods):
		PyBus.Instance().post(KeyEvent(Key(key), KeyAction(action)))

	@subscribe(onEvent=ButtonEvent)
	def on_button_event(self, event: ButtonEvent):
		pass






