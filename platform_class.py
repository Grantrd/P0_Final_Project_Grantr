from hero_class import*
from pygame import *


class Platform:
    def __init__(self, x, y, length, canvas):
        self.x = x
        self.y = y
        self.length = length
        self.canvas = canvas
        self.draw((130, 130, 130), 5)


    def start(self):
        return ((self.x + 70), (self.y + 85))

    def end(self):
        return ((self.x + self.length + 15), (self.y + 85))

    def solid(self):
        #is_solid = False
        if self.z > self.x:
            if self.z < (self.x + self.length):
                if self.m < self.y:
                    self.floor = self.y
                    #is_solid = True
                elif self.m > self.y:
                    self.floor = int(self.height * 0.78)
                    #is_solid = False
            elif self.z > (self.x + self.length):
                self.floor = int(self.height * 0.78)
                #is_solid = False
        elif self.z < self.x:
            self.floor = int(self.height * 0.78)
            #is_solid = False
        return self.floor

    def draw(self, colour, width):
        pygame.draw.line(self.canvas, colour, self.start(), self.end(), width)
