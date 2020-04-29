#! /usr/bin/env python3
# coding: utf-8

import pygame

from structure import Game


def main():

	game = Game()
	screen, mac_gyver = game.start()

	running = True

	while running:

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
					mac_gyver.move(event.key, game.map)

	pygame.quit()


if __name__ == "__main__":
	main()
