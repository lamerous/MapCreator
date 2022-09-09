import pygame
from editor import Editor
from menu import Menu
from tile import Tile
from tile_chooser import TileChooser
from settings import *

pygame.init()

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption(WIN_TITLE)

clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)


editor_surf = pygame.Surface((EDITOR_WIDTH, EDITOR_HEIGHT))
menu_surf = pygame.Surface((MENU_WIDTH, MENU_HEIGHT))
tile_ch_surf = pygame.Surface((TILE_CH_WIDTH, TILE_CH_HEIGHT))  # tile_ch -- tile_chooser

editor = Editor(editor_surf)
editor.draw_tiles(5, 10, TILE_SIZE)

tile_ch = TileChooser(tile_ch_surf)
tile_ch.load_images("tiles", TILES_IN_ROW)

menu = Menu(menu_surf)

run = True

while run:
	# 1 - left mouse buttonm 2 - center mouse button, 3 - right mouse button
	mouse_buttons = {1: False, 2: False, 3: False}

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			run = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_buttons[event.button] = True

	#editor_surf.fill(pygame.Color("darkred"))
	#menu_surf.fill(pygame.Color("darkorange"))
	#tile_ch_surf.fill(pygame.Color("darkgreen"))

	editor.update(mouse_buttons)
	menu.update()

	screen.blit(editor_surf, EDITOR_POS)
	screen.blit(menu_surf, MENU_POS)
	screen.blit(tile_ch_surf, TILE_CH_POS)

	fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, (255, 255, 255))
	screen.blit(fps_text, (0, 0))

	pygame.display.flip()

	clock.tick(FPS)