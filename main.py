import pygame
from editor import Editor
from menu import Menu
from tile import Tile
from settings import *

pygame.init()

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption(WIN_TITLE)

editor_surf = pygame.Surface((EDITOR_WIDTH, EDITOR_HEIGHT))
menu_surf = pygame.Surface((MENU_WIDTH, MENU_HEIGHT))
tile_ch_surf = pygame.Surface((TILE_CH_WIDTH, TILE_CH_HEIGHT))  # tile_ch -- tile_chooser

editor = Editor(editor_surf)
editor.draw_tiles(5, 10, TILE_SIZE)

menu = Menu(menu_surf)

run = True

while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			run = False

	editor_surf.fill(pygame.Color("darkred"))
	#menu_surf.fill(pygame.Color("darkorange"))
	#tile_ch_surf.fill(pygame.Color("darkgreen"))

	editor.update()
	menu.update()

	screen.blit(editor_surf, EDITOR_POS)
	screen.blit(menu_surf, MENU_POS)
	screen.blit(tile_ch_surf, TILE_CH_POS)

	pygame.display.flip()