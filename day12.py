from copy import deepcopy
import re

def dfs(adj_list, small_visited, p, visit_twice_allowed):
    if p == 'end':
        return 1

    ret = 0
    for q in adj_list[p]:
        if q == 'start':
            continue

        # dont consider if we are not allowed to visit a small cave twice
        if visit_twice_allowed == False and small_visited.get(q, 0) >= 1:
            continue

        # visit this node if we are allowed to visit one small cave twice
        if visit_twice_allowed == True and small_visited.get(q, 0) == 1:
            # only allowed to visit one small cave twice
            visit_twice_allowed = False

        if q != 'end' and q.islower():
            small_visited[q] += 1
            ret += dfs(adj_list, small_visited, q, visit_twice_allowed)
            small_visited[q] -= 1
        else:
            ret += dfs(adj_list, small_visited, q, visit_twice_allowed)

        # restore state
        if small_visited.get(q, 0) == 1:
            visit_twice_allowed = True

    return ret

if __name__ == '__main__':
    with open('day12.txt', 'r') as inp:
        edges = re.findall('(\w+)-(\w+)', inp.read())
        adj_list = {e[0]: [] for e in edges}
        adj_list.update({e[1]: [] for e in edges})

        for e in edges:
            adj_list[e[0]].append(e[1])
            adj_list[e[1]].append(e[0])

        small_visited = {}
        for key in adj_list:
            if key.islower():
                small_visited[key] = 0

        print(dfs(adj_list, deepcopy(small_visited), 'start', False))
        print(dfs(adj_list, deepcopy(small_visited), 'start', True))
