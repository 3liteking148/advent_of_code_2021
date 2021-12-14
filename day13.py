import re

def fold(dir, mid, points):
    ret = {}
    for x, y in points:
        if dir == 'x' and x > mid:
            x = mid - (x - mid)
        elif dir == 'y' and y > mid:
            y = mid - (y - mid)

        if x >= 0 and y >= 0:
            ret[(x, y)] = 1
    return ret

if __name__ == '__main__':
    with open('day13.txt', 'r') as inp:
        text = inp.read()
        coords = re.findall(r'(\d+),(\d+)\n', text)
        cmds = re.findall(r'((?<=fold along ).)=(\d+)', text)
        dict = {(int(x), int(y)): 1 for x, y in coords}

        print(len(fold(cmds[0][0], int(cmds[0][1]), dict)))

        for c in cmds:
            dict = fold(c[0], int(c[1]), dict)

        w = max([x + 1 for x, y in dict])
        h = max([y + 1 for x, y in dict])

        for y in range(h):
            for x in range(w):
                if (x, y) in dict:
                    print('█', end='')
                else:
                    print(' ', end='')
            print()
