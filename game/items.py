#! /usr/bin/env python3
# coding: utf-8

import pygame

import game.structure

""" This module defines the types of objects which can be displayed on the map.
    At the minimum, an object can be defined by its position in the structure
    (with indexes) and its image. The player inherits of these minimum
    characteristics and also have the possibility to move."""


class MapObject:
    """ A basic object of the map which can be displayed on the screen. """
    WIDTH = 32
    HEIGHT = 32

    def __init__(self, x, y, path):
        self.position = game.structure.Position(x, y)
        self.image = game.structure.Image(path)

    def update(self, screen):
        """ Display a map object on the screen. """
        screen.blit(
            self.image.sprite_image,
            (self.position.to_pixels(
                self.position.x_index,
                self.position.y_index)))
        pygame.display.update()


class Player(MapObject):
    """ Child of the MapObject class. Allow the player to move on
        allowed positions. """

    def __init__(self, x, y, path):
        super().__init__(x, y, path)
        self.items_count = 0
        self.end_game = False

    def move(self, key, map):
        """ Determine the new move of the player and associated actions
            up to the context. """
        new_position = self.calculation_of_the_new_position(key)
        move_authorized = self.is_move_authorized(map, new_position)
        if move_authorized:
            map.screen.blit(
                map.floor.image.sprite_image,
                (self.position.to_pixels(
                    self.position.x_index,
                    self.position.y_index)))
            self.position = new_position
            self.update(map.screen)

            if (new_position.x_index, new_position.y_index) in map.items:
                self.items_count += 1
                map.items.remove((
                    new_position.x_index,
                    new_position.y_index))

            elif (new_position.x_index, new_position.y_index) in map.guardians:
                if self.items_count == map.number_of_objects:
                    new_image = pygame.image.load(
                        'images/you_win.jpg').convert_alpha()

                else:
                    new_image = pygame.image.load(
                        'images/you_die.jpg').convert_alpha()

                self.end_game = True
                new_image = pygame.transform.scale(
                    new_image,
                    map.screen.get_size())
                map.screen.blit(new_image, (0, 0))
                pygame.display.update()

    def calculation_of_the_new_position(self, key):
        """ From the key pressed by the user, calculation of the possible
            new position of the player in the structure. """
        x = self.position.x_index
        y = self.position.y_index
        new_position = game.structure.Position(x, y)
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
        """ Determine whether the move to the new position is possible. """
        if ((new_position.x_index, new_position.y_index) not in map.walls
                and (0 <= new_position.x_index <=
                     game.structure.Map.NUMBER_OF_SPRITES_IN_WIDTH)
                and (0 <= new_position.y_index <=
                     game.structure.Map.NUMBER_OF_SPRITES_IN_HEIGHT)
                and self.end_game is False):
            return True
        else:
            return False
