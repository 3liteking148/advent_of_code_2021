import re

def test(dx, dy, x0, x1, y0, y1):
    x = 0
    y = 0

    tmp = -2 ** 32
    while x <= x1 and y >= y1:
        if x0 <= x and y0 >= y:
            return True

        x += dx
        y += dy

        if dx > 0:
            dx -= 1

        dy -= 1
    return False

with open('day17.txt', 'r+') as inp:
    capture = re.match(r'target area: x=(\d+)\.\.(\d+), y=([-\d]+)\.\.([-\d]+)', inp.read()).groups()
    x0, x1, y1, y0 = (int(x) for x in capture)
    print(capture)

    best = -2**32
    total = 0

    for i in range(1, x1 + 1):
        tmp = 0
        for j in range(y1, y1 * -1):
            if test(i, j, x0, x1, y0, y1):
                #print(i, j)
                best = max(best, j)
                tmp += 1
        #print(i, tmp)
        total += tmp
    print(best * (best + 1) // 2)
    print(total)
