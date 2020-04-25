#! /usr/bin/env python3
# coding: utf-8

import pygame

from structure import Game


def main():

	game = Game()
	game.start()

	running = True

	while running:

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				pass

	pygame.quit()


if __name__ == "__main__":
	main()
