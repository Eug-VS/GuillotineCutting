from random import randint, seed

seed(0)


class Shape:
    def __init__(self, h, w, stub=False):
        self.h = h
        self.w = w
        self.stub = stub

    def __str__(self):
        if not self.stub:
            return f'Shape({self.h} x {self.w})'
        else:
            return f'Stub-Shape({self.h} x {self.w})'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.h == other.h and self.w == other.w

    def area(self):
        return self.h * self.w

    def inscribes(self, other):
        return other.h <= self.h and other.w <= self.w


def random_shape(shape):
    return Shape(randint(1, int(shape.h*0.7)), randint(1, int(shape.w*0.7)))


class Slicer:
    def __init__(self, surface, blocks):
        self.surface = surface
        self.blocks = blocks

    def __str__(self):
        s = f'Slicer with surface {self.surface} and blocks:\n -'
        s += "\n -".join(str(block) for block in self.blocks)
        return s

    def use_block(self, target_block):
        print(f'Using block {target_block}')
        for block in self.blocks:
            if block == target_block:
                self.blocks.remove(block)
                return

    def get_slice_pairs(self, orientation):
        results = []
        for block in self.blocks:
            if self.surface.inscribes(block):
                if block == self.surface:
                    print(f'(!) Block {block} fits just into the surface!')
                    return block
                if orientation == "horizontal" and block.w == self.surface.w:
                    stub = Shape(self.surface.h - block.h, block.w, stub=True)
                    print(f'(!) Block {block} takes all width of surface {self.surface}. Creating {stub}')
                    return [(block, stub)]
                elif orientation == "vertical" and block.h == self.surface.h:
                    stub = Shape(block.h, self.surface.w - block.w, stub=True)
                    print(f'(!) Block {block} takes all height of surface {self.surface}. Creating {stub}')
                    return [(block, stub)]
                else:
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
        slice_pairs = self.get_slice_pairs("horizontal")
        if type(slice_pairs) is list:
            if len(slice_pairs):
                print("Horizontal block pairs:\n\t" + "\n\t".join(str(pair) for pair in slice_pairs))
        return slice_pairs

    def get_slice_pairs_vertical(self):
        slice_pairs = self.get_slice_pairs("vertical")
        if type(slice_pairs) is list:
            if len(slice_pairs):
                print("Vertical block pairs:\n\t" + "\n\t".join(str(pair) for pair in slice_pairs))
        return slice_pairs

    def solve(self):
        v_block_pairs = self.get_slice_pairs_vertical()
        if type(v_block_pairs) is not list:
            self.use_block(v_block_pairs)
            return self.blocks
        h_block_pairs = self.get_slice_pairs_horizontal()
        if type(h_block_pairs) is not list:
            self.use_block(h_block_pairs)
            return self.blocks
        v_pairs = []
        h_pairs = []

        for block_pair in v_block_pairs:
            l = block_pair[0].w
            r = block_pair[1].w
            if (l, r) not in v_pairs and (r, l) not in v_pairs:
                v_pairs.append((l, r))

        for block_pair in h_block_pairs:
            u = block_pair[0].h
            d = block_pair[1].h
            if (u, d) not in h_pairs and (d, u) not in h_pairs:
                h_pairs.append((u, d))

        print("Vertical slices:\n", v_pairs)
        print("Horizontal slices:\n", h_pairs)

        if len(v_pairs) == 1 and len(h_pairs) == 1:
            if v_block_pairs[0][1].stub and h_block_pairs[0][1].stub:
                print('Both vertical and horizontal slices fit...')
                v_area = v_block_pairs[0][0].area()
                h_area = h_block_pairs[0][0].area()
                if v_area > h_area:
                    print('...but vertical slice has more area value!')
                    h_pairs = []
                else:
                    print('...but horizontal slice has more area value!')
                    v_pairs = []
            elif v_block_pairs[0][1].stub:
                print('Vertical slice fits better!')
                h_pairs = []
            else:
                print('Horizontal slice fits better!')
                v_pairs = []

        if len(v_pairs) == 1:
            print("The only possible vertical slice found. Go!")

            left_surface = Shape(self.surface.h, v_pairs[0][0])
            right_surface = Shape(self.surface.h, v_pairs[0][1])

            for block in self.blocks:
                if block == left_surface:
                    print('(!) Left part of the slice corresponds to the block:')
                    self.use_block(block)
                    left_surface = None
                    break
            for block in self.blocks:
                if block == right_surface:
                    print('(!) Right part of the slice corresponds to the block:')
                    self.use_block(block)
                    right_surface = None
                    break

            if left_surface:
                left = Slicer(left_surface, self.blocks)
                print("Left: ", left)
                self.blocks = left.solve()
            if right_surface:
                right = Slicer(right_surface, self.blocks)
                print("Right: ", right)
                self.blocks = right.solve()

        elif len(h_pairs):
            print("The only possible horizontal slice found. Go!")

            up_surface = Shape(h_pairs[0][1], self.surface.w)
            bottom_surface = Shape(h_pairs[0][0], self.surface.w)

            for block in self.blocks:
                if block == up_surface:
                    print('(!) Upper part of the slice corresponds to the block:')
                    self.use_block(block)
                    up_surface = None
                    break
            for block in self.blocks:
                if block == bottom_surface:
                    print('(!) Bottom part of the slice corresponds to the block:')
                    self.use_block(block)
                    bottom_surface = None
                    break

            if up_surface:
                up = Slicer(up_surface, self.blocks)
                print("Up: ", up)
                self.blocks = up.solve()

            if bottom_surface:
                bottom = Slicer(bottom_surface, self.blocks)
                print("Bottom: ", bottom)
                self.blocks = bottom.solve()

        return self.blocks
