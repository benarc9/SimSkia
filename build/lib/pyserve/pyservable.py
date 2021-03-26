from typing import List
from abc import ABC


class Observer(ABC):
	def __init__(self):
		super(Observer, self).__init__()

	def update(self, observable: 'Observable', arg: object):
		raise NotImplementedError()


class Observable(ABC):
	def __init__(self):
		self.changed: bool = False
		self.obs: List[Observer] = []

	def add_observer(self, observer: Observer) -> None:
		if observer is None:
			raise ValueError("Observer is None")
		if observer not in self.obs:
			self.obs.append(observer)

	def delete_observer(self, observer: Observer) -> None:
		self.obs.remove(observer)

	def notify_observers(self, *args) -> None:
		if not self.changed:
			return
		self.clear_changed()

		length = len(self.obs) - 1
		for i in range(length, -1, -1):
			self.obs[i].update(self, args)

	def delete_observers(self) -> None:
		self.obs.clear()

	def set_changed(self) -> None:
		self.changed = True

	def clear_changed(self) -> None:
		self.changed = False

	def has_changed(self) -> bool:
		return self.changed

	def count_observers(self) -> int:
		return len(self.obs)
