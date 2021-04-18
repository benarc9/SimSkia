from engine.ecs.component import Component

from enum import Enum


class MapType(Enum):
	Square = 1
	Hex = 2
	Iso = 3


class TileMap(Component):
	def __init__(self):
		super(TileMap, self).__init__()

	@property
	def map_type(self) -> MapType:
		return self.map_type

	@map_type.setter
	def map_type(self, value: MapType):
		self.map_type = value
