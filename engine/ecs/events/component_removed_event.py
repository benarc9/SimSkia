from engine.lib.event import Event


class ComponentRemovedEvent(Event):
	def __init__(self, source):
		super(ComponentRemovedEvent, self).__init__(source)
