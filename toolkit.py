class Shape:
    def __init__(self, h, w):
        self.w = w
        self.h = h
        self.area = self.w * self.h

    def __str__(self):
        return f'Shape({self.h} x {self.w})'
