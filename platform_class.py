from hero_class import*
from pygame import *


class Platform:
    def __init__(self, x, y, length, canvas):
        self.x = x
        self.y = y
        self.length = length
        self.canvas = canvas
        self.draw((130, 130, 130), 5)
    """sets the starting point of drawing it"""
    def start(self):
        return ((self.x + 70), (self.y + 85))

    """sets the end point of drawing it"""
    def end(self):
        return ((self.x + self.length + 15), (self.y + 85))

    """Makes the floor solid"""
    def solid(self, x, y, height):
        newfloor = int(height * .84)
        is_solid = False
        if y <= self.y and self.x <= x <= (self.x + self.length):
            newfloor = self.y
            is_solid = True
        elif self.x >= x or x >= (self.x + self.length) or y > self.y:
            newfloor = int(height * .84)
            is_solid = False
        return is_solid, newfloor

    """Draws the floor on screen"""
    def draw(self, colour, width):
        pygame.draw.line(self.canvas, colour, self.start(), self.end(), width)