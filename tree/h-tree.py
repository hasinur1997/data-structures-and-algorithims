import math

def draw_line(x1, y1, x2, y2):
    pass


def draw_htree(x, y, length, depth):

    if (depth == 0):
        return
    x0 = x - length / 2
    x1 = x + length / 2
    y0 = y - length / 2
    y1 = y + length / 2

    draw_line(x0, y0, x0, y1)
    draw_line(x1, y0, x1, y1)
    draw_line(x0, y, x1, y)

    new_length = length/math.sqrt(2)

