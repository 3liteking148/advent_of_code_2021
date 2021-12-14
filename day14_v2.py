import re


# A class that stores the quantity of each letter
class Counter:
    def __init__(self, initial=None):
        if initial is not None:
            self.counter = {initial: 1}
        else:
            self.counter = {}

    def add(self, counter):
        for key, value in counter.counter.items():
            self.counter[key] = self.counter.get(key, 0) + value

    def max(self):
        return max(self.counter.values())

    def min(self):
        return min(self.counter.values())


# table[(i, 'A', 'B')] contains the quantity of
# each letter in between 'A' and 'B' after i steps
def compute_table(alphabet, rules):
    table = {}

    # base case
    for a in alphabet:
        for b in alphabet:
            table[(0, a, b)] = Counter()

    # compute rest of table
    for i in range(1, 41):
        for a in alphabet:
            for b in alphabet:
                middle = rules[(a, b)]
                table[(i, a, b)] = Counter(middle)
                table[(i, a, b)].add(table[(i - 1, a, middle)])
                table[(i, a, b)].add(table[(i - 1, middle, b)])

    return table


def calculate(table, initial, steps):
    counter = Counter(initial[-1])  # last letter wont be added by the for loop
    for i in range(len(initial) - 1):
        counter.add(Counter(initial[i]))
        counter.add(table[(steps, initial[i], initial[i+1])])

    return counter.max() - counter.min()


with open('day14.txt', 'r') as inp:
    text = inp.read()
    initial = re.match('\w+', text)[0]

    alphabet = set(re.findall('\w', text))
    rules = {x[0:2]: x[2] for x in re.findall('(\w)(\w) -> (\w)', text)}
    table = compute_table(alphabet, rules)

    print(calculate(table, initial, 10))
    print(calculate(table, initial, 40))
