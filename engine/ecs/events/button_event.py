from engine.ecs.events.key_event import KeyAction
from engine.input.button import Button
from engine.lib.event import Event


class ButtonEvent(Event):
	def __init__(self, controller: str, button: Button, action: KeyAction):
		super(ButtonEvent, self).__init__(self)
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

