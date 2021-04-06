from typing import Dict

from engine.ecs.events.key_event import Key
from engine.input.button import Button


class ControlLayout:
	def __init__(self, name: str):
		self._name = name
		self.button_map = {}
		self.action_map = {}

	def map(self, key: Key, button: Button) -> "ControlLayout":
		self.button_map[key] = button
		return self

	def is_mapped(self, key: Key) -> bool:
		return key in self.button_map.keys()

	@property
	def button_map(self) -> Dict[Key, Button]:
		return self._button_map

	@button_map.setter
	def button_map(self, value: Dict[Key, Button]):
		self._button_map = value

	@property
	def name(self) -> str:
		return self._name
