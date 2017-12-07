import pygame

class Enemy:

    def __init__(self, img, canvas, height):
        self.canvas = canvas
        self.img = img
        self.load = pygame.image.load(self.img)
        self.x = 100
        self.y = int(height * 0.84)

    def display(self, x):
        self.x = x
        self.canvas.blit(self.load, (x, self.y))
        return self.x, self.y

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


