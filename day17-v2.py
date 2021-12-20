import math
import re
from interval import interval

def get_zero(a, b, c):
    if a != 0:
        if b * b - 4 * a * c < 0:
            return None
        zero1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
        zero2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)

        # in this problem we only want the smaller number
        return min(zero1, zero2)
    else:
        return -c / b

def get_eq(x):
    # (n(n+1)) - ((n-x)(n-x+1)) / 2
    # (n^2 + n - (n^2 - nx + n - nx + x^2 - x)) / 2
    # (2nx - x^2 + x) / 2
    a = 0
    b = x
    c = (-(x * x) + x) / 2
    return (a, b, c)

def get_eq_2(n):
    # (n(n+1)) - ((n-x)(n-x+1)) / 2
    # (n^2 + n - (n^2 - nx + n - nx + x^2 - x)) / 2
    # (2nx - x^2 + x) / 2
    a = -1 / 2
    b = (1 + 2*n) / 2
    c = 0
    return (a, b, c)

def poly_subt(poly1, poly2):
    return tuple(poly1[i] - poly2[i] for i in range(3))

def get_steps(x):
    if x == 0:
        return interval()

    test = poly_subt(get_eq(x), (0, 0, y0))
    test2 = poly_subt(get_eq(x), (0, 0, y1))
    b = get_zero(*test)
    a = get_zero(*test2)

    if math.ceil(a) > math.floor(b):
        c = interval()
    else:
        c = interval[math.ceil(a) - 1, math.floor(b) + 1]
    return c

def get_x_steps(x):
    test = poly_subt(get_eq_2(x), (0, 0, x0))
    test2 = poly_subt(get_eq_2(x), (0, 0, x1))
    a = get_zero(*test)
    b = get_zero(*test2)

    if b == None:
        b = y1 * -1 * 2 + 2

    if a == None or math.ceil(a) > math.floor(b):
        c = None
    else:
        c = (math.ceil(a), math.floor(b))
    return c

def interval2startend(x):
    start = int(x.extrema[0][0])
    if len(x.extrema) == 1:
        end = int(x.extrema[0][0])
    else:
        end = int(x.extrema[1][0])
    return start, end

'''
   1
 2   3
4 5 6 7
'''
SEGTREE_SIZE = 2
def fill_segtree(tree, i):
    if i >= SEGTREE_SIZE:
        tree[i] = get_steps(i - SEGTREE_SIZE)
        return tree[i]

    tree[i] = fill_segtree(tree, i*2) | fill_segtree(tree, i*2+1)
    return tree[i]

def get_range(tree, i, query_start, query_end):
    a = i
    b = i + 1
    while a < SEGTREE_SIZE:
        a *= 2
        b *= 2
    b -= 1
    #print(a, b)

    if query_start > b or query_end < a:
        return interval()

    if query_start <= a and b <= query_end:
        #print(query_start, query_end, "in", a, b)
        return tree[i]
    else:
        a = get_range(tree, i*2, query_start, query_end)
        b = get_range(tree, i*2+1, query_start, query_end)
        return a | b


def get_range_wrapper(tree, i, query_start, query_end):
    return get_range(tree, i, query_start + SEGTREE_SIZE, query_end + SEGTREE_SIZE)

cache = {}
with open('day17.txt', 'r+') as inp:
    capture = re.match(r'target area: x=(\d+)\.\.(\d+), y=([-\d]+)\.\.([-\d]+)', inp.read()).groups()
    x0, x1, y1, y0 = (int(x) for x in capture)

    # set segment tree size
    while SEGTREE_SIZE < y1 * -1 * 2 + 2:
        SEGTREE_SIZE *= 2

    # create segment tree
    tree = [0 for _ in range(SEGTREE_SIZE * 2)]
    print("[DEBUG] empty segment tree created")

    # fill segment tree
    fill_segtree(tree, 1)
    print("[DEBUG] segment tree filled")

    get_range(tree, 1, 0, 0)

    part1 = 0
    ans = 0
    for x in range(x1 + 1):
        test = get_x_steps(x)
        if test == None:
            continue

        start, end = test
        if (start, end) not in cache:
            out = get_range_wrapper(tree, 1, start, end)
            #print(start, end)

            k = 0
            for c in out.components:
                start1, end1 = interval2startend(c)
                part1 = max(part1, end1-1)
                k += end1 - start1 - 1
            cache[(start, end)] = k

        ans += cache[(start, end)]
    print((part1 * part1 + part1) // 2)
    print(ans)
