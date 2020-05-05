#! /usr/bin/env python3
# coding: utf-8

import os
import random

import pygame

import game
import items

""" This module creates the skeleton of the game and add visual elements on it.
	The skeleton is a structure with a form of a grid in 2 dimensions.
	This grid is materialized in a list of lists (map.structure).
	On each cell of the grid (i.e. each sprite), an image is displayed. This image can be a player, a guardian, 
	a wall, a floor or an item to pick-up.
	This module allow multiple players, multiple guardians and multiple pick-up items.
	By default, there is 1 player, 1 guardian, and 3 items to pick-up. """


class Image:
    """ Visual element to be displayed in a sprite / a cell of the structure. """

    def __init__(self, path):
        self.sprite_image = self.load_and_scale_image(path)

    def load_and_scale_image(self, path):
        """ Adapt the image given in the path to be displayed in a sprite. """
        new_image = pygame.image.load(path).convert_alpha()
        new_image = pygame.transform.scale(new_image, (items.MapObject.WIDTH, items.MapObject.HEIGHT))

        return new_image


class Position:
    """ Define a cell position in the structure (a list of lists which represents a grid) by its x and y indexes. """

    def __init__(self, x, y):
        self.x_index = x
        self.y_index = y

    def to_pixels(self, x, y):
        """ Convert a pair of indexes coordinates (position in the structure)
        into a pair of pixels coordinates (position on the screen). """

        return x * items.MapObject.WIDTH, y * items.MapObject.HEIGHT


class Map:
    """ Display a map with all its sprites : player(s), guardian(s), floors, walls and randomly displayed items. """

    NUMBER_OF_SPRITES_IN_WIDTH = 15
    NUMBER_OF_SPRITES_IN_HEIGHT = 15

    def __init__(self):
        self.structure = []  # A list of lists which represents the structural grid of the sprites. Access via indexes.
        self.screen = pygame.Surface

        self.player = None
        self.guardian = None
        self.floor = None
        self.wall = None

        self.players = set()
        self.guardians = set()
        self.floors = set()
        self.walls = set()
        self.items = set()

        self.number_of_objects = 3

    def initialize_structure(self):
        """ Create the structure (list of lists) from the file 'map.txt'. """
        file = open('map.txt', 'r', encoding='utf8')
        structure = file.read().split("\n")
        for i in range(len(structure)):
            structure[i] = structure[i].split(',')
        self.structure = structure
        file.close()

    def initialize_screen(self):
        """ Create the screen where the game will be displayed. """
        self.screen = pygame.display.set_mode(
            (self.NUMBER_OF_SPRITES_IN_WIDTH * items.MapObject.WIDTH,
             self.NUMBER_OF_SPRITES_IN_HEIGHT * items.MapObject.HEIGHT))
        pygame.display.set_caption("Help Mac Gyver to get out !")
        pygame.key.set_repeat(500, 20)

    def initialize_sprites(self):
        """ Add all the sprites - except pick-up items -  on the screen from the values stored in the structure.
         For each sprite, the image of the map object is displayed on the screen and the indexes of its position
         in the structure is added in the dedicated set. A floor background is also added for aesthetic purpose. """
        self.player = items.Player(0, 0, 'images/mac_gyver.png')
        self.guardian = items.MapObject(0, 0, 'images/guardian.png')
        self.floor = items.MapObject(0, 0, 'images/floor.png')
        self.wall = items.MapObject(0, 0, 'images/wall.png')

        for i in range(len(self.structure)):
            for j in range(len(self.structure[i])):
                if self.structure[i][j] == '1':
                    self.wall.position.x_index = j
                    self.wall.position.y_index = i
                    self.wall.update(self.screen)

                    self.walls.add((j, i,))

                else:
                    self.floor.position.x_index = j
                    self.floor.position.y_index = i
                    self.floor.update(self.screen)

                    if self.structure[i][j] == 'P':
                        self.player.position.x_index = j
                        self.player.position.y_index = i
                        self.player.update(self.screen)

                        self.players.add((j, i,))

                    elif self.structure[i][j] == 'G':
                        self.guardian.position.x_index = j
                        self.guardian.position.y_index = i
                        self.guardian.update(self.screen)

                        self.guardians.add((j, i,))

                    else:
                        self.floors.add((j, i,))

    def display_items_randomly(self):
        """ Add randomly arranged pick-up items on the screen. """
        list_of_floors = list(self.floors)
        for k in range(self.number_of_objects):
            random_number = random.randint(0, len(list_of_floors) - 1)
            x, y = list_of_floors[random_number][0], list_of_floors[random_number][1]
            item = items.MapObject(x, y, self.list_of_images_paths()[k])
            self.items.add((x, y))
            self.floors.discard((x, y))
            list_of_floors.pop(random_number)
            item.update(self.screen)

    def list_of_images_paths(self):
        """ Browse the file 'images/objects' and create a list with all the PNG images contained in it. """
        list_of_images_paths = []
        for file_name in os.listdir('images/objects'):
            if file_name.endswith('.png'):
                list_of_images_paths.append('images/objects/' + file_name)

        return list_of_images_paths


if __name__ == "__main__":
    new_game = game.Game()
    new_game.start()
    pygame.time.delay(3000)
