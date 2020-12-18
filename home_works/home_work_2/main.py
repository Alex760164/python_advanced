from src.circle import Circle
from src.point import Point

if __name__ == '__main__':
    # Testing libraries of Point and Circle
    small_circle = Circle(Point(12, 12), 425)
    big_circle = Circle(Point(9, 1), 10293.4)

    if (small_circle < big_circle):
        print('Test #1 is OK')

    if (small_circle == small_circle):
        print('Test #2 is OK')
