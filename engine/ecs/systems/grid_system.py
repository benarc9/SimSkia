from engine.ecs.components.tile_map import TileMap
from engine.ecs.system import System


class GridSystem(System):
	def __init__(self):
		super(GridSystem, self).__init__([TileMap])

	def update(self):
		pass

	def start(self):
		pass
