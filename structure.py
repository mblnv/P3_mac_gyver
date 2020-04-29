#! /usr/bin/env python3
# coding: utf-8

import os
import random

import pygame


class Map:

	NUMBER_OF_SPRITES_IN_WIDTH = 15
	NUMBER_OF_SPRITES_IN_HEIGHT = 15

	def __init__(self):
		self.structure = self._initialize_structure()
		self.screen = self._initialize_screen()
		self.walls = pygame.sprite.Group()
		self.guardians = pygame.sprite.Group()
		self.players = pygame.sprite.Group()
		self.floors = pygame.sprite.Group()
		self.objects = pygame.sprite.Group()
		self.number_of_objects = 3

	def _initialize_structure(self):

		file = open('map.txt', 'r')
		structure = file.read().split("\n")
		for i in range(len(structure)):
			structure[i] = structure[i].split(',')

		return structure

	def _initialize_screen(self):
		screen = pygame.display.set_mode(
			(self.NUMBER_OF_SPRITES_IN_WIDTH * Item.WIDTH, self.NUMBER_OF_SPRITES_IN_HEIGHT * Item.HEIGHT))
		pygame.display.set_caption("Help Mac Gyver to get out !")

		return screen

	def initialize_sprites(self, screen):

		for i in range(len(self.structure)):
			for j in range(len(self.structure[i])):
				if self.structure[i][j] == '1':
					wall = Item(j, i, 'images/wall.png', self.walls)
					wall.update(screen)
				elif self.structure[i][j] == 'G':
					floor = Item(j, i, 'images/floor.png')
					floor.update(screen)
					guardian = Item(j, i, 'images/guardian.png', self.guardians)
					guardian.update(screen)
				elif self.structure[i][j] == 'P':
					floor = Item(j, i, 'images/floor.png')
					floor.update(screen)
					player = Player(j, i, 'images/mac_gyver.png', self.players)
					player.update(screen)
				else:
					floor = Item(j, i, 'images/floor.png', self.floors)
					floor.update(screen)

		list_of_floor_sprites = self.floors.sprites()

		for k in range(self.number_of_objects):
			random_number = random.randrange(0, len(self.floors))
			object = Object(list_of_floor_sprites[random_number].position.x_index,
							list_of_floor_sprites[random_number].position.y_index,
							self.list_of_images_paths()[k], self.floors)
			self.floors.remove(list_of_floor_sprites[random_number])
			self.structure[object.position.y_index][object.position.x_index] = 'OBJ'
			object.update(screen)

		return screen, player

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
		new_image = pygame.transform.scale(new_image, (Item.WIDTH, Item.HEIGHT))

		return new_image


class Position:

	def __init__(self, x, y):
		self.x_index = x
		self.y_index = y

	def to_pixels(self, n):
		return n * Item.WIDTH


class Item(pygame.sprite.Sprite):

	WIDTH = 32
	HEIGHT = 32

	def __init__(self, x, y, path, *groups):
		super().__init__(*groups)
		self.position = Position(x, y)
		self.image = Image(path)

	def update(self, screen):
		screen.blit(self.image.sprite_image, (self.position.to_pixels(self.position.x_index), self.position.to_pixels(self.position.y_index)))
		pygame.display.update()


class Player(Item):

	def __init__(self, x, y, path, *groups):
		super().__init__(x, y, path, *groups)
		self.new_position = Position(0, 0)
		self.objects_count = 0
		self.velocity = Item.WIDTH

	def calculation_of_the_new_position(self, key):
		#import ipdb; ipdb.set_trace()
		x = self.position.x_index
		y = self.position.y_index
		tmp_position = Position(x, y)
		if key == pygame.K_LEFT:
			tmp_position.x_index -= 1
		elif key == pygame.K_RIGHT:
			tmp_position.x_index += 1
		elif key == pygame.K_UP:
			tmp_position.y_index -= 1
		elif key == pygame.K_DOWN:
			tmp_position.y_index += 1

		return tmp_position

	def is_move_authorized(self, map, tmp_position):
		#import ipdb; ipdb.set_trace()
		if (0 <= tmp_position.x_index <= Map.NUMBER_OF_SPRITES_IN_WIDTH - 1
				and 0 <= tmp_position.y_index <= Map.NUMBER_OF_SPRITES_IN_HEIGHT - 1
				and map.structure[tmp_position.y_index][tmp_position.x_index] != '1'):
			return True
		else:
			return False

	def move(self, key, map, screen):
		#import ipdb; ipdb.set_trace()
		tmp_position = self.calculation_of_the_new_position(key)
		move_authorized = self.is_move_authorized(map, tmp_position)
		if move_authorized:
			if map.structure[tmp_position.y_index][tmp_position.x_index] == '0':
				screen.blit(map.floors.sprites()[0].image.sprite_image,
							(self.position.to_pixels(self.position.x_index), self.position.to_pixels(self.position.y_index)))
				#import ipdb; ipdb.set_trace()
				self.position = tmp_position
				self.update(screen)
		#else:
			#self.new_position = self.position

class Object(Item):

	def __init__(self, x, y, path, *groups):
		super().__init__(x, y, path, *groups)


class Game:

	def __init__(self):
		self.map = Map()

	def start(self):
		screen, mac_gyver = self.map.initialize_sprites(self.map.screen)

		return screen, mac_gyver

if __name__ == "__main__":
	game = Game()
	game.start()
	pygame.time.delay(3000)