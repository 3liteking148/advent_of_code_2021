import re
from functools import reduce


def t(visited, grid, row, col):
    w = len(grid[0])
    h = len(grid)

    if not (0 <= row < h and 0 <= col < w):
        return -1

    if visited[row][col]:
        return -1
    visited[row][col] = True

    if grid[row][col] == 9:
        return -1

    a = 1 + t(visited, grid, row + 1, col)
    b = 1 + t(visited, grid, row - 1, col)
    c = 1 + t(visited, grid, row, col + 1)
    d = 1 + t(visited, grid, row, col - 1)
    return a + b + c + d

with open('day9.txt', 'r') as inp:
    grid = re.findall(r'(\b\d+\b)', inp.read())
    grid = [[int(x) for x in y] for y in grid]

    w = len(grid[0])
    h = len(grid)

    visited = [[False for _ in range(w)] for _ in range(h)]
    a = []
    part1 = 0
    for y in range(h):
        for x in range(w):
            # part 1
            up    = y == 0 or grid[y][x] < grid[y-1][x]
            down  = x == 0 or grid[y][x] < grid[y][x-1]
            left  = y == h - 1 or grid[y][x] < grid[y+1][x]
            right = x == w - 1 or grid[y][x] < grid[y][x+1]

            if up and down and left and right:
                part1 += 1 + grid[y][x]

            # part 2
            a.append(1 + t(visited, grid, y, x))
    print(part1)

    a.sort()
    print(reduce(lambda a, b: a*b, a[-3:]))
