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
from hero_class import*
from pygame import *


class Platform:
    def __init__(self, x, y, length, canvas):
        self.x = x
        self.y = y
        self.length = length
        self.canvas = canvas
        self.draw((130, 130, 130), 5)

    """sets the starting point of drawing it"""
    def start(self):
        return ((self.x + 70), (self.y + 85))

    """sets the end point of drawing it"""
    def end(self):
        return ((self.x + self.length + 15), (self.y + 85))

    """Makes the floor solid"""
    def solid(self, x, y):
        #floor = 504
        if self.x > x > (self.x + self.length) and y < self.y:
            floor = 504
            print("Error")
        elif self.x < x < (self.x + self.length) and y <= self.y:
            floor = self.y
            #print(True)
        else:
            floor = 504
        return floor

    """Draws the floor on screen"""
    def draw(self, colour, width):
        pygame.draw.line(self.canvas, colour, self.start(), self.end(), width)

    def testit(self, did_pass):
        linenum = sys._getframe(1).f_lineno                 # Get the caller's line number.
        if did_pass:
            msg = "Platform Test at line {0} ok.".format(linenum)
        else:
            msg = ("Platform Test at line {0} FAILED.".format(linenum))
        print(msg)

    def platform_test_suite(self):
        """one = platform_class.Platform(324, 328, 185, gameDisplay)
           two = platform_class.Platform(77, 407, 186, gameDisplay)"""
        self.testit(self.solid(400, 320) == 328)
        self.testit(self.solid(90, 400) == 407)
        self.testit(self.solid(100, 100) == 504)