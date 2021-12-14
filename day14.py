from functools import lru_cache
import re

rules: dict
alphabet: set

@lru_cache(maxsize=100000)
def test(i, i_max, a, b, letter):
    if i == i_max:
        return 0

    m = rules[(a, b)]
    ret = 0

    if m == letter:
        ret = 1

    ret += test(i+1, i_max, a, m, letter)
    ret += test(i+1, i_max, m, b, letter)
    return ret

def get_num_of_letter(letter, steps):
    ret = 0
    for i in range(len(start)-1):
        ret += (start[i] == letter)
        ret += test(0, steps, start[i], start[i+1], letter)

    # last element not part of prev loop
    ret += (start[-1] == letter)
    return ret

def solve(steps):
    minimum = 2 ** 64
    maximum = 0

    for letter in alphabet:
        num_of_letter = get_num_of_letter(letter, steps)
        minimum = min(minimum, num_of_letter)
        maximum = max(maximum, num_of_letter)

    print(maximum - minimum)

with open('day14.txt', 'r') as inp:
    text = inp.read()
    start = re.match('\w+', text)[0]
    rules = {x[0:2]: x[2] for x in re.findall('(\w)(\w) -> (\w)', text)}
    alphabet = set(re.findall('\w', text))

    solve(10)
    solve(40)
