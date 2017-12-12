######################################################################
# Author: Rodney Grant
# Username: GrantR
#
# Assignment: P0_Final
#
# Purpose: To demonstrate my knowledge of programming and make a fun Mario Clone
# ###############################################################################
from pygame import *
from hero_class import*
import platform_class
from enemy_class import *
import unittest

"""Method Allows the game to take player input and use it to move the player"""


def player_input(event, floor, hero_y, jump, x_change, y_change):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_change = -5
        if event.key == pygame.K_RIGHT:
            x_change = 5
        if hero_y >= (floor - 10):
            if event.key == pygame.K_SPACE:
                if not jump:
                    y_change = -10
                else:
                    y_change = 10

    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            x_change = 0
        if event.key == pygame.K_SPACE:
            if jump:
                y_change = 5
    return x_change, y_change


def gravity(floor, hero, jump, x_change, y_change):
    hero.jumpable(x_change, y_change, floor)
    if hero.y >= floor:
        jump = False
    if hero.y < floor:
        jump = True
    if hero.y > floor:
        hero.y = floor
    return jump


def winner(display_width, display_height, floor, gameDisplay, hero, one, textsurface, white):
    if floor == one.y:
        if 440 > hero.x > 400:
            if 280 > hero.y:
                gameDisplay.fill(white)
                gameDisplay.blit(textsurface, (int(display_width / 6 - 110), int(display_height / 2)))
                win = True
            else:
                win = False
        else:
            win = False
    else:
        win = False
    return win


def lose(display_width, floor, hero, snowman):
    if hero.crash(snowman.x, snowman.y) == 1:
        hero.y = -100
        floor = -100
    elif hero.crash(snowman.x, snowman.y) == 2:
        snowman.y = -100
    if hero.x > display_width:
        hero.y = -100
    if hero.x < -65:
        hero.y = -100
    return floor


def platform(floor, hero, one, two):
    if one.x < hero.x < (one.x + one.length) and hero.y <= one.y:
        floor = one.y
    elif two.x < hero.x < (two.x + two.length) and hero.y <= two.y:
        floor = two.y
    else:
        floor = 504
    return floor


def testit(did_pass):
    linenum = sys._getframe(1).f_lineno                 # Get the caller's line number.
    if did_pass:
        msg = "Game Test at line {0} ok.".format(linenum)
    else:
        msg = ("Game Test at line {0} FAILED.".format(linenum))
    print(msg)


def game_test_suite(hero, gameDisplay, textsurface, one, snowman, two):
    hero.y = 504
    hero.x = 600
    testit(gravity(504, hero, True, -10, 0) == False)
    testit(gravity(504, hero, True, 0, -10) == True)
    testit(gravity(504, hero, True, 500, 0) == False)
    testit(gravity(504, hero, True, 0, 300) == True)
    testit(winner(800, 600, 504, gameDisplay, hero, one, textsurface, (255, 255, 255)) == False)
    hero.x = 420
    hero.y = 278
    testit(winner(800, 600, 504, gameDisplay, hero, one, textsurface, (255, 255, 255)) == True)
    snowman.x = 100
    snowman.y = 504
    testit(lose(800, 504, hero, snowman) == 504)
    snowman.x = 600
    snowman.y = 504
    hero.y = 504
    hero.x = 600
    testit(lose(800, 504, hero, snowman) == -100)
    snowman.x = 300
    snowman.y = 504
    testit(lose(800, 504, hero, snowman) == -100)
    hero.x = 350
    hero.y = 325
    testit(platform(504, hero, one, two) == 328)
    hero.x = 130
    hero.y = 405
    testit(platform(504, hero, one, two) == 407)
    hero.x = 300
    hero.y = 400
    testit(platform(504, hero, one, two) == 328)
    hero.x = 0
    hero.y = 0
    testit(platform(504, hero, one, two) == 407)


def main():
    """setup Screen"""
    pygame.init()
    display_width = 800
    display_height = 600
    pygame.font.init()

    myfont = pygame.font.SysFont('Comic Sans MS', 90)
    """Colors"""
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (0, 255, 0)

    """setup Game"""
    coin = pygame.image.load('coin.png')
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('penguin_ario')
    clock = pygame.time.Clock()
    floor = int(.84 * display_height)

    """enemy - to be class"""
    hero = Hero('animal.png', gameDisplay, floor)
    snowman = Enemy('enemy.png', gameDisplay, display_height)
    """setup screen"""
    win = False
    x = int(display_width * 0.45)
    y = floor
    x_change = 0
    jump = False
    y_change = 0
    textsurface = myfont.render('Congratulations You win', False, (0, 0, 0))

    """game loop"""
    crashed = False

    while not crashed:
        background = pygame.image.load('background2.png').convert()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            x_change, y_change = player_input(event, floor, hero.y, jump, x_change, y_change)

        """platforms, in progress"""
        one = platform_class.Platform(324, 328, 185, gameDisplay)
        two = platform_class.Platform(77, 407, 186, gameDisplay)

        """gameScreen"""
        hero.display()
        snowman.display(snowman.x)
        snowman.track(hero.x)

        """background"""
        gameDisplay.fill(white)
        gameDisplay.blit(background, [0, 0])
        snowman.display(snowman.x)
        snowman.track(hero.x)
        gameDisplay.blit(coin, (430, 270))

        """platform"""
        one.draw(white, 5)
        two.draw(white, 5)
        hero.display()

        """actors... Acting"""
        jump = gravity(floor, hero, jump, x_change, y_change)

        """Selects the necessary platform to make solid"""
        floor = platform(floor, hero, one, two)

        """Kills the enemy, or the penguin"""
        floor = lose(display_width, floor, hero, snowman)

        """ends the game loop"""
        crashed = hero.game_over()


        """Allows fish coin collecting and winning"""
        win = winner(display_width, display_height, floor, gameDisplay, hero, one, textsurface, green)

        """refresh screen"""
        pygame.display.update()

        if win:
            crashed = True
            pygame.time.delay(2000)

        """clock for ...something later"""
        clock.tick(60)

    pygame.quit()

    """end of game loop"""

    hero.hero_test_suite()
    one.platform_test_suite()
    two.platform_test_suite()
    snowman.enemy_test_suite()
    game_test_suite(hero, gameDisplay, textsurface, one, snowman, two)


main()

if __name__ == '__main__':
    unittest.main()