with open('day25.txt') as inp:
    grid = [[c for c in line.strip()] for line in inp.readlines()]
    height, width = len(grid), len(grid[0])

    ans = 0
    moved = True
    locked = set()
    while moved:
        moved = False
        for target in ('>', 'v'):
            locked.clear()
            for i in range(height):
                for j in range(width):
                    i_next = (i + 1) % height if target == 'v' else i
                    j_next = (j + 1) % width if target == '>' else j
                    if grid[i][j] == target and grid[i_next][j_next] == '.':
                        if (i, j) in locked or (i_next, j_next) in locked:
                            continue
                        grid[i][j] = '.'
                        grid[i_next][j_next] = target
                        locked.add((i, j))
                        locked.add((i_next, j_next))
                        moved = True
        ans += 1
    print(ans)
