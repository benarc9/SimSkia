from engine.ecs.entity import Entity
from engine.lib.event import Event


class EntityAddedEvent(Event):
	def __init__(self, source, entity: Entity):
		super(EntityAddedEvent, self).__init__(source)
		self.entity = entity

	@property
	def entity(self) -> Entity:
		return self._entity

	@entity.setter
	def entity(self, value: Entity):
		self._entity = value
