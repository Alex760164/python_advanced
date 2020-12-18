class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point):
        return ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5
