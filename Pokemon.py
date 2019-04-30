""" This is a Pokemon sort of game where the player roams in an open world fighting enemies and stuff.
 We have IDK what right now
 TODO - Make a simple light green background and move it wrt the player
 TODO - animate the character moving style
 TODO - Make the grass and its random occurrence in the ground
 TODO - Make enemies either in grass or in person (and other characters)
 TODO - Make the interface for interaction with the gamer
 TODO - Make the game a bit different from Pokemon or add class of Pokemon and create levels
 TODO - Come up with a storyline """

import pygame
from pygame.locals import *
import sys
from Settings.Game import *
from Settings.Colors import *
from Character import Character


def main():
    def tick():
        fps_clock.tick(FPS)

    def quitgame():
        pygame.quit()
        sys.exit()

    pygame.init()
    surface = pygame.display.set_mode(Display_size)
    pygame.display.set_caption(caption)
    fps_clock = pygame.time.Clock()
    player = Character.Character('Player')
    temp = pygame.image.load('../Assets/' + 'Player' + '/front_standing.png')

    while True:  # Main game loop
        status = []
        for event in pygame.event.get():
            if event.type == QUIT:
                quitgame()
            elif event.type == KEYDOWN:
                if (event.key == K_UP) | (event.key == K_w):
                    player.direction['up'] = 1
                elif (event.key == K_DOWN) | (event.key == K_s):
                    player.direction['down'] = 1
                elif (event.key == K_RIGHT) | (event.key == K_d):
                    player.direction['right'] = 1
                elif (event.key == K_LEFT) | (event.key == K_a):
                    player.direction['left'] = 1
            elif event.type == KEYUP:
                if (event.key == K_UP) | (event.key == K_w):
                    player.direction['up'] = 0
                elif (event.key == K_DOWN) | (event.key == K_s):
                    player.direction['down'] = 0
                elif (event.key == K_RIGHT) | (event.key == K_d):
                    player.direction['right'] = 0
                elif (event.key == K_LEFT) | (event.key == K_a):
                    player.direction['left'] = 0
        player.move(status)
        surface.fill(Light_green)
        for stat in status:
            surface.blit(stat[0], (Display_size[0]/2, Display_size[1]/2))
        pygame.display.update()
        tick()

    pass


if __name__ == '__main__':
    main()
