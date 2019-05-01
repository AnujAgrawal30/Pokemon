from pygame.image import load
# from copy import deepcopy
from random import random

Assets = {'grass': {'normal': load('../Assets/Map/grass_normal.png')},
          'blank': {'box': load('../Assets/Map/blank_box.png')}}


class Block:
    def __init__(self, image=None, size=(50, 50), alpha=255):
        self.size = size
        self.alpha = alpha
        if image is None:
            if random() > 0.5:
                self.image = Assets['grass']['normal']
            else:
                self.image = Assets['blank']['box']
        else:
            self.image = Assets[image.split(' ')[0]][image.split(' ')[1]]


def initialize(width=1, height=1):
    grid = []
    for i in range(height):
        row = []
        for j in range(width):
            row += list([Block()])
        grid += list([row])
    return grid
