import pygame
from tile import Tile
from settings import *

class Editor:
	def __init__(self, surface, *, fill_color = (0, 0, 0), tile_color = (0, 0, 0)):
		self.surface = surface

		self.fill_color = fill_color
		self.tile_color = tile_color

		self.position = [0, 0]

		self.tile_group = pygame.sprite.Group()

		self.fill_image = None

		self.cols = 0
		self.row = 0

		self.tile_size = [0, 0]

		# self.map structure 
		# [{(x1, y1): pygame.Image1}, {(x2, y2): pygame.Image2}, ...]
		self.map = []

	def draw_tiles(self, rows, cols, size):
		for i in range(cols):
			for j in range(rows):
				pos = (i * size[0], j * size[1])
				tile = Tile(size, pos, fill_color=self.tile_color)
				self.tile_group.add(tile)

		self.sel_rect = pygame.Surface(size)
		self.sel_rect.fill((0, 0, 200))
		self.sel_rect.set_alpha(100)

		self.tile_size = size
		self.cols = cols
		self.rows = rows

	def move(self, speed_x, speed_y, win_width, win_height):
		if speed_x > 0 and self.position[0] < 0:
			self.position[0] += speed_x
		if speed_x < 0 and self.position[0] > -self.surface.get_width() + win_width:
			self.position[0] += speed_x
		if speed_y > 0 and self.position[1] < 0:
			self.position[1] += speed_y
		if speed_y < 0 and self.position[1] > -self.surface.get_height() + win_height:
			self.position[1] += speed_y

		return self.position

	def set_fill_image(self, image):
		self.fill_image = image

	def update(self, mouse_buttons):
		# mouse_buttons = {1: bool, 2: bool, 3: bool} 
		# 1 - left mouse button, 2 - center mouse button, 3 - right mouse button
		# bool - True or False

		mouse_pos = pygame.mouse.get_pos()
		mouse_x, mouse_y = mouse_pos[0] - self.position[0], mouse_pos[1] - self.position[1]

		self.surface.fill(self.fill_color)
		self.tile_group.draw(self.surface)

		# draw tiles
		for i in self.map:
			for coords in i:
				image = i[coords]
				image = pygame.transform.scale(image, self.tile_size)
				self.surface.blit(image, (coords))

		for tile in self.tile_group:
			rect = tile.get_rect()
			size = tile.get_size()
			pos = tile.get_position()

			# if cursor on tile
			if rect.x < mouse_x and rect.x + rect.width > mouse_x and rect.y < mouse_y and rect.y + rect.height > mouse_y and mouse_x + self.position[0] < TILE_CH_POS[0]:
				# init selection rect
				left_angle_coord = mouse_x // size[0] * size[0], mouse_y // size[1] * size[1]
				self.surface.blit(self.sel_rect, left_angle_coord)

				# left mouse button
				if mouse_buttons[1]:
					if self.fill_image:
						if self.map.count({pos: self.fill_image}) < 1:
							self.map.append({pos: self.fill_image})
					else:
						print("No choosen image")

				# right mouse button
				if mouse_buttons[3]:
					_break = False  # to quit

					# find first element and break
					for i in reversed(self.map):
						for coords in i:
							if coords == left_angle_coord:
								self.map.remove(i)
								_break = True

						if _break:
							break

	def zoom(self, zoom_dir):
		if self.tile_size[0] + zoom_dir != 0 and self.tile_size[1] + zoom_dir != 1:
			self.tile_size[0] += zoom_dir
			self.tile_size[1] += zoom_dir

		new_tile_group = pygame.sprite.Group()

		for i in range(self.cols):
			for j in range(self.rows):
				pos = (i * self.tile_size[0], j * self.tile_size[1])
				tile = Tile(self.tile_size, pos, fill_color=self.tile_color)
				new_tile_group.add(tile

		self.sel_rect = pygame.transform.scale(self.sel_rect, self.tile_size)

		self.tile_group = new_tile_group