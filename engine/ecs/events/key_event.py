from engine.input.key import Key
from engine.input.action import Action


class KeyEvent:
	def __init__(self, key: Key, action: Action):
		self._key = key
		self._action = action

	@property
	def action(self) -> Action:
		return self._action

	@property
	def key(self) -> Key:
		return self._key
