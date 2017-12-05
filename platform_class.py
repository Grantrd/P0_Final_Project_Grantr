from hero_class import*
from pygame import *


class Platform:
    def __init__(self, x, y, length, display_height, floor, z, m, canvas):
        self.x = x
        self.y = y
        self.length = length
        self.height = display_height
        self.floor = floor
        self.z = z
        self.m = m
        self.canvas = canvas

    def start(self):
        return ((self.x + 70), (self.y + 85))

    def end(self):
        return ((self.x + self.length + 15), (self.y + 85))

    def solid(self):
        if self.z < self.x:
            self.floor = int(self.height * 0.78)
        elif self.z > (self.x + self.length):
            self.floor = int(self.height * 0.78)
        elif self.m > self.y:
            self.floor = int(self.height * 0.78)
        else:
            self.floor = self.y
        return self.floor

    def draw(self, colour, width):
        pygame.draw.line(self.canvas, colour, self.start(), self.end(), width)
