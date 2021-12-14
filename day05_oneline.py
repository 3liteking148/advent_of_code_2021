import re
from functools import reduce

'''
# More verbose version

set_vertical = lambda pair: ((pair[0], i) for i in range(min(pair[1], pair[3]), max(pair[1], pair[3])+1))
set_horizontal = lambda pair: ((i, pair[1]) for i in range(pair[0], pair[2]+1))
set_diagonal = lambda pair: ((pair[0]+i, pair[1]+(i*(pair[3] - pair[1]) // (pair[2] - pair[0]))) for i in range(pair[2] - pair[0] + 1))

# eval('None or dict') equals dict
update_sets = lambda dict, keys: dict.update({k: 1 if k in dict else 0 for k in keys}) or dict

def get_final(dict, matches, set_vertical, set_horizontal, set_diagonal):
    if len(matches) == 0:
        return sum(dict.values())

    keys = set_vertical(matches[-1]) if matches[-1][0] == matches[-1][2] else set_horizontal(matches[-1]) if matches[-1][1] == matches[-1][3] else set_diagonal(matches[-1])
    return get_final(update_sets(dict, keys), matches[0:-1], set_vertical, set_horizontal, set_diagonal)

if __name__ == '__main__':
    matches = (lambda text, sort: [sort([int(k) for k in x]) for x in re.findall('(\d+),(\d+) -> (\d+),(\d+)', text)])(open('day5.txt').read(), lambda pair: (pair[2], pair[3], pair[0], pair[1]) if pair[2] < pair[0] else pair)
    print(get_final({}, matches, set_vertical, set_horizontal, lambda pair: {}))
    print(get_final({}, matches, set_vertical, set_horizontal, set_diagonal))
'''

print((lambda get_final, matches: get_final(get_final, {}, matches, lambda pair: ((pair[0], i) for i in range(min(pair[1], pair[3]), max(pair[1], pair[3])+1)), lambda pair: ((i, pair[1]) for i in range(pair[0], pair[2]+1)), lambda pair: {}))((lambda get_final, dict, matches, set_vertical, set_horizontal, set_diagonal: sum(dict.values()) if len(matches) == 0 else get_final(get_final, (lambda dict, keys: dict.update({k: 1 if k in dict else 0 for k in keys}) or dict)(dict, set_vertical(matches[-1]) if matches[-1][0] == matches[-1][2] else set_horizontal(matches[-1]) if matches[-1][1] == matches[-1][3] else set_diagonal(matches[-1])), matches[0:-1], set_vertical, set_horizontal, set_diagonal)), (lambda text, sort: [sort([int(k) for k in x]) for x in re.findall('(\d+),(\d+) -> (\d+),(\d+)', text)])(open('day5.txt').read(), lambda pair: (pair[2], pair[3], pair[0], pair[1]) if pair[2] < pair[0] else pair)))
print((lambda get_final, matches: get_final(get_final, {}, matches, lambda pair: ((pair[0], i) for i in range(min(pair[1], pair[3]), max(pair[1], pair[3])+1)), lambda pair: ((i, pair[1]) for i in range(pair[0], pair[2]+1)), lambda pair: ((pair[0]+i, pair[1]+(i*(pair[3] - pair[1]) // (pair[2] - pair[0]))) for i in range(pair[2] - pair[0] + 1))))((lambda get_final, dict, matches, set_vertical, set_horizontal, set_diagonal: sum(dict.values()) if len(matches) == 0 else get_final(get_final, (lambda dict, keys: dict.update({k: 1 if k in dict else 0 for k in keys}) or dict)(dict, set_vertical(matches[-1]) if matches[-1][0] == matches[-1][2] else set_horizontal(matches[-1]) if matches[-1][1] == matches[-1][3] else set_diagonal(matches[-1])), matches[0:-1], set_vertical, set_horizontal, set_diagonal)), (lambda text, sort: [sort([int(k) for k in x]) for x in re.findall('(\d+),(\d+) -> (\d+),(\d+)', text)])(open('day5.txt').read(), lambda pair: (pair[2], pair[3], pair[0], pair[1]) if pair[2] < pair[0] else pair)))
