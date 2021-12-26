import math
import re


class Node:
    def __init__(self, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right


def extract(seq, node):
    depth = 0
    for i, c in enumerate(seq):
        if c == ',' and depth == 1:
            node2 = Node(parent=node)
            node2.left = extract(seq[1:i], node2)
            node2.right = extract(seq[i+1:-1], node2)
            return node2
        elif c == '[':
            depth += 1
        elif c == ']':
            depth -= 1

    return int(seq)


def get_child(node, target):
    if target == 'left':
        return node.left
    elif target == 'right':
        return node.right


def add_to_child(node, target, x):
    if target == 'left':
        node.left += x
    elif target == 'right':
        node.right += x


def explode(node, target):
    add = get_child(node, target)
    prev = node
    node = node.parent
    while node is not None and get_child(node, target) == prev:
        prev = node
        node = node.parent
    if node is not None:
        if type(get_child(node, target)) == int:
            add_to_child(node, target, add)
        else:
            node = get_child(node, target)

            # switch direction after 1 move
            if target == 'left':
                target = 'right'
            elif target == 'right':
                target = 'left'

            while type(node) == Node and type(get_child(node, target)) == Node:
                node = get_child(node, target)
            add_to_child(node, target, add)


def get_magnitude(node, debug=False):
    if type(node) == int:
        return node

    if debug:
        left_side = get_magnitude(node.left, debug)
        right_side = get_magnitude(node.right, debug)
        return '[{},{}]'.format(left_side, right_side)
    return 3 * get_magnitude(node.left) + 2 * get_magnitude(node.right)


def snailfish_math(p, depth, target):
    side = 'left'

    for node in (p.left, p.right):
        if target == 0 and type(node) == Node and depth == 3:
            #print("explode", node.left, node.right)
            explode(node, 'left')
            explode(node, 'right')
            if side == 'left':
                p.left = 0
            else:
                p.right = 0
            #print(get_magnitude(node, debug=True))
            return 1
        elif target == 1 and type(node) == int and node >= 10:  # if leaf
            #print('split', node)
            left = math.floor(node / 2)
            right = math.ceil(node / 2)

            if side == 'left':
                p.left = Node(left=left, right=right, parent=p)
            else:
                p.right = Node(left=left, right=right, parent=p)
            #print(get_magnitude(node, debug=True))
            return 1
        elif type(node) == Node:
            # return immediately after an operation is performed
            if snailfish_math(node, depth+1, target) != 0:
                return 1
        side = 'right'
    return 0


def snailfish_add(node):
    exploded, split = 1, 1
    while exploded == 1 or split == 1:
        while exploded == 1:
            exploded = snailfish_math(node, 0, 0)
        split = snailfish_math(node, 0, 1)
        exploded = snailfish_math(node, 0, 0)  # explode again


with open('day18.txt', 'r') as inp:
    numbers = re.findall(r'(.*)\n', inp.read())

    node = Node()
    node.left = extract(numbers[0], node)
    node.right = extract(numbers[1], node)

    snailfish_add(node)
    for i in range(2, len(numbers)):
        node = Node(left=node)
        node.left.parent = node
        node.right = extract(numbers[i], node)

        snailfish_add(node)

    # part 1
    print(get_magnitude(node))

    best = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            node = Node()
            node.left = extract(numbers[i], node)
            node.right = extract(numbers[j], node)

            snailfish_add(node)
            best = max(best, get_magnitude(node))

    # part 2
    print(best)
