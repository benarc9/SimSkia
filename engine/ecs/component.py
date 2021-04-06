from abc import ABC


class Component(ABC):
    def __init__(self):
        super(Component, self).__init__()
        self.entity = None

    def __str__(self):
        return "Component [{}]".format(self.__class__.__name__)

    @property
    def entity(self):
        return self._entity

    @entity.setter
    def entity(self, value):
        self._entity = value
