from hero_class import*


class Platform:
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length

    def start(self):
        return ((self.x + 70), (self.y + 85))

    def end(self):
        return ((self.x + self.length + 15), (self.y + 85))

    def solid(self, display_height, x, y):
        floor = 0
        if x >= self.x:
            if x <= self.x + self.length:
                if y <= self.y:
                    floor = self.y
            elif x > (self.x + self.length):
                floor = int(display_height * 0.78)
        elif x < self.x:
            floor = int(display_height * 0.78)
        return floor
