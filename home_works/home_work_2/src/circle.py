PI = 3.14


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def square(self):
        return PI * (self.radius ** 2)

    def do_intersect(self, circle):
        l_centers = (((self.center.x - circle.center.x) ** 2) + ((self.center.y - circle.center.y) ** 2)) ** 0.5
        delta = l_centers - self.radius - circle.radius
        if delta > 0:
            return False
        else:
            return True

    # x < y
    def __lt__(self, other):
        if self.square() < other.square():
            return True
        else:
            return False

    # x ≤ y
    def __le__(self, other):
        if self.square() <= other.square():
            return True
        else:
            return False

    # x == y
    def __eq__(self, other):
        if self.square() == other.square():
            return True
        else:
            return False

    # x != y
    def __ne__(self, other):
        return not self.__eq__(other)

    # x > y
    def __gt__(self, other):
        return other.__lt__(self)

    # x ≥ y
    def __ge__(self, other):
        return other.__le__(self)
