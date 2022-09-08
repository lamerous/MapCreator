# -*- coding: cp1251 -*-

from PIL import Image
from os import system, mkdir
import sys

def progress_bar(title, progress, total):
	percent = 100 * (progress / float(total))
	bar = '█' * int(percent) + '-' * (100 - int(percent))
	print(f"\r{title} |{bar}| {percent:.2f}", end="\r")

# check for correct arguments
if len(sys.argv) != 5 and len(sys.argv) != 4:
	print("Syntax: tilesets_to_images.py (tile_path) (width) (height) (folder)\n")
	print("tile_path     - path to tileset")
	print("sprite_width  - width of one sprite")
	print("sprite_height - height of one sprite")
	print("folder        - folder to save sprites (left empty for save to the current folder)")
	raise SystemExit(1)

# opening file for start work with them
try:
	filename = sys.argv[1]
	tile_image = Image.open(filename)
except FileNotFoundError:
	print("Can't open", filename)
	raise SystemExit(1)

# getting sprite size
try:
	sprite_width = int(sys.argv[2])
	sprite_height = int(sys.argv[3])
except:
	print("Wrong size")
	raise SystemExit(1)

# checking folder, cause pillow can't save file to the non-exsistent folder
folder = ""
if len(sys.argv) == 5:
	folder = sys.argv[4] + '/'
	try:
		mkdir(folder)
	except:
		pass

count_iterations = 0
count_width_sprites = tile_image.size[0]//sprite_width
count_height_sprites = tile_image.size[1]//sprite_height 
total_sprites = count_width_sprites * count_height_sprites

progress_bar("Progress: ", 0, total_sprites)

# cut and save sprites
for i in range(count_width_sprites):
	for j in range(count_height_sprites):
		sprite = tile_image.crop((sprite_width*i, sprite_height*j, sprite_width*i+sprite_width, sprite_height*j+sprite_height))
		sprite.save(f"{folder}sprite{count_iterations}.png", quality=100)
		count_iterations += 1
		progress_bar("Progress: ", count_iterations, total_sprites)

print("\nScript finished")
print(f"Files created: {count_iterations}/{total_sprites}")