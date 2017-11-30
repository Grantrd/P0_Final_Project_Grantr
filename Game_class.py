import pygame

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
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
heroimg = pygame.image.load('hero.gif')

def hero(x, y):
    gameDisplay.blit(heroimg, (x, y))

"""starting x, and y values for hero, and starting x and y change values"""
floor = int(display_height * 0.80)
x = (display_width  * 0.45)
y = floor
x_change = 0
y_change = 0

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_RIGHT:
                x_change = 5
            if event.key == pygame.K_SPACE:
                y_change = -10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_SPACE & y < floor:
                y_change = -1

    x += x_change
    y += y_change
    gameDisplay.fill(white)
    hero(x, y)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
