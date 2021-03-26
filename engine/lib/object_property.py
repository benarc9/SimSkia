from typing import Generic
from typing import TypeVar

from engine.lib.observable_property import ObservableProperty


B = TypeVar("B")


class ObjectProperty(Generic[B], ObservableProperty[B]):
    def __init__(self, value: B=None):
        super(ObjectProperty, self).__init__(value)
