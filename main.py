#! /usr/bin/env python3
# coding: utf-8

import pygame

import structure


def main():

	screen, list_of_all_sprites, mac_gyver, current_position_of_mac_gyver, mac_gyver_start_index = structure.display_map()

	# Dimensions of Mac Gyver
	mac_gyver_rect = mac_gyver.get_rect()
	x = current_position_of_mac_gyver.x
	y = current_position_of_mac_gyver.y

	# Position of Mac Gyver
	# for sprite in list_of_all_sprites:
	# 	if sprite.type == "mac_gyver":
	# 		x = sprite.position.x
	# 		y = sprite.position.y
	# 		index_of_mac_gyver = list_of_all_sprites.index(sprite)
	# 		# ajouter une sortie de boucle

	#import ipdb; ipdb.set_trace()
	#current_position_of_mac_gyver = structure.Position(x, y)

	velocity = 32

	run = True

	while run:

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				run = False
			
			elif event.type == pygame.KEYDOWN:
				
				#import ipdb; ipdb.set_trace()
				screen.fill((0,0,0), ((current_position_of_mac_gyver.x, current_position_of_mac_gyver.y), (32, 32)))
				
				if event.key == pygame.K_LEFT and x >= velocity:
					x -= velocity
				elif event.key == pygame.K_RIGHT and x < (screen.get_width() - mac_gyver_rect.width):
					x += velocity
				elif event.key == pygame.K_UP and y > velocity:
					y -= velocity
				elif event.key == pygame.K_DOWN and y < (screen.get_height() - mac_gyver_rect.height):
					y += velocity
			
				#import ipdb; ipdb.set_trace()
				new_position_of_mac_gyver = structure.Position(x, y)
				authorized_move = False	
				
				for sprite in list_of_all_sprites:
					
					if new_position_of_mac_gyver.x == sprite.position.x \
						and new_position_of_mac_gyver.y == sprite.position.y \
						and sprite.type == "":
						
						authorized_move = True
						break

					else:
						authorized_move = False


				if authorized_move:

						list_of_all_sprites[mac_gyver_start_index].type = ""

						
						screen.blit(mac_gyver, (new_position_of_mac_gyver.x, new_position_of_mac_gyver.y))
						pygame.display.update()

						current_position_of_mac_gyver = new_position_of_mac_gyver

				else:
						x = current_position_of_mac_gyver.x
						y = current_position_of_mac_gyver.y

		# vérifier la fonction delay et son emplacement avec zestedesavoir
		pygame.time.delay(100)

	pygame.quit()


if __name__ == "__main__":
    main()