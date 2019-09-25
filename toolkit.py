from random import randint, seed

seed(0)


class Shape:
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def __str__(self):
        return f'Shape({self.h} x {self.w})'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.h == other.h and self.w == other.w

    def area(self):
        return self.h * self.w


def random_shape(shape):
    return Shape(randint(1, shape.h), randint(1, shape.w))


def slice_pair(surface, blocks, orientation):
    results = []
    for block in blocks:
        for other in blocks:
            if other != block:
                if orientation == "horizontal":
                    if block.h + other.h == surface.h:
                        results.append((block, other))
                elif orientation == "vertical":
                    if block.w + other.w == surface.w:
                        results.append((block, other))
    for pair in results:
        for other in results:
            if other == (pair[1], pair[0]):
                results.remove(other)
    return results


def slice_pair_horizontal(surface, blocks):
    return slice_pair(surface, blocks, "horizontal")


def slice_pair_vertical(surface, blocks):
    return slice_pair(surface, blocks, "vertical")
