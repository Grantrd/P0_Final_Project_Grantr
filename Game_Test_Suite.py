######################################################################
# Author: Rodney Grant
# Username: GrantR
#
# Assignment: P0_Final
#
# Purpose: To demonstrate my knowledge of programming and make a fun Mario Clone
# ###############################################################################

from Game_class import *
from hero_class import *
from platform_class import *
from enemy_class import *


def testit(did_pass):
    """
    Prints the result of the tests
    """
    linenum = sys.getframe(1).f_lineno                 # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def game_test_suite():
    hero = Hero('animal.png', None, 504)
    testit(hero.crash(100, 200) == 1)



