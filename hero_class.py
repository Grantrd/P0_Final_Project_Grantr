from enemy_class import *
import pygame


class Hero:

    def __init__(self, img, canvas):
        self.y = 486
        self.x = 600
        self.canvas = canvas
        self.img = img
        self.load = pygame.image.load(self.img)

    def display(self, x, y):
        self.x += x
        self.y += y
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
        elif int(self.y) == int(y - 100):
            if int(self.x) <= int(x + 40):
                if int(self.x) >= int(x - 40):
                    return 2

    def game_over(self):
        if self.y <= -100:
            crashed = True
        else:
            crashed = False
        return crashed

