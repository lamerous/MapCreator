import pygame
from tile import Tile

class Editor:
	def __init__(self, surface):
		self.surface = surface

		self.tile_group = pygame.sprite.Group()

		self.test_image = [pygame.image.load("tiles/sprite2.png"), pygame.image.load("tiles/sprite1.png")]
		self.iter = 0

		self.fill_image = None

		# self.map structure 
		# [{(x1, y1): pygame.Image1}, {(x2, y2): pygame.Image2}, ...]
		self.map = []

	def draw_tiles(self, rows, cols, size):
		for i in range(cols):
			for j in range(rows):
				pos = (i * size[0], j * size[1])
				tile = Tile(size, pos, fill_color=(100, 100, 100))
				self.tile_group.add(tile)


	def update(self, mouse_buttons):
		# mouse_buttons = {1: bool, 2: bool, 3: bool} 
		# 1 - left mouse button, 2 - center mouse button, 3 - right mouse button
		# bool - True or False

		mouse_x, mouse_y = pygame.mouse.get_pos()

		self.surface.fill((pygame.Color("darkred")))
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

				# left mouse button
				if mouse_buttons[1]:
					if not self.fill_image:
						if self.map.count({pos: self.test_image[self.iter]}) < 1:
							self.map.append({pos: self.test_image[self.iter]})
							self.iter += 1
							if self.iter > 1:
								self.iter = 0
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

		# draw tiles
		for i in self.map:
			for coords in i:
				image = i[coords]
				image = pygame.transform.scale(image, size)
				self.surface.blit(image, (coords))

