from typing import List
from typing import TypeVar
from abc import ABC

from engine.lib.observable_property import ObservableProperty

T = TypeVar("T")


class ListProperty(ObservableProperty[List[T]], ABC):
	def __init__(self, list_val: List[T]=None):
		super(ListProperty, self).__init__(list_val)

	def add(self, val: T):
		self.value.append(val)
		self._changed()

	def remove(self, val: T):
		self.value.remove(val)
		self._changed()

	def clear(self):
		self.value = list()
		self._changed()

	def _changed(self):
		self.changed(self.value)



