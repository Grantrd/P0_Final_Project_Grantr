######################################################################
# Author: Rodney Grant
# Username: GrantR
#
# Assignment: P0_Final
#
# Purpose: To demonstrate my knowledge of programming
# ######################################################################
from enemy_class import *
import pygame
import platform_class

class Hero:

    def __init__(self, img, canvas,  floor):
        self.y = floor
        self.x = 600
        self.canvas = canvas
        self.img = img
        self.load = pygame.image.load(self.img)
    """Allows the player to jump"""
    def jumpable(self, x, y, floor):
        self.x += x
        if (floor - 130) < (self.y + y):
            self.y += y
            if self.y == floor - 130:
                if self.y < floor:
                    self.y += 10
                    print(floor)
        return self.x, self.y

    """lets the snowman and penguin kill each other"""
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

    def gravity(self, platform):
        floors = platform.solid(self.x, self.y)
        jump = False

        if self.y > floors:
            self.y = floors

        if self.y >= floors:
            jump = False

        if self.y < floors:
            jump = True

        return jump, floors

    """ends the game if the penguin dies"""
    def game_over(self):
        if self.y <= -100:
            crashed = True
        else:
            crashed = False
        return crashed
    """Draws the hero on screen"""
    def display(self):
        self.canvas.blit(self.load, (self.x, self.y))
