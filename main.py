from toolkit import *

M = 4
N = 5

surface = Shape(M, N)
blocks = [Shape(3, 2), Shape(2, 2), Shape(2, 1), Shape(2, 3), Shape(1, 2)]


def print_task():
    print("Surface:")
    print("\t", surface)
    print("Blocks: ")
    for block in blocks:
        print("\t", block)


print_task()
