from enemy_class import *
import pygame


class Hero:

    def __init__(self, img, canvas):
        self.canvas = canvas
        self.img = img
        self.load = pygame.image.load(self.img)

    def display(self, x, y):
        self.x = x
        self.y = y
        self.canvas.blit(self.load, (x, y))
        return self.x, self.y
    """work in progress"""
    def crash(self, enemy_x, enemy_y):
        x = enemy_x
        y = enemy_y
        #print("Y: " + str(self.y + 10), y, "X: " + str(self.x), x)
        if int(self.y + ) == int(y):
            if int(self.x) == int(x):
                return "True"
        elif int(self.y) == int(y):
            if int(self.x) == int(x + 40) or int(self.x) == int(x - 40):
                return "False"

