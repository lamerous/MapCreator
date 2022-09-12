import pygame
from tile import Tile
from settings import *
import os
from math import ceil

class TileChooser:
	def __init__(self, surface, start_position, *, fill_color = (0, 0, 0), tiles_in_row = 4):
		self.surface = surface

		self.fill_color = fill_color

		self.tiles_in_row = tiles_in_row

		self.tile_size = 0, 0

		self.position = start_position

		self.count = 0

		self.original_images = []   # save original images to protect them from damage when resizing
		self.tile_group = pygame.sprite.Group()

	def calculate_new_height(self):
		return ceil((self.count+self.tiles_in_row) / self.tiles_in_row) * self.tile_size[1]

	def load_images(self, path):
		x, y = 0, 0
		count = 0
		for i in os.listdir(path):
			# if last 4 symbols
			if i[-4:] == '.png':
				if x % self.tiles_in_row == 0 and x != 0:
					x = 0
					y += 1

				size = (int(self.surface.get_width() / self.tiles_in_row), int(self.surface.get_width() / self.tiles_in_row))
				self.tile_size = size
				pos = x * size[0], y * size[1]
				image = pygame.image.load(path+'/'+i)
				tile = Tile(size, pos, image)
				self.original_images.append(image)
				self.tile_group.add(tile)

				x += 1
				self.count += 1

	def scroll(self, speed, win_height):
		if speed < 0:
			if self.position[1] + speed - win_height > -self.surface.get_height():
				self.position[1] += speed
		else:
			if self.position[1] < 0:
				self.position[1] += speed

		return self.position

	def set_new_surface(self, surface):
		self.surface = surface

	def update(self, editor, mouse_buttons=None):
		# mouse_buttons = {1: bool, 2: bool, 3: bool} 
		# 1 - left mouse button, 2 - center mouse button, 3 - right mouse button
		# bool - True or False

		mouse_pos = pygame.mouse.get_pos()
		mouse_x, mouse_y = mouse_pos[0] - EDITOR_WIDTH, mouse_pos[1] - self.position[1]

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

	def zoom(self, zoom_dir):
		if self.tiles_in_row + zoom_dir != 0:
			self.tiles_in_row += zoom_dir

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
