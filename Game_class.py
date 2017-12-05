import pygame
from pygame import *
from hero_class import*
import platform_class
import random
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
floor = int(display_height * 0.78)

"""enemy - to be class"""
hero = platform_class.Hero('animal.png', gameDisplay)
snowman = Enemy('enemy.png', gameDisplay)


x = int(display_width * 0.45)
y = floor
x_change = 0
jump = False
y_change = 0

"""game loop"""
crashed = False

while not crashed:
    background = pygame.image.load('background.png').convert()

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

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_SPACE:
                if jump:
                    y_change = 5

    """character jumping and moving"""
    x += x_change
    y += y_change
    z = x-(random.randint(1, 100))
    m = y-(random.randint(-50, 50))
    if y >= floor:
        jump = False
    if y < floor:
        jump = True
    if y > floor:
        y = floor

    """platforms, in progress"""
    one = platform_class.Platform(100, 300, 115, display_height, floor, x, y, gameDisplay)
    two = platform_class.Platform(200, 400, 115, display_height, floor, x, y, gameDisplay)
    # if (not one.solid()) & (not two.solid()):
    #     int(display_height * 0.78)
    # if one.solid():
    #     floor = one.y
    # if two.solid():
    #     floor = two.y
    #if two.solid():
        #floor = two.platformer()
    if not one.solid():
        floor = two.platformer()
    elif not two.solid():
        floor = one.platformer()
    """gameScreen"""

    """background"""
    gameDisplay.fill(white)
    gameDisplay.blit(background, [0, 0])
    """platform"""
    one.draw(white, 5)
    two.draw(black, 5)

    """actors"""
    hero.display(x, y)
    snowman.display(snowman.track(x))
    if hero.crash(snowman.track(x), snowman.y) == "True":
        snowman.y = -100
    if hero.crash(snowman.track(x), snowman.y):
        hero.y = -100
        floor = - 100
    #else:
        #print("miss")


    """refresh screen"""
    pygame.display.update()

    """clock for ...something later"""
    clock.tick(60)

pygame.quit()
"""end of game loop"""