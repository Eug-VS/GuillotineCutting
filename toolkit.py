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


def find_slice(surface, blocks, orientation):
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


def find_slice_horizontal(surface, blocks):
    return find_slice(surface, blocks, "horizontal")


def find_slice_vertical(surface, blocks):
    return find_slice(surface, blocks, "vertical")
