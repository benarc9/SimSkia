from abc import ABC
from typing import Generic
from typing import List
from typing import TypeVar


B = TypeVar("B")


class Bindable(Generic[B], ABC):
    def __init__(self):
        super(Bindable, self).__init__()
        self.bound = []

    def bind(self, other: 'Bindable'):
        if self not in other.bound:
            other.bound.append(self)

    def unbind(self, other: 'Bindable'):
        if self in other.bound:
            other.bound.remove(self)
        if other in self.bound:
            self.bound.remove(other)

    def bind_bidirectional(self, other: 'Bindable'):
        if other not in self.bound:
            self.bound.append(other)
        if self not in other.bound:
            other.bind(self)

    def remote_change(self, new: B):
        raise NotImplementedError()

    def changed(self, new_value: B):
        for bound in self.bound:
            bound.remote_change(new_value)

    @property
    def bound(self) -> List['Bindable']:
        return self._bound

    @bound.setter
    def bound(self, value: List['Bindable']):
        self._bound = value
