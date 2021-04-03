from typing import TypeVar

T = TypeVar("T")


def singleton(self, clazz: T) -> T:
	instance: T = None
	def wrapper(*args, **kwargs):
		global instance
		if instance is None:
			instance = clazz(*args, **kwargs)
		return instance

	return wrapper

