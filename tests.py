from toolkit import *
from unittest import TestCase, main

surface = Shape(4, 5)
blocks = [Shape(3, 2), Shape(2, 2), Shape(2, 1), Shape(2, 3), Shape(1, 2)]


class ToolkitTestCase(TestCase):
    def setUp(self):
        self.surface = Shape(4, 5)
        self.blocks = [Shape(3, 2), Shape(2, 2), Shape(2, 1), Shape(2, 3), Shape(1, 2)]

    def test_find_slice_horizontal(self):
        assert find_slice_horizontal(surface, blocks) == [
            (Shape(3, 2), Shape(1, 2)),
            (Shape(2, 2), Shape(2, 1)),
            (Shape(2, 2), Shape(2, 3)),
            (Shape(2, 1), Shape(2, 3)),
        ], "Horizontal slice doesn't work"

    def test_find_slice_vertical(self):
        assert find_slice_vertical(surface, blocks) == [
            (Shape(3, 2), Shape(2, 3)),
            (Shape(2, 2), Shape(2, 3)),
            (Shape(2, 3), Shape(1, 2)),
        ], "Vertical slice doesn't work"


if __name__ == '__main__':
    main()
