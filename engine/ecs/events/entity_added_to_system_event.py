from engine.ecs.entity import Entity


class EntityAddedToSystemEvent:
	def __init__(self, entity: Entity):
		self._entity = entity

	@property
	def entity(self) -> Entity:
		return self._entity
