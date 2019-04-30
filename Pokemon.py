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
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
from Settings.Game import *
from Settings.Colors import *


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

    while True:  # Main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                quitgame()
        surface.fill(Light_green)
        img = pygame.image.load('player.png')
        surface.blit(img, (Display_size[0]/2, Display_size[1]/2))
        pygame.display.update()
        tick()

    pass


if __name__ == '__main__':
    main()
