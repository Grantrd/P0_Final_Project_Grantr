import pygame


class Hero:

    def __init__(self, img):
        self.img = img
        self.load = pygame.image.load(self.img)

    def display(self, x, y, gameDisplay):
        self.x = x
        self.y = y
        gameDisplay.blit(self.load, (x, y))
        return self.x, self.y


