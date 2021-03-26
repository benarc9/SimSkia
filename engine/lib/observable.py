from abc import ABC
from typing import Generic
from typing import List
from typing import TypeVar

from engine.lib.observer import Observer
from engine.lib.event import Event


T = TypeVar("T")


class Observable(ABC):
	def __init__(self):
		super(Observable, self).__init__()
		self.observers = list()

	def notify(self, event: Event):
		for observer in self.observers:
			observer.on_event(event)

	def add(self, observer: Observer):
		if observer not in self.observers:
			self.observers.append(observer)

	def remove(self, observer: Observer):
		self.observers.remove(observer)

	@property
	def observers(self) -> List[Observer]:
		return self._observers

	@observers.setter
	def observers(self, value: List[Observer]):
		self._observers = value
