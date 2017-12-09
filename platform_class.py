######################################################################
# Author: Rodney Grant
# Username: GrantR
#
# Assignment: P0_Final
#
# Purpose: To demonstrate my knowledge of programming
# ######################################################################
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
    def solid(self, x, y):
        #floor = 504
        if self.x < x < (self.x + self.length) and y <= self.y:
            floor = self.y
            #print(True)
        else:
            floor = 504
        return floor

    """Draws the floor on screen"""
    def draw(self, colour, width):
        pygame.draw.line(self.canvas, colour, self.start(), self.end(), width)