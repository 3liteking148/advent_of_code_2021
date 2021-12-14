from functools import reduce

print((lambda xy: xy[0] * xy[1])(reduce((lambda xy, cmd: (xy[0] + cmd[1], xy[1]) if cmd[0] == 'forward' else (xy[0], xy[1] - cmd[1]) if cmd[0] == 'up' else (xy[0], xy[1] + cmd[1]) if cmd[0] == 'down' else None), [(0,0)] + [(x.split(' ')[0], int(x.split(' ')[1])) for x in open('day2.txt', 'r')])))
print((lambda xya: xya[0] * xya[1])(reduce((lambda xya, cmd: (xya[0] + cmd[1], xya[1] + xya[2] * cmd[1], xya[2]) if cmd[0] == 'forward' else (xya[0], xya[1], xya[2] - cmd[1]) if cmd[0] == 'up' else (xya[0], xya[1], xya[2] + cmd[1]) if cmd[0] == 'down' else None), [(0,0,0)] + [(x.split(' ')[0], int(x.split(' ')[1])) for x in open('day2.txt', 'r')])))
