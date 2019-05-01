from Settings.Game import *
from Map import Block


class Map():
    def __init__(self, width=Display_blocks[0] * 9, heigth=Display_blocks[1] * 9, display=None):
        self.width = width
        self.heigth = heigth
        self.grid = Block.initialize(self.width, self.heigth)
        if display != None:
            self.display = display
        else:
            x = (width - Display_blocks[0]) / 2
            y = (heigth - Display_blocks[1]) / 2
            self.display = [x, y]

    def update_status(self, status):
        x = self.display[0]
        while x <= self.display[0] + Display_blocks[0]:
            X = int(x)
            y = self.display[1]
            while y <= self.display[1] + Display_blocks[1]:
                Y = int(y)
                status.append([self.grid[Y][X].image, ((X - self.display[0]) * 50, (Y - self.display[1]) * 50)])
                y += 1
            x += 1

    def moveup(self, status):
        self.display[1] -= 0.1
        self.update_status(status)

    def movedown(self, status):
        self.display[1] += 0.1
        self.update_status(status)

    def moveleft(self, status):
        self.display[0] -= 0.1
        self.update_status(status)

    def moveright(self, status):
        self.display[0] += 0.1
        self.update_status(status)

    def stay(self, status):
        self.update_status(status)
