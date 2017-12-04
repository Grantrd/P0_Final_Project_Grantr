from pygame import*
from hero_class import*
from platform_class import*
Clock = pygame.time.Clock()

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
hero = Hero('animal.png')
"""enemy - to be class"""
enemy = pygame.image.load('enemy.png')
#gameDisplay.blit(enemy, (x-100, y))


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
    if y >= floor:
        jump = False
    if y < floor:
        jump = True
    if y > floor:
        y = floor

    """platforms, in progress"""
    one = Platform(100, 300, 115, display_height, floor, x, y, gameDisplay)
    two = Platform(200, 400, 115, display_height, floor, x, y, gameDisplay)
    floor = one.solid()
    floor = two.solid()
    """gameScreen"""

    """background"""
    gameDisplay.fill(white)
    gameDisplay.blit(background, [0, 0])
    """platform"""
    one.draw(white, 5)
    two.draw(black, 5)

    """actors"""
    gameDisplay.blit(enemy, (x-100, y))
    hero.display(x, y, gameDisplay)

    """refresh screen"""
    pygame.display.update()

    """clock for ...something later"""
    clock.tick(60)

pygame.quit()
"""end of game loop"""