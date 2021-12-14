import re

'''
# process input to a list
timers = (lambda inp: [inp.count(str(i)) for i in range(9)])(re.findall(r'\b\d\b', open('day6.txt', 'r').read()))

# [days 0-5] + [day 6] + [day 7] + [day 8]
new_timers = lambda timers: timers[1:7] + [timers[7] + timers[0]] + [timers[8]] + [timers[0]]

# simulate lanternfish
fish = lambda day, timers: sum(timers) if day == 256 else fish(day+1, new_timers(timers))

print(fish(0, timers))
'''

print((lambda fish, day, timers: fish(fish, day, timers))(lambda fish, day, timers: sum(timers) if day ==  80 else fish(fish, day+1, timers[1:7] + [timers[7] + timers[0]] + [timers[8]] + [timers[0]]), 0, (lambda inp: [inp.count(str(i)) for i in range(9)])(re.findall(r'\b\d\b', open('day6.txt', 'r').read()))))
print((lambda fish, day, timers: fish(fish, day, timers))(lambda fish, day, timers: sum(timers) if day == 256 else fish(fish, day+1, timers[1:7] + [timers[7] + timers[0]] + [timers[8]] + [timers[0]]), 0, (lambda inp: [inp.count(str(i)) for i in range(9)])(re.findall(r'\b\d\b', open('day6.txt', 'r').read()))))
