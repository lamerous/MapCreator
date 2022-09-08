import pygame
from tile import Tile

class Editor:
	def __init__(self, surface):
		self.surface = surface

		self.tile_group = pygame.sprite.Group()

	def draw_tiles(self, rows, cols, size):
		for i in range(cols):
			for j in range(rows):
				pos = (i * size[0], j * size[1])
				tile = Tile(size, pos, fill_color=(10, 100, 100))
				self.tile_group.add(tile)


	def update(self):
		self.tile_group.draw(self.surface)