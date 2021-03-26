from abc import ABC
from typing import Callable
from typing import List
from typing import Type
from typing import TypeVar

from engine.lib.event import Event


T = TypeVar("T", bound=Event)


class Observer(ABC):
	def __init__(self, event_types: List[Type[Event]]):
		super(Observer, self).__init__()
		self.event_types = event_types
		self.registration = {}

	def on_event(self, event: T):
		raise NotImplementedError()

	def subscribe(self, funct):
		pass

	@property
	def event_types(self) -> List[Type[Event]]:
		return self._event_types
	
	@event_types.setter
	def event_types(self, value: List[Type[Event]]):
		self._event_types = value
