from engine.lib.event import Event


class ComponentAddedEvent(Event):
	def __init__(self, source):
		super(ComponentAddedEvent, self).__init__(source)
