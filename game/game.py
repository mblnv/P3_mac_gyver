#! /usr/bin/env python3
# coding: utf-8

import game.structure

""" This module allow to launch a new game with the construction of a map and all its components. 
    After creating an instance of Game, the new game is ready to be played."""


class Game:
    """ Define the game itself. It begins with the creation of a map in the constructor. """

    def __init__(self):
        self.map = game.structure.Map()

    def start(self):
        """ Launch the game by displaying all visual elements of the map. """
        self.map.initialize_structure()
        self.map.initialize_screen()
        self.map.initialize_sprites()
        self.map.display_items_randomly()
