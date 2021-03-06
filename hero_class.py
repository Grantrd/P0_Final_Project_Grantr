######################################################################
# Author: Rodney Grant
# Username: GrantR
#
# Assignment: P0_Final
#
# Purpose: To demonstrate my knowledge of programming and make a fun Mario Clone
# ###############################################################################
import sys
from sys import _getframe
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
    def testit(self, did_pass):
        linenum = sys._getframe(1).f_lineno                 # Get the caller's line number.
        if did_pass:
            msg = "Hero Test at line {0} ok.".format(linenum)
        else:
            msg = ("Hero Test at line {0} FAILED.".format(linenum))
        print(msg)

    def hero_test_suite(self):
        x = 600
        y = 504
        self.x = x
        self.y = y
        self.testit(self.jumpable(90, -100, 504) == (690, 404))
        self.x = x
        self.y = y
        self.testit(self.jumpable(-100, -120, 504) == (500, 384))
        self.x = x
        self.y = y
        self.testit(self.jumpable(100, 100, 504) == (700, 504))
        self.x = x
        self.y = y
        self.testit(self.jumpable(-200, -200, 504) == (400, 304))
        self.x = x
        self.y = y
        self.testit(self.crash(600, 504) == 1)
        self.x = x
        self.y = y-70
        self.testit(self.crash(550, 504) == 2)
        self.x = x
        self.y = y
        self.testit(self.crash(600, 404) == 2)
        self.x = x
        self.y = -100
        self.testit(self.game_over() == True)
        self.x = x
        self.y = 100
        self.testit(self.game_over() == False)