# window
WIN_WIDTH = 1280
WIN_HEIGHT = 720
WIN_TITLE = "Map Creator"

# editor
EDITOR_WIDTH = WIN_WIDTH / 1.2
EDITOR_HEIGHT = WIN_HEIGHT / 1.2
EDITOR_POS = (0, 0)    # start position
EDITOR_MOVE_SPEED = 10

# menu
MENU_WIDTH = WIN_WIDTH / 1.2
MENU_HEIGHT = WIN_HEIGHT - EDITOR_HEIGHT
MENU_POS = (0, EDITOR_HEIGHT)     # start position

# tile chooser
TILE_CH_WIDTH = WIN_WIDTH - EDITOR_WIDTH   # tile_ch -- tile chooser
TILE_CH_HEIGHT = WIN_HEIGHT
TILE_CH_POS = [EDITOR_WIDTH, 0]    # start position
TILE_CH_SCROLL_SPEED = 50
TILES_IN_ROW = 4


# tiles
ROWS = 20
COLS = 20
TILE_SIZE = [64, 64]

FPS = 30