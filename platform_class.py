from hero_class import*
from pygame import *


class Platform:
    def __init__(self, x, y, length, display_height, floor, z, m):
        self.x = x
        self.y = y
        self.length = length
        self.height = display_height
        self.floor = floor
        self.z = z
        self.m = m

    def start(self):
        return ((self.x + 70), (self.y + 85))

    def end(self):
        return ((self.x + self.length + 15), (self.y + 85))

    def solid(self):
        print(self.x, self.z)
        if self.z >= self.x:
            if self.z <= self.x + self.length:
                if self.m <= self.y:
                    self.floor = self.y
            elif self.m > (self.x + self.length):
                self.floor = int(self.height * 0.78)
        elif self.z < self.x:
            self.floor = int(self.height * 0.78)
        floor = self.floor
        return floor

    def draw(self, canvas, color, width):
        pygame.draw.line(canvas, color, self.start(), self.end(), width)