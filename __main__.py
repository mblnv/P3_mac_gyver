#! /usr/bin/env python3
# coding: utf-8

import pygame

import game.game


def main():
    new_game = game.game.Game()
    new_game.start()

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key in [
                    pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN
                ]:
                    new_game.map.player.move(event.key, new_game.map)

    pygame.quit()


if __name__ == "__main__":
    main()
