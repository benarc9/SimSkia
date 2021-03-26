from typing import Generic
from typing import TypeVar


T = TypeVar("T")


class Event(Generic[T]):
	def __init__(self, source: T, **kwargs):
		self.source = source
		for key in kwargs:
			self.__setattr__(key, kwargs[key])

	@property
	def source(self) -> T:
		return self._source

	@source.setter
	def source(self, value: T):
		self._source = value
