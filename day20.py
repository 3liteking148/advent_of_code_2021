import re


def read(image, row, col, default):
    if 0 <= row < len(image) and 0 <= col < len(image[0]):
        return image[row][col]
    return default


border_color = '.'
def process(table, image):
    global border_color
    height, width = len(image) + 4, len(image[0]) + 4
    new_image = [['' for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            idx = 0
            for r in range(i-1, i+2):
                for c in range(j-1, j+2):
                    idx *= 2
                    idx += read(image, r - 2, c - 2, border_color) == '#'
            new_image[i][j] = table[idx]

    if table[0] == '#' and border_color == '.':
        border_color = '#'
    elif table[0] == '#' and border_color == '#':
        border_color = '.'

    return new_image


def count(image):
    ans = 0
    for row in ret:
        for pixel in row:
            ans += pixel == '#'
    return ans


with open('day20.txt') as inp:
    table, image = re.match(r'([.#]{512})\s+((?:[.#]+\n?)+)', inp.read()).groups()
    image = image.strip().split('\n')

    # part 1 (process 2 times)
    ret = process(table, image)
    ret = process(table, ret)
    print(count(ret))

    # part 2 (do it 48 more times)
    for i in range(48):
        ret = process(table, ret)

    print(count(ret))
