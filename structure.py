#! /usr/bin/env python3
# coding: utf-8

import os
import random
import pygame


class Map:

	NUMBER_OF_SPRITES_IN_WIDTH = 15
	NUMBER_OF_SPRITES_IN_HEIGHT = 15

	def __init__(self):
		self.structure = []  # A list of lists which represents the structural grid of the sprites. Access through indexes.
		self.screen = pygame.Surface

		self.player = None
		self.guardian = None
		self.floor = None
		self.wall = None

		self.walls = set()
		self.guardians = set()
		self.players = set()
		self.floors = set()
		self.items = set()

		self.number_of_objects = 3

	def initialize_structure(self):

		file = open('map.txt', 'r')
		structure = file.read().split("\n")
		for i in range(len(structure)):
			structure[i] = structure[i].split(',')
		self.structure = structure

	def initialize_screen(self):
		self.screen = pygame.display.set_mode(
			(self.NUMBER_OF_SPRITES_IN_WIDTH * MapObject.WIDTH, self.NUMBER_OF_SPRITES_IN_HEIGHT * MapObject.HEIGHT))
		pygame.display.set_caption("Help Mac Gyver to get out !")

	def initialize_sprites(self):

		self.player = Player(0, 0, 'images/mac_gyver.png')
		self.guardian = MapObject(0, 0, 'images/guardian.png')
		self.floor = MapObject(0, 0, 'images/floor.png')
		self.wall = MapObject(0, 0, 'images/wall.png')

		for i in range(len(self.structure)):
			for j in range(len(self.structure[i])):
				if self.structure[i][j] == '1':
					# Add the image of the wall
					self.wall.position.x_index = j
					self.wall.position.y_index = i
					self.wall.update(self.screen)
					# Add the tuple of the index coordinates in the dedicated set
					self.walls.add((j, i,))

				elif self.structure[i][j] == 'G':
					# Add the floor background for aesthetic purpose
					self.floor.position.x_index = j
					self.floor.position.y_index = i
					self.floor.update(self.screen)
					# Add the image of the guardian
					self.guardian.position.x_index = j
					self.guardian.position.y_index = i
					self.guardian.update(self.screen)
					# Add the tuple of the index coordinates in the dedicated set
					self.guardians.add((j, i,))

				elif self.structure[i][j] == 'P':
					# Add the floor background for aesthetic purpose
					self.floor.position.x_index = j
					self.floor.position.y_index = i
					self.floor.update(self.screen)
					# Add the image of the player (Mac Gyver)
					self.player.position.x_index = j
					self.player.position.y_index = i
					self.player.update(self.screen)
					# Add the tuple of the index coordinates in the dedicated set
					self.players.add((j, i,))

				else:
					# Add the image of the floor
					self.floor.position.x_index = j
					self.floor.position.y_index = i
					self.floor.update(self.screen)
					# Add the tuple of the index coordinates in the dedicated set
					self.floors.add((j, i,))

		print('Mac Gyver : ', self.players)
		print('Guardian : ', self.guardians)
		print('Objets : ', self.items)
		print('walls : ', self.walls)
		print('Floors : ', self.floors)

		list_of_floors = list(self.floors)
		for k in range(self.number_of_objects):
			random_number = random.randint(0, len(list_of_floors) - 1)
			x, y = list_of_floors[random_number][0], list_of_floors[random_number][1]
			item = Item(x, y, self.list_of_images_paths()[k])
			self.items.add((x, y))
			self.floors.discard((x, y))
			list_of_floors.pop(random_number)
			item.update(self.screen)

	def list_of_images_paths(self):
		list_of_images_paths = []
		for file_name in os.listdir('images/objects'):
			if file_name.endswith('.png'):
				list_of_images_paths.append('images/objects/' + file_name)

		return list_of_images_paths


class Image:

	def __init__(self, path):
		self.sprite_image = self.load_and_scale_image(path)

	def load_and_scale_image(self, path):

		new_image = pygame.image.load(path).convert_alpha()
		new_image = pygame.transform.scale(new_image, (MapObject.WIDTH, MapObject.HEIGHT))

		return new_image


class Position:

	def __init__(self, x, y):
		self.x_index = x
		self.y_index = y

	def to_pixels(self, n):
		return n * MapObject.WIDTH


class MapObject():

	WIDTH = 32
	HEIGHT = 32

	def __init__(self, x, y, path, *groups):
		super().__init__(*groups)
		self.position = Position(x, y)
		self.image = Image(path)

	def update(self, screen):
		screen.blit(self.image.sprite_image, (self.position.to_pixels(self.position.x_index), self.position.to_pixels(self.position.y_index)))
		pygame.display.update()


class Player(MapObject):

	def __init__(self, x, y, path, *groups):
		super().__init__(x, y, path, *groups)
		self.items_count = 0

	def calculation_of_the_new_position(self, key):
		x = self.position.x_index
		y = self.position.y_index
		new_position = Position(x, y)
		if key == pygame.K_LEFT:
			new_position.x_index -= 1
		elif key == pygame.K_RIGHT:
			new_position.x_index += 1
		elif key == pygame.K_UP:
			new_position.y_index -= 1
		elif key == pygame.K_DOWN:
			new_position.y_index += 1

		return new_position

	def is_move_authorized(self, map, new_position):
		if (new_position.x_index, new_position.y_index) not in map.walls:
			return True
		else:
			return False

	def move(self, key, map):
		tmp_position = self.calculation_of_the_new_position(key)
		move_authorized = self.is_move_authorized(map, tmp_position)
		if move_authorized:
			map.screen.blit(
				map.floor.image.sprite_image,
				(self.position.to_pixels(self.position.x_index),
				 self.position.to_pixels(self.position.y_index)))
			self.position = tmp_position
			self.update(map.screen)

			if (tmp_position.x_index, tmp_position.y_index) in map.items:
				self.items_count += 1
				map.items.remove((tmp_position.x_index, tmp_position.y_index))
				print('nombre d objets ramassés : ', self.items_count)

			elif (tmp_position.x_index, tmp_position.y_index) in map.guardians:

				if self.items_count == 3:
					new_image = pygame.image.load('images/you_win.jpg').convert_alpha()

				else:
					new_image = pygame.image.load('images/you_die.jpg').convert_alpha()

				new_image = pygame.transform.scale(new_image, map.screen.get_size())
				map.screen.blit(new_image, (0, 0))
				pygame.display.update()


class Item(MapObject):

	def __init__(self, x, y, path, *groups):
		super().__init__(x, y, path, *groups)


class Game:

	def __init__(self):
		self.map = Map()

	def start(self):
		self.map.initialize_structure()
		self.map.initialize_screen()
		self.map.initialize_sprites()

		return self.map.screen, self.map.player


if __name__ == "__main__":
	game = Game()
	game.start()
	pygame.time.delay(3000)