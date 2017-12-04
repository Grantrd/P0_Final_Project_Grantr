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
