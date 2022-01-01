from heapq import heappush, heappop, heapify


cost = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
room = {'A': 3, 'B': 5, 'C': 7, 'D': 9}
room2 = {3: 'A', 5: 'B', 7: 'C', 9: 'D'}
hallway_coords = (1, 2, 4, 6, 8, 10, 11)
room_coords = (3, 5, 7, 9)


def move(energy, map, dbg, row1, col1, row2, col2):
    map = tuple((tuple((map[row1][col1] if row == row2 and col == col2 else map[row2][col2]  if row == row1 and col == col1 else map[row][col] for col in range(len(map[row])))) if row in [row1, row2] else map[row] for row in range(len(map))))
    c = cost[map[row2][col2]] * (abs(row1 - row2) + abs(col1 - col2))

    #return (energy + c, map, dbg + ((row1, col1, row2, col2),))
    return (energy + c, map, dbg)


def print_map(map):
    for row in map:
        for pixel in row:
            print(pixel, end='')
    print()


def solve(map, row_cnt):
    pq = [(0, map, ())]
    heapify(pq)
    prev = 0

    evaluated = {}
    while len(pq):
        energy, map, dbg = heappop(pq)
        if map in evaluated:
            continue
        evaluated[map] = True

        ok = True
        for i in range(2, 2 + row_cnt):
            if (map[i][3] != 'A' or map[i][5] != 'B' or map[i][7] != 'C' or map[i][9] != 'D'):
                ok = False
                break
        if ok:
            return (energy, dbg)

        for idx, i in enumerate(hallway_coords):
            if map[1][i] != '.':
                for target in room_coords:
                    letter = map[1][i]

                    ok = room[letter] == target
                    for j in range(i+1, target+1):
                        ok &= map[1][j] == '.'
                    for j in range(target, i):
                        ok &= map[1][j] == '.'
                    if not ok:
                        continue

                    # insert at deepest
                    for depth in range(2, 2 + row_cnt):
                        ok = map[depth][target] == '.'

                        # check above
                        for d in range(2, depth):
                            ok &= map[d][target] == '.'

                        # check deeper
                        for d in range(depth + 1, 2 + row_cnt):
                            ok &= map[d][target] == room2[target]

                        if ok:
                            test = move(energy, map, dbg, 1, i, depth, target)
                            heappush(pq, test)
                            break

        for idx, i in enumerate(room_coords):
            invalid_in_col = False
            for d in range(2, 2 + row_cnt):
                invalid_in_col |= map[d][i] != room2[i]
            if not invalid_in_col:
                continue

            if map[2][i] != '.':
                for target in hallway_coords:
                    ok = True
                    for j in range(i+1, target+1):
                        ok &= map[1][j] == '.'
                    for j in range(target, i):
                        ok &= map[1][j] == '.'
                    if ok:
                        test = move(energy, map, dbg, 2, i, 1, target)
                        heappush(pq, test)

            for d in range(3, 2 + row_cnt):
                if map[d][i] != '.':
                    empty = True
                    for dd in range(2, d):
                        empty &= map[dd][i] == '.'

                    if empty:
                        test = move(energy, map, dbg, d, i, 2, i)
                        heappush(pq, test)
                        break


with open('day23.txt', 'r') as inp:
    lines = inp.readlines()

    # part 1
    map = tuple(tuple(x for x in line) for line in lines)
    ans, path = solve(map, 2)
    print(ans)

    # part 2
    lines.insert(3, '  #D#C#B#A#')
    lines.insert(4, '  #D#B#A#C#')
    map = tuple(tuple(x for x in line) for line in lines)
    ans, path = solve(map, 4)
    print(ans)

    '''
    for p in path:
        _, map, _ = move(0, map, (), p[0], p[1], p[2], p[3])
        print_map(map)
    '''
