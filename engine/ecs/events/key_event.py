from engine.input.key import Key
from engine.input.key_action import KeyAction


class KeyEvent:
	def __init__(self, key: Key, action: KeyAction):
		self._key = key
		self._action = action

	@property
	def action(self) -> KeyAction:
		return self._action

	@property
	def key(self) -> Key:
		return self._key
