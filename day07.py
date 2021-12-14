import re


if __name__ == '__main__':
    with open('day7.txt', 'r') as inp:
        crabs = [int(x) for x in re.findall(r'\b\d+\b', inp.read())]

        best = 2 ** 32
        for i in range(min(crabs), max(crabs) + 1):
            best = min(best, sum([abs(x - i) for x in crabs]))
        print(best)

        fuel = [0]
        for i in range(1, max(crabs) - min(crabs) + 1):
            fuel.append(fuel[i-1] + i)

        best = 2 ** 32
        for i in range(min(crabs), max(crabs) + 1):
            best = min(best, sum([fuel[abs(x - i)] for x in crabs]))
        print(best)
