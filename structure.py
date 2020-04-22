#! /usr/bin/env python3
# coding: utf-8

import pygame


class Sprite:

	SPRITE_WIDTH = 32
	SPRITE_HEIGHT = 32

	NUMBER_OF_SPRITES_IN_WIDTH = 15
	NUMBER_OF_SPRITES_IN_HEIGHT = 15

	def __init__(self, position, type):
		self.position = position
		# self.width = SPRITE_WIDTH
		# self.height = SPRITE_HEIGHT
		self.type = type


class Position:

	def __init__(self, x, y):
		self.x = x
		self.y = y


def initialize_screen():

	screen = pygame.display.set_mode((Sprite.NUMBER_OF_SPRITES_IN_WIDTH * Sprite.SPRITE_WIDTH, Sprite.NUMBER_OF_SPRITES_IN_HEIGHT * Sprite.SPRITE_HEIGHT))

	pygame.display.set_caption("Help Mac Gyver to get out !")

	return screen


def initialize_structure():

	list_of_all_sprites = []
	list_of_all_walls = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 27, 30, 31, 32, 33, 35, 37, 38, 39, 40, 41, 42, 44, 45, 59, 60, 62, 63, 64, 65, 66, 68, 69, 70, 71, 72, 74, 75, 77, 81, 85, 89, 90, 92, 94, 96, 98, 100, 102, 103, 104, 105, 107, 109, 110, 111, 113, 115, 117, 119, 120, 122, 124, 128, 130, 132, 134, 135, 137, 141, 143, 145, 149, 150, 152, 153, 154, 155, 156, 158, 160, 162, 164, 165, 173, 177, 179, 180, 182, 183, 184, 186, 187, 188, 190, 191, 192, 194, 201, 207, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224]
	guardian_index = 29
	mac_gyver_start_index = 195

	for i in range(Sprite.NUMBER_OF_SPRITES_IN_WIDTH * Sprite.NUMBER_OF_SPRITES_IN_HEIGHT):
		position = Position(i % Sprite.NUMBER_OF_SPRITES_IN_WIDTH * Sprite.SPRITE_WIDTH, i // Sprite.NUMBER_OF_SPRITES_IN_WIDTH * Sprite.SPRITE_HEIGHT)
		if i == guardian_index:
			list_of_all_sprites.append(Sprite(position, "guardian"))
		elif i in list_of_all_walls:
			list_of_all_sprites.append(Sprite(position, "wall"))
		elif i == mac_gyver_start_index:
			list_of_all_sprites.append(Sprite(position, "mac_gyver"))
		else:
			list_of_all_sprites.append(Sprite(position, ""))

	return list_of_all_sprites


def add_sprite_images(screen, list_of_all_sprites):

	# Wall image
	wall = pygame.image.load('Wall.png').convert_alpha()
	wall = pygame.transform.scale(wall, (Sprite.SPRITE_WIDTH, Sprite.SPRITE_HEIGHT))

	# Guardian image
	guardian = pygame.image.load('Guardian.png').convert_alpha()
	guardian = pygame.transform.scale(guardian, (Sprite.SPRITE_WIDTH, Sprite.SPRITE_HEIGHT))

	# MacGyver image
	mac_gyver = pygame.image.load('MacGyver.png').convert_alpha()
	mac_gyver = pygame.transform.scale(mac_gyver, (Sprite.SPRITE_WIDTH, Sprite.SPRITE_HEIGHT))

	for sprite in list_of_all_sprites:
		if sprite.type == "wall":
			screen.blit(wall, (sprite.position.x, sprite.position.y))
		elif sprite.type == "guardian":
			screen.blit(guardian, (sprite.position.x, sprite.position.y))
		elif sprite.type == "mac_gyver":
			screen.blit(mac_gyver, (sprite.position.x, sprite.position.y))
			mac_gyver_position = Position(sprite.position.x, sprite.position.y)
			# à revoir. Définir la variable en global sur le module ?
			mac_gyver_start_index = list_of_all_sprites.index(sprite)

	return mac_gyver, mac_gyver_position, mac_gyver_start_index


def display_map():
	pygame.init()
	screen = initialize_screen()
	list_of_all_sprites = initialize_structure()
	mac_gyver, mac_gyver_position, mac_gyver_start_index = add_sprite_images(screen, list_of_all_sprites)
	pygame.display.update()
	# vérifier la fonction delay et son emplacement avec zestedesavoir
	pygame.time.delay(100)
	return screen, list_of_all_sprites, mac_gyver, mac_gyver_position, mac_gyver_start_index


if __name__ == "__main__":
	display_map()


	# =====================================
	# Vérification OVI - A EFFACER A LA FIN
	# =====================================
	# print("longueur de ma liste : ", len(list_of_all_sprites))
	# for sprite in list_of_all_sprites:
	# 	if list_of_all_sprites.index(sprite) < 200:
	# 		print('[', list_of_all_sprites.index(sprite), ']', sprite.position.x, sprite.position.y, sprite.type, Sprite.SPRITE_WIDTH, Sprite.SPRITE_HEIGHT)
			

