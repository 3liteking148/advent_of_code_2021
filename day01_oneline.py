print((lambda inp: sum([1 for x, y in zip(inp, inp[1:]) if y > x]))([int(x.strip()) for x in open("day1.txt", "r")]))
print((lambda inp: sum([1 for x, y in (lambda l: zip(l, l[1:]))([x + y + z for x, y, z in zip(inp, inp[1:], inp[2:])]) if y > x]))([int(x.strip()) for x in open("day1.txt", "r")]))
