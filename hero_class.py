from enemy_class import *
import pygame


class Hero:

    def __init__(self, img, canvas):
        self.y = 486
        self.x = 600
        self.canvas = canvas
        self.img = img
        self.load = pygame.image.load(self.img)

    def display(self, x, y, floor, jump):
        self.x += x
        if (floor - 100) < (self.y + y):
            self.y += y
            if self.y == floor - 90:
                if self.y < floor:
                    self.y = floor
        elif self.y < floor and (self.y > self.y - 100):
            self.y += + 10
        self.canvas.blit(self.load, (self.x, self.y))
        return self.x, self.y
    """work in progress"""
    def crash(self, snowmanx, snowmany):
        x = snowmanx
        y = snowmany
        if int(self.y) == int(y):
            if int(self.x) <= int(x + 70):
                if int(self.x) >= int(x - 70):
                    return 1
        elif int(self.y) == int(y - 70):
            if int(self.x) <= int(x + 50):
                if int(self.x) >= int(x - 50):
                    return 2

    def game_over(self):
        if self.y <= -100:
            crashed = True
        else:
            crashed = False
        return crashed

