######################################################################
# Author: Rodney Grant
# Username: GrantR
#
# Assignment: P0_Final
#
# Purpose: To demonstrate my knowledge of programming
# ######################################################################
import pygame
from pygame import *
from hero_class import*
import platform_class
from enemy_class import *
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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                    x_change = -5
            if event.key == pygame.K_RIGHT:
                    x_change = 5
            if hero.y >= (floor - 10):
                if event.key == pygame.K_SPACE:
                    if not jump:
                        y_change = -10
                    else:
                        y_change = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_SPACE:
                if jump:
                    y_change = 5

    """platforms, in progress"""
    one = platform_class.Platform(324, 328, 185, gameDisplay)
    two = platform_class.Platform(77, 407, 186, gameDisplay)

    """gameScreen"""
    hero.display()
    snowman.display(snowman.x)
    snowman.track(hero.x)
    #print(hero.x, hero.y)

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
    hero.jumpable(x_change, y_change, floor)
    if hero.y >= floor:
        jump = False

    if hero.y < floor:
        jump = True

    if hero.y > floor:
        hero.y = floor

    """Selects the necessary platform to make solid"""
    if one.x < hero.x < (one.x + one.length) and hero.y <= one.y:
        floor = one.y
    elif two.x < hero.x < (two.x + two.length) and hero.y <= two.y:
        floor = two.y
    else:
        floor = 504

    """Kills the enemy, or the penguin"""
    if hero.crash(snowman.x, snowman.y) == 1:
        hero.y = -100
        floor = -100
    elif hero.crash(snowman.x, snowman.y) == 2:
        snowman.y = -100
    if hero.x > display_width:
        hero.y = -100
    if hero.x < -65:
        hero.y = -100

    """ends the game loop"""
    crashed = hero.game_over()
    print(hero.x, hero.y)

    """Allows fish coin collecting and winning"""
    if floor == one.y:
        if 425 > hero.x > 410:
            if 285 > hero.y:
                gameDisplay.fill(white)
                gameDisplay.blit(textsurface, (int(display_width/2 - 110), int(display_height/2)))
                win = True

    """refresh screen"""
    pygame.display.update()

    if win:
        crashed = True
        pygame.time.delay(2000)

    """clock for ...something later"""
    clock.tick(60)

pygame.quit()
"""end of game loop"""