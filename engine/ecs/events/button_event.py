from engine.input.action import Action
from engine.input.button import Button


class ButtonEvent:
	def __init__(self, button: Button, action: Action, controller):
		self._controller = controller
		self._button = button
		self._action = action

	@property
	def controller(self):
		return self._controller

	@property
	def button(self) -> Button:
		return self._button

	@property
	def action(self) -> Action:
		return self._action

