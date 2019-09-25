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


class Slicer:
    def __init__(self, surface, blocks):
        self.surface = surface
        self.blocks = blocks

    def __str__(self):
        s = f'Slicer with surface {self.surface} and blocks:\n -'
        s += "\n -".join(str(block) for block in self.blocks)
        return s

    def get_slice_pairs(self, orientation):
        results = []
        for block in self.blocks:
            for other in self.blocks:
                if other != block:
                    if orientation == "horizontal":
                        if block.h + other.h == self.surface.h:
                            results.append((block, other))
                    elif orientation == "vertical":
                        if block.w + other.w == self.surface.w:
                            results.append((block, other))
        for pair in results:
            for other in results:
                if other == (pair[1], pair[0]):
                    results.remove(other)
        return results

    def get_slice_pairs_horizontal(self):
        return self.get_slice_pairs("horizontal")

    def get_slice_pairs_vertical(self):
        return self.get_slice_pairs("vertical")
