import pygame

class Tile(pygame.sprite.Sprite):
	def __init__(self, size, position, image = None, *, fill_color = (0, 0, 0), border_color = (200, 200, 200)):
		pygame.sprite.Sprite.__init__(self)

		self.size = size
		self.position = position
		self.fill_color = fill_color
		self.border_color = border_color

		if image:
			self.set_image(image)
		else:
			self.image = pygame.Surface(size)
			self.image.fill(fill_color)

		pygame.draw.rect(self.image, self.border_color, (0, 0) + self.size, 1)

		self.rect = self.image.get_rect()

		self.rect.x = position[0]
		self.rect.y = position[1]

	def get_position(self):
		return (self.rect.x, self.rect.y)

	def set_image(self, image):
		self.image = image
		self.image = pygame.transform.scale(self.image, self.size)
		pygame.draw.rect(self.image, self.border_color, (0, 0) + self.size, 1)