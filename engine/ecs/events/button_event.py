from engine.ecs.events.key_event import KeyAction
from engine.input.button import Button


class ButtonEvent:
	def __init__(self, controller: str, button: Button, action: KeyAction):
		self._controller = controller
		self._button = button
		self._action = action

	@property
	def controller(self) -> str:
		return self._controller

	@property
	def button(self) -> Button:
		return self._button

	@property
	def action(self) -> KeyAction:
		return self._action

