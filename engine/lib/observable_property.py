from abc import ABC
from typing import TypeVar

from engine.lib.bindable import Bindable


B = TypeVar("B")


class ObservableProperty(Bindable[B], ABC):
    def __init__(self, value: B=None):
        self._value = value
        super(ObservableProperty, self).__init__()

    def __str__(self):
        return str(self.value)

    def remote_change(self, new: B):
        self.value = new

    @property
    def value(self) -> B:
        return self._value

    @value.setter
    def value(self, value: B):
        if self._value != value:
            self._value = value
            self.changed(self._value)
