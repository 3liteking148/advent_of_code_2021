from functools import reduce
'''
# stripped input
input_stripped = [l.strip() for l in open('day3.txt', 'r')]

for part 1:
# [# of lines/rows, # of 1s in column 1, # of 1s in column 2, etc]
input_processed = (lambda inp: [len(inp)] + [sum([int(l[i]) for l in inp]) for i in range(len(inp[0]))])(input_stripped)

for part 2:
lambda f, cmp, i, l
f - function
cmp - comparison function
i - column number
l - input_stripped
'''

print(( lambda l: reduce(lambda a, b: 2 * a + (b / l[0] >= 0.5), [0] + l[1:]) * reduce(lambda a, b: 2 * a + (b / l[0] < 0.5), [0] + l[1:]) )( (lambda inp: [len(inp)] + [sum([int(l[i]) for l in inp]) for i in range(len(inp[0]))])([l.strip() for l in open('day3.txt', 'r')] ) ))
print(( lambda f, l: int('0b'+f(f, lambda a, b: a == b, 0, l), 2) * int('0b'+f(f, lambda a, b: a != b, 0, l), 2))((lambda f, cmp, i, l: f(f, cmp, i + 1, [x for x in l if cmp(int(x[i % len(l[0])]), int(sum([int(k[i % len(l[0])]) for k in l]) / len(l) >= 0.5))]) if len(l) > 1 else l[0]), ([l.strip() for l in open('day3.txt', 'r')] )))
