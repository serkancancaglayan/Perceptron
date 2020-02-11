import random


class Point:
    def __init__(self):
        self.x = random.uniform(0, 400)
        self.y = random.uniform(0, 400)
        if self.x > self.y:
            self.label = 1
        else:
            self.label = -1
