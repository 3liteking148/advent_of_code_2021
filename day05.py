import re


def swap_if_needed(pair):
    if pair[2] < pair[0]:
        return (pair[2], pair[3], pair[0], pair[1])
    else:
        return pair

def empty(points, pair):
    pass


def set_vertical(points, pair):
    for i in range(min(pair[1], pair[3]), max(pair[1], pair[3])+1):
        points.append((pair[0], i))


def set_horizontal(points, pair):
    for i in range(pair[0], pair[2]+1):
        points.append((i, pair[1]))


def set_diagonal(points, pair):
    m = (pair[3] - pair[1]) // (pair[2] - pair[0])
    for i in range(pair[2] - pair[0] + 1):
        points.append((pair[0]+i, pair[1]+(i*m)))


def get_final(matches, set_vertical, set_horizontal, set_diagonal):
    arr = {}
    for pair in matches:
        points = []
        pair = swap_if_needed(pair)
        if pair[0] == pair[2]: # vertical
            set_vertical(points, pair)
        elif pair[1] == pair[3]: # horizontal
            set_horizontal(points, pair)
        else:
            set_diagonal(points, pair)

        for p in points:
            if p[1] not in arr:
                arr[p[1]] = {p[0]: 0}
            elif p[0] not in arr[p[1]]:
                arr[p[1]][p[0]] = 0
            else:
                arr[p[1]][p[0]] = 1

    return sum([sum(arr[y].values()) for y in arr])


if __name__ == '__main__':
    with open('day5.txt') as file:
        text = file.read()
        matches = re.findall('(\d+),(\d+) -> (\d+),(\d+)', text)
        matches = [[int(k) for k in x] for x in matches]

        print(get_final(matches, set_vertical, set_horizontal, empty))
        print(get_final(matches, set_vertical, set_horizontal, set_diagonal))
