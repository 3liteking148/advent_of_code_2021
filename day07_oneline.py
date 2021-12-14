from functools import reduce
import re

'''
crabs = [int(x) for x in re.findall(r'\b\d+\b', open('day7.txt', 'r').read())]

part1_gen = (lambda crabs: (sum((abs(x - i) for x in crabs)) for i in range(min(crabs), max(crabs) + 1)))(crabs)
print(reduce(lambda a, b: a if a < b else b, part1_gen))

fuel = (lambda arr: [sum(arr[0:i]) for i in range(1, 3000)])([i for i in range(3000)])
# OR
fuel = [i*(i+1)/2 for i in range(3000)]

part2_gen = (lambda crabs: (sum([abs(x - i) * (abs(x - i) + 1) // 2 for x in crabs]) for i in range(min(crabs), max(crabs) + 1)))(crabs)
print(reduce(lambda a, b: a if a < b else b, part2_gen))
'''

print(reduce(lambda a, b: a if a < b else b, (lambda crabs: (sum([abs(x - i) for x in crabs]) for i in range(min(crabs), max(crabs) + 1)))([int(x) for x in re.findall(r'\b\d+\b', open('day7.txt', 'r').read())])))
print(reduce(lambda a, b: a if a < b else b, (lambda crabs: (sum([abs(x - i) * (abs(x - i) + 1) // 2 for x in crabs]) for i in range(min(crabs), max(crabs) + 1)))([int(x) for x in re.findall(r'\b\d+\b', open('day7.txt', 'r').read())])))
