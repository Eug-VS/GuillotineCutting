class Shape:
    def __init__(self, h, w):
        self.w = w
        self.h = h
    
    def __str__(self):
        return f'Shape({self.h} x {self.w})'

    def area(self):
        return self.w * self.h
