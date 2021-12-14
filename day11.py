def valid(w, h, r, c):
    return 0 <= r < h and 0 <= c < w

def step(grid):
    w = len(grid[0])
    h = len(grid)

    stack = []
    flashes = 0

    for r in range(h):
        for c in range(w):
            grid[r][c] += 1
            if grid[r][c] == 10:
                stack.append((r, c))

    while len(stack) != 0:
        r, c = stack.pop()
        grid[r][c] = 0
        flashes += 1

        for r1 in range(r-1, r+2):
            for c1 in range(c-1, c+2):
                if valid(w, h, r1, c1) and grid[r1][c1] != 0:
                    grid[r1][c1] += 1
                    if grid[r1][c1] == 10:
                        stack.append((r1, c1))
    return flashes


with open('day11.txt', 'r') as inp:
    part1 = [[int(x) for x in y.strip()] for y in inp]
    part2 = [y[:] for y in part1] # deep copy

    flash = 0

    for i in range(100):
        flash += step(part1)

    print(flash)

    steps = 0
    while sum(sum(y) for y in part2) != 0:
        step(part2)
        steps += 1
    print(steps)
