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

editor_size = [TILE_SIZE[0] * COLS + TILE_CH_WIDTH, TILE_SIZE[1] * ROWS + MENU_HEIGHT]

if editor_size[0] < WIN_WIDTH:
	editor_size[0] = EDITOR_WIDTH
if editor_size[1]< WIN_HEIGHT:
	editor_size[1] = EDITOR_HEIGHT

editor_surf = pygame.Surface(editor_size)
menu_surf = pygame.Surface((MENU_WIDTH, MENU_HEIGHT))
tile_ch_surf = pygame.Surface((TILE_CH_WIDTH, TILE_CH_HEIGHT))  # tile_ch -- tile_chooser

editor = Editor(editor_surf, tile_color=(100, 100, 100))
editor.draw_tiles(ROWS, COLS, TILE_SIZE)
editor_pos = EDITOR_POS

tile_ch = TileChooser(tile_ch_surf, TILE_CH_POS, tiles_in_row=TILES_IN_ROW)
tile_ch.load_images("tiles")
tile_ch_pos = TILE_CH_POS

# change tile chooser height
tile_ch_surf = pygame.transform.scale(tile_ch_surf, (tile_ch_surf.get_width(), tile_ch.calculate_new_height()))
tile_ch.set_new_surface(tile_ch_surf)

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

		if event.type == pygame.MOUSEWHEEL:
			if event.y > 0:
				d = 1
			if event.y < 0:
				d = -1

			if pygame.key.get_mods() & pygame.KMOD_SHIFT:
				tile_ch.zoom(-d)
			elif pygame.key.get_mods() & pygame.KMOD_CTRL:
				editor.zoom(d)
			else:
				tile_ch_pos = tile_ch.scroll(d * TILE_CH_SCROLL_SPEED, WIN_HEIGHT)


	keys = pygame.key.get_pressed()
	dx, dy = 0, 0
	if keys[pygame.K_w]:
		dy = 1
	elif keys[pygame.K_s]:
		dy = -1
	else:
		dy = 0

	if keys[pygame.K_a]:
		dx = 1
	elif keys[pygame.K_d]:
		dx = -1
	else:
		dx = 0

	editor_pos = editor.move(dx * EDITOR_MOVE_SPEED, dy * EDITOR_MOVE_SPEED, WIN_WIDTH, WIN_HEIGHT)

	menu_surf.fill(pygame.Color("darkcyan"))

	editor.update(mouse_buttons)
	tile_ch.update(editor, mouse_buttons)
	menu.update()

	screen.blit(editor_surf, editor_pos)
	screen.blit(menu_surf, MENU_POS)
	screen.blit(tile_ch_surf, tile_ch_pos)

	fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, (255, 255, 255))
	screen.blit(fps_text, (0, 0))

	pygame.display.flip()

	clock.tick(FPS)