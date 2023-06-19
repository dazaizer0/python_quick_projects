import math
import random


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    d = math.sqrt(dx**2 + dy**2)
    return d


def generate_cell(pos_x, pos_y):
    d = distance(int(pos_x), int(pos_y), 10, 10)
    i = random.randint(0, int(d / 2))
    if i < 4:
        print("# ", end="")
    else:
        print(". ", end="")


size = 30

for y in range(0, size):
    for x in range(0, size):
        generate_cell(x, y)
    print("")
