import pygame
pygame.image.load('../player.png')


class Character:
    def __init__(self, name):
        self.motion = [pygame.image.load('../assets/' + name + 'standing'),
                        pygame.image.load('../assets/' + name + 'walking1'),
                        pygame.image.load('../assets/' + name + 'walking2'),
                        pygame.image.load('../assets/' + name + 'walking1'),
                        pygame.image.load('../assets/' + name + 'standing'),
                        pygame.image.load('../assets/' + name + 'walking-1'),
                        pygame.image.load('../assets/' + name + 'walking-2'),
                        pygame.image.load('../assets/' + name + 'walking-1')]
        # self.health = 100
        
    pass

