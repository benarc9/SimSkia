from engine.lib.observable_property import ObservableProperty


class BoolProperty(ObservableProperty[bool]):
    def __init__(self, initial: bool=None):
        super(BoolProperty, self).__init__(initial)
