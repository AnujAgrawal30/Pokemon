import pygame
import os
from Settings.Game import *
os.chdir(os.path.dirname(os.path.realpath(__file__)))


class Character:
    def __init__(self, name, location=[Display_size[0] / 2, Display_size[1] / 2], speed=5):
        self.speed = speed
        self.motion_pos = 0
        self.location = location
        os.getcwd()
        self.direction = {'up': 0, 'down': 0, 'right': 0, 'left': 0}
        self.motion = {'front': [pygame.image.load('../Assets/' + name + '/front_standing.png'),
                        pygame.image.load('../Assets/' + name + '/front_walking1.png'),
                        pygame.image.load('../Assets/' + name + '/front_walking2.png'),
                        pygame.image.load('../Assets/' + name + '/front_walking1.png'),
                        pygame.image.load('../Assets/' + name + '/front_standing.png'),
                        pygame.image.load('../Assets/' + name + '/front_walking-1.png'),
                        pygame.image.load('../Assets/' + name + '/front_walking-2.png'),
                        pygame.image.load('../Assets/' + name + '/front_walking-1.png')],
                        'back': [pygame.image.load('../Assets/' + name + '/back_standing.png'),
                        pygame.image.load('../Assets/' + name + '/back_walking1.png'),
                        pygame.image.load('../Assets/' + name + '/back_walking2.png'),
                        pygame.image.load('../Assets/' + name + '/back_walking1.png'),
                        pygame.image.load('../Assets/' + name + '/back_standing.png'),
                        pygame.image.load('../Assets/' + name + '/back_walking-1.png'),
                        pygame.image.load('../Assets/' + name + '/back_walking-2.png'),
                        pygame.image.load('../Assets/' + name + '/back_walking-1.png')],
                        'right': [pygame.image.load('../Assets/' + name + '/right_standing.png'),
                        pygame.image.load('../Assets/' + name + '/right_walking1.png'),
                        pygame.image.load('../Assets/' + name + '/right_walking2.png'),
                        pygame.image.load('../Assets/' + name + '/right_walking1.png')],
                        'left': [pygame.image.load('../Assets/' + name + '/left_standing.png'),
                        pygame.image.load('../Assets/' + name + '/left_walking1.png'),
                        pygame.image.load('../Assets/' + name + '/left_walking2.png'),
                        pygame.image.load('../Assets/' + name + '/left_walking1.png')]}

    def moveup(self, status):
        stat = [self.motion['back'][self.motion_pos], self.location]
        self.motion_pos += 1
        self.motion_pos %= 8
        print(self.motion_pos)
        status.append(stat)

    def movedown(self, status):
        stat = [self.motion['front'][self.motion_pos], self.location]
        self.motion_pos += 1
        self.motion_pos %= 8
        print(self.motion_pos)
        status.append(stat)

    def moveright(self, status):
        stat = [self.motion['right'][self.motion_pos], self.location]
        self.motion_pos += 1
        self.motion_pos %= 4
        print(self.motion_pos)
        status.append(stat)

    def moveleft(self, status):
        stat = [self.motion['left'][self.motion_pos], self.location]
        self.motion_pos += 1
        self.motion_pos %= 4
        print(self.motion_pos)
        status.append(stat)

    def move(self, status):
        if self.direction['up'] == 1:
            self.moveup(status)
        elif self.direction['down'] == 1:
            self.movedown(status)
        elif self.direction['right'] == 1:
            self.moveright(status)
        elif self.direction['left'] == 1:
            self.moveleft(status)
        else:
            stat = [self.motion['front'][0], self.location]
            print(self.motion_pos)
            status.append(stat)

