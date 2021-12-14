import re

with open('day10.txt', 'r') as inp:
    ans = {')': 0, ']': 0, '}': 0, '>': 0}
    bracket_convert = {')': '(', ']': '[', '}': '{', '>': '<'}
    part2_bracket_score = {'(': 1, '[': 2, '{': 3, '<': 4}

    part2 = []
    for line in re.findall(r'(.+)\n', inp.read()):
        stack = []
        for x in line:
            if x == '(' or x == '[' or x == '{' or x == '<':
                stack.append(x)
            else:
                if bracket_convert[x] != stack[-1]:
                    ans[x] += 1
                    stack = None
                    break
                else:
                    stack.pop()

        # part 2
        if stack != None:
            score = 0
            for s in stack[::-1]:
                score = score * 5 + part2_bracket_score[s]
            part2.append(score)

    print(ans[')'] * 3 + ans[']'] * 57 + ans['}'] * 1197 + ans['>'] * 25137)

    part2.sort()
    print(part2[len(part2)//2])
