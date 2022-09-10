import pygame
from tile import Tile
from settings import *
import os

class TileChooser:
	def __init__(self, surface, *, fill_color = (0, 0, 0), tiles_in_row = 4):
		self.surface = surface

		self.fill_color = fill_color

		self.tiles_in_row = tiles_in_row

		self.position = [0, 0]

		self.original_images = []   # for save original images to protect from damage images when resizing
		self.tile_group = pygame.sprite.Group()

	def load_images(self, path):
		x, y = 0, 0
		for i in os.listdir(path):
			# if last 4 symbols
			if i[-4:] == '.png':
				if x % self.tiles_in_row == 0 and x != 0:
					x = 0
					y += 1

				size = (int(self.surface.get_width() / self.tiles_in_row), int(self.surface.get_width() / self.tiles_in_row))
				pos = x * size[0], y * size[1]
				image = pygame.image.load(path+'/'+i)
				tile = Tile(size, pos, image)
				self.original_images.append(image)
				self.tile_group.add(tile)

				x += 1

	def scroll(self):
		keys = pygame.key.get_pressed()


	def update(self, editor, mouse_buttons=None):
		# mouse_buttons = {1: bool, 2: bool, 3: bool} 
		# 1 - left mouse button, 2 - center mouse button, 3 - right mouse button
		# bool - True or False

		mouse_pos = pygame.mouse.get_pos()
		mouse_x, mouse_y = mouse_pos[0] - EDITOR_WIDTH, mouse_pos[1]

		self.surface.fill(self.fill_color)
		self.tile_group.draw(self.surface)

		for tile in self.tile_group:
			rect = tile.get_rect()
			size = tile.get_size()
			pos = tile.get_position()
			# if cursor on tile
			if rect.x < mouse_x and rect.x + rect.width > mouse_x and rect.y < mouse_y and rect.y + rect.height > mouse_y:
				# draw selection rect
				sel_rect = pygame.Surface(size)
				sel_rect.fill((0, 0, 200))
				sel_rect.set_alpha(100)

				left_angle_coord = mouse_x // size[0] * size[0], mouse_y // size[1] * size[1]

				self.surface.blit(sel_rect, left_angle_coord)

				#left mouse click
				if mouse_buttons[1]:
					editor.set_fill_image(tile.get_image())

	def zoom(self, scroll_dir):
		# scroll_dir
		#  1 zoom in 
		# -1 zoom out

		if self.tiles_in_row + scroll_dir != 0:
			self.tiles_in_row += scroll_dir

		new_tile_group = pygame.sprite.Group()

		x, y = 0, 0

		for i, tile in enumerate(self.tile_group):

			if x % self.tiles_in_row == 0 and x != 0:
				x = 0
				y += 1

			size = (int(self.surface.get_width() / self.tiles_in_row), int(self.surface.get_width() / self.tiles_in_row))
			pos = x * size[0], y * size[1]

			image = self.original_images[i]
			image = pygame.transform.scale(image, size)

			new_tile = Tile(size, pos, image)
			new_tile_group.add(new_tile)

			x += 1

		self.tile_group = new_tile_group
