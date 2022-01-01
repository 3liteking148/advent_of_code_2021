# idea from https://www.mattkeeter.com/blog/2021-12-27-brute/
# vocarious ram eater

W = 0
X = 1
Y = 2
Z = 3
MIN = 4
MAX = 5


def to_idx(x):
    if x == 'w':
        return W
    if x == 'x':
        return X
    if x == 'y':
        return Y
    if x == 'z':
        return Z
with open('day24.txt', 'r') as inp:
    program = inp.readlines()

    universes = [(0, 0, 0, 0, 0, 0)]
    cnt = 1
    for op in program:
        op = op.strip().split(' ')
        print(op, cnt)

        if op[0] == 'inp':
            cnt += 1
            # remove duplicates since we are only interested in lowest and highest
            new_universes = {}
            for universe in universes:
                w, x, y, z = universe[W], universe[X], universe[Y], universe[Z]
                if (w, x, y, z) not in new_universes:
                    new_universes[(w, x, y, z)] = (universe[MIN], universe[MAX])
                else:
                    a = min(new_universes[(w, x, y, z)][0], universe[MIN])
                    b = max(new_universes[(w, x, y, z)][1], universe[MAX])
                    new_universes[(w, x, y, z)] = (a, b)
            universes = []
            for key, value in new_universes.items():
                universes.append((key[0], key[1], key[2], key[3], value[0], value[1]))


            # split into more universes
            new_universes = []
            for universe in universes:
                for i in range(1, 10):
                    new_universe = [universe[0], universe[1], universe[2], universe[3], universe[4], universe[5]]
                    new_universe[to_idx(op[1])] = i
                    new_universe[MIN] = new_universe[MIN] * 10 + i
                    new_universe[MAX] = new_universe[MAX] * 10 + i
                    new_universes.append(tuple(new_universe))
            universes = new_universes
        else:
            for i in range(len(universes)):
                if not op[2].isalpha():
                    second = int(op[2])
                else:
                    second = universes[i][to_idx(op[2])]
                tmp = list(universes[i])

                if op[0] == 'add':
                    tmp[to_idx(op[1])] += second
                elif op[0] =='mul':
                    tmp[to_idx(op[1])] *= second
                elif op[0] =='div':
                    tmp[to_idx(op[1])] //= second
                elif op[0] =='mod':
                    tmp[to_idx(op[1])] %= second
                elif op[0] =='eql':
                    tmp[to_idx(op[1])] = int(tmp[to_idx(op[1])] == second)

                universes[i] = tuple(tmp)
    ans = 0
    for universe in universes:
        if universe[Z] == 0:
            ans = max(ans, universe[MAX])
    print(ans)

    ans = 10 ** 24
    for universe in universes:
        if universe[Z] == 0:
            ans = min(ans, universe[MIN])
    print(ans)
