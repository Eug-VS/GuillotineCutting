from random import randint, seed

seed(0)


class Shape:
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def __str__(self):
        return f'Shape({self.h} x {self.w})'

    def area(self):
        return self.w * self.h


def random_shape(shape):
    return Shape(randint(1, shape.h), randint(1, shape.w))
