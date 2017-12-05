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
        is_solid = False
        if self.z < self.x:
            is_solid = False
            self.floor = int(self.height * .78)
        elif self.z > (self.x + self.length):
            is_solid = False
            self.floor = int(self.height * .78)
        elif self.m > self.y:
            is_solid = False
            self.floor = int(self.height * .78)
        else:
            is_solid = True
            self.floor = self.y
        # else:
        #     state = [False, int(self.height * 0.78)]
        # state.append(is_solid)
        # state.append(self.floor)
        # print(state)
        return is_solid

    def draw(self, colour, width):
        pygame.draw.line(self.canvas, colour, self.start(), self.end(), width)
