from Settings.Game import *
from Map import Block


class Map:
    def __init__(self, width=Display_blocks[0]*2, height=Display_blocks[1]*2, display=None):
        self.width = width
        self.height = height
        self.grid = Block.initialize(self.width, self.height)
        if display is not None:
            self.display = display
        else:
            x = (width - Display_blocks[0]) / 2
            y = (height - Display_blocks[1]) / 2
            self.display = [x, y]
        self.corner = {'horizontal': 0, 'vertical': 0}

    def update_status(self, status):
        x = self.display[0]
        while x < self.display[0] + Display_blocks[0]:
            X = int(x)
            y = self.display[1]
            while y < self.display[1] + Display_blocks[1]:
                Y = int(y)
                status.append([self.grid[Y][X].image, ((X - self.display[0]) * 50, (Y - self.display[1]) * 50)])
                y += 1
            x += 1

    def moveup(self, status):
        if self.display[1] <= 0:
            self.display[1] = 0
            self.corner['vertical'] -= 0.1
            if self.corner['vertical'] <= -(Display_blocks[1] / 2):
                self.corner['vertical'] = -(Display_blocks[1] / 2)
            self.update_status(status)
            return True
        elif self.corner['vertical'] > 0:
            self.corner['vertical'] -= 0.1
            self.update_status(status)
            return True
        self.display[1] -= 0.1
        self.update_status(status)
        return False

    def movedown(self, status):
        if self.display[1] >= (self.height - Display_blocks[1]):
            self.display[1] = self.height - Display_blocks[1]
            self.corner['vertical'] += 0.1
            if self.corner['vertical'] >= (Display_blocks[1] / 2):
                self.corner['vertical'] = (Display_blocks[1] / 2)
            self.update_status(status)
            return True
        elif self.corner['vertical'] < 0:
            self.corner['vertical'] += 0.1
            self.update_status(status)
            return True
        self.display[1] += 0.1
        self.update_status(status)
        return False

    def moveleft(self, status):
        if self.display[0] <= 0:
            self.display[0] = 0
            self.corner['horizontal'] -= 0.1
            if self.corner['horizontal'] <= int(-Display_blocks[1] / 2):
                self.corner['horizontal'] = int(-Display_blocks[1] / 2)
            self.update_status(status)
            return True
        elif self.corner['horizontal'] > 0:
            self.corner['horizontal'] -= 0.1
            self.update_status(status)
            return True
        self.display[0] -= 0.1
        self.update_status(status)
        return False

    def moveright(self, status):
        if self.display[0] >= self.width - Display_blocks[0]:
            self.display[0] = self.width - Display_blocks[0]
            self.corner['horizontal'] += 0.1
            if self.corner['horizontal'] >= (Display_blocks[1] / 2):
                self.corner['horizontal'] = (Display_blocks[1] / 2)
            self.update_status(status)
            return True
        elif self.corner['horizontal'] < 0:
            self.corner['horizontal'] += 0.1
            self.update_status(status)
            return True
        self.display[0] += 0.1
        self.update_status(status)
        return False

    def stay(self, status):
        self.update_status(status)
        return False
