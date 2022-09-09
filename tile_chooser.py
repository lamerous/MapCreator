import pygame
from tile import Tile
import os

class TileChooser:
	def __init__(self, surface):
		self.surface = surface

		self.tiles = pygame.sprite.Group()

	def load_images(self, path, tiles_in_row):
		for i in os.listdir(path):
			# if last 4 symbols
			if i[-4:] == '.png':
				size = (self.surface.get_width() / tiles_in_row, self.surface.get_width() / tiles_in_row)
				x, y = 0, 0
				


	def update(self):
		pass