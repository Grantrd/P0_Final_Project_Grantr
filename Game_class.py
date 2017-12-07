import pygame
from pygame import *
from hero_class import*
import platform_class
from enemy_class import *

"""setup Screen"""
pygame.init()
display_width = 800
display_height = 600

"""Colors"""
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

"""setup Game"""
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('penguin_ario')
clock = pygame.time.Clock()
floor = int(.84 * display_height)

"""enemy - to be class"""
hero = platform_class.Hero('animal.png', gameDisplay, floor)
snowman = Enemy('enemy.png', gameDisplay, display_height)
"""setup screen"""
x = int(display_width * 0.45)
y = floor
x_change = 0
jump = False
y_change = 0

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
            if y >= (floor - 10):
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

    """character jumping and moving"""
    if hero.y >= floor:
        jump = False
    if hero.y < floor:
        jump = True
    if hero.y > floor:
        hero.y = floor

    """platforms, in progress"""
    platforms = []
    one = platform_class.Platform(324, 328, 185, gameDisplay)
    two = platform_class.Platform(75, 407, 188, gameDisplay)
    platforms.append(one)
    platforms.append(two)
    for i in range(len(platforms)):
        if platforms[i].solid(hero.x, hero.y, floor)[0]:
            floor = platforms[i].solid(hero.x, hero.y, floor)[1]
        elif platforms[i].solid(hero.x, hero.y, floor)[0]:
            floor = platforms[i].solid(hero.x, hero.y, floor)[1]
        else:
            floor = int(display_height * 0.84)
    """gameScreen"""

    """background"""
    gameDisplay.fill(white)
    gameDisplay.blit(background, [0, 0])
    """platform"""
    one.draw(black, 5)
    two.draw(black, 5)

    """actors... Acting"""
    hero.jumpable(x_change, y_change, floor)
    hero.display()
    snowman.display(snowman.x)
    snowman.track(hero.x)
    if hero.crash(snowman.x, snowman.y) == 1:
        hero.y = -100
        floor = -100
    elif hero.crash(snowman.x, snowman.y) == 2:
       snowman.y = -100
    crashed = hero.game_over()
    """refresh screen"""
    pygame.display.update()

    """clock for ...something later"""
    clock.tick(60)

pygame.quit()
"""end of game loop"""