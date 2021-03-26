from abc import ABC


class Component(ABC):
    def __init__(self):
        super(Component, self).__init__()

    def __str__(self):
        return "Component [{}]".format(self.__class__.__name__)
