######################################################################
# Author: Rodney Grant
# Username: GrantR
#
# Assignment: P0_Final
#
# Purpose: To demonstrate my knowledge of programming and make a fun Mario Clone
# ###############################################################################
import pygame
import sys
from sys import _getframe

class Enemy:
    """Creates the enemy"""
    def __init__(self, img, canvas, height):
        self.canvas = canvas
        self.img = img
        self.load = pygame.image.load(self.img)
        self.x = 100
        self.y = int(height * 0.84)

    """Draws the enemy on screen"""
    def display(self, x):
        self.x = x
        self.canvas.blit(self.load, (x, self.y))
        #return self.x, self.y

    """Allows the enemy to Follow the Hero"""
    def track(self, x):
        change = 0
        if self.x != x:
            if self.x < x:
                change = 3
            elif self.x > x:
                change = -5
            else:
                change = 0
        self.x += change
        return self.x

    def testit(self, did_pass):
        linenum = sys._getframe(1).f_lineno                 # Get the caller's line number.
        if did_pass:
            msg = "Enemy Test at line {0} ok.".format(linenum)
        else:
            msg = ("Enemy Test at line {0} FAILED.".format(linenum))
        print(msg)

    def enemy_test_suite(self):
        self.x = 100
        self.testit(self.track(600) == 103)
        self.x = 100
        self.testit(self.track(90) == 95)
        self.x = 100
        self.testit(self.track(100) == 100)
        self.x = 100
        self.testit(self.track(700) == 100)