import pygame

class Button(pygame.sprite.Sprite):
	def __init__(self, size, position, *, fill_color = (200, 200, 200), border_color = (0, 0, 0)):
		pygame.sprite.Sprite.__init__(self)

				