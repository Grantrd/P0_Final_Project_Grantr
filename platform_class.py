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
        state = []
        is_solid = False
        if self.z >= self.x:
            if self.z <= (self.x + self.length):
                if self.m <= self.y:
                    return (True, self.y)
                    #is_solid = True
                else:
                    return (False, int(self.height * 0.78))
                    #is_solid = False
            else:
                return (False, int(self.height * 0.78))
                #is_solid = False
        else:
            return (False, int(self.height * 0.78))

        # state.append(is_solid)
        # state.append(self.floor)
        # print(state)
        # return state

    def draw(self, colour, width):
        pygame.draw.line(self.canvas, colour, self.start(), self.end(), width)
