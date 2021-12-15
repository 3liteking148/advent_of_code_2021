import re
from heapq import heappush, heappop, heapify


def get_lowest_risk(grid):
    width, height = len(grid[0]), len(grid)
    weights = {(0, 0): 0}

    # priority queue
    pq = [(0, 0, 0)]
    heapify(pq)

    while pq:
        risk, r, c = heappop(pq)
        next_coords = ((r-1, c), (r+1, c), (r, c-1), (r, c+1))

        for r1, c1 in next_coords:
            if 0 <= r1 < height and 0 <= c1 < width:
                current_weight = weights.get((r1, c1), 2 ** 32)
                new_weight = grid[r1][c1] + weights[(r, c)]

                if current_weight > new_weight:
                    weights[(r1, c1)] = new_weight
                    heappush(pq, (new_weight, r1, c1))

    return weights[(height-1, width-1)]


with open('day15.txt', 'r') as inp:
    lines = re.findall(r'(\b\d+\b)', inp.read())
    grid = [[int(x) for x in line] for line in lines]
    width, height = len(grid[0]), len(grid)

    print(get_lowest_risk(grid))
    conversion = [9, 1, 2, 3, 4, 5, 6, 7, 8]
    grid2 = [[conversion[(grid[r % width][c % height] + c // width + r
             // height) % 9] for c in range(width*5)] for r in range(height*5)]
    print(get_lowest_risk(grid2))
