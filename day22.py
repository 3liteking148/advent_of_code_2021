import re

class Stats:
    def __init__(self, max_area):
        self.max_area = max_area
        self.prev_progress = -1
        self.progress = 0
    def add_area(self, x):
        self.progress += x
        percentage = self.progress / self.max_area * 100
        if  int(percentage) >= self.prev_progress + 1:
            print(f'{int(percentage)}%')
            self.prev_progress = int(percentage)

class Cube:
    def __init__(self, x1, x2, y1, y2, z1, z2):
        self.x1, self.y1, self.z1 = int(x1), int(y1), int(z1)
        self.x2, self.y2, self.z2 = int(x2), int(y2), int(z2)

    def split(self, x_midpoint=None, y_midpoint=None, z_midpoint=None):
        if x_midpoint != None:
            yield Cube(self.x1, x_midpoint, self.y1, self.y2, self.z1, self.z2)
            yield Cube(x_midpoint + 1, self.x2, self.y1, self.y2, self.z1, self.z2)
        elif y_midpoint != None:
            yield Cube(self.x1, self.x2, self.y1, y_midpoint, self.z1, self.z2)
            yield Cube(self.x1, self.x2, y_midpoint + 1, self.y2, self.z1, self.z2)
        elif z_midpoint != None:
            yield Cube(self.x1, self.x2, self.y1, self.y2, self.z1, z_midpoint)
            yield Cube(self.x1, self.x2, self.y1, self.y2, z_midpoint + 1, self.z2)

    def area(self):
        return (self.x2 - self.x1 + 1) * (self.y2 - self.y1 + 1) * (self.z2 - self.z1 + 1)
    def valid(self):
        return self.x1 <= self.x2 and self.y1 <= self.y2 and self.z1 <= self.z2

class Command:
    def __init__(self, type, cube):
        self.type = type
        self.cube = cube


def is_intersecting(cube1, cube2):
    return ((cube1.x1 <= cube2.x1 <= cube1.x2 or cube2.x1 <= cube1.x1 <= cube2.x2) and
                 (cube1.y1 <= cube2.y1 <= cube1.y2 or cube2.y1 <= cube1.y1 <= cube2.y2) and
                 (cube1.z1 <= cube2.z1 <= cube1.z2 or cube2.z1 <= cube1.z1 <= cube2.z2))

commands = []
stats = None
def check(cube, split_axis):
    global max_area, progress, tmp

    if not cube.valid():
        return 0

    #print(cube.x1, cube.x2, cube.y1, cube.y2, cube.z1, cube.z2, split_axis)
    on = 'off'
    for command in commands:
        # is the whole block inside the command area
        if (command.cube.x1 <= cube.x1 <= command.cube.x2 and
            command.cube.x1 <= cube.x2 <= command.cube.x2 and
            command.cube.y1 <= cube.y1 <= command.cube.y2 and
            command.cube.y1 <= cube.y2 <= command.cube.y2 and
            command.cube.z1 <= cube.z1 <= command.cube.z2 and
            command.cube.z1 <= cube.z2 <= command.cube.z2):
           on = command.type
        # if not, are the two blocks at least intersecting each other?
        elif not (cube.x1 == cube.x2 and cube.y1 == cube.y2 and cube.z1 == cube.z2) and (
        is_intersecting(cube, command.cube)):
             split_cubes = None
             if split_axis == 'x':
                 split_axis = 'y'
                 if cube.x1 == cube.x2:
                     split_cubes = (cube, )
                 if command.cube.x1 < cube.x1 and command.cube.x2 <= cube.x2:
                     split_cubes = cube.split(x_midpoint=command.cube.x2)
                 elif cube.x1 <= command.cube.x1 and cube.x2 < command.cube.x2:
                     split_cubes = cube.split(x_midpoint=command.cube.x1 - 1)
                 else:
                     split_cubes = cube.split(x_midpoint=((cube.x1 + cube.x2) // 2))
             elif split_axis == 'y':
                 split_axis = 'z'
                 if cube.y1 == cube.y2:
                     split_cubes = (cube, )
                 if command.cube.y1 < cube.y1 and command.cube.y2 <= cube.y2:
                     split_cubes = cube.split(y_midpoint=command.cube.y2)
                 elif cube.y1 <= command.cube.y1 and cube.y2 < command.cube.y2:
                     split_cubes = cube.split(y_midpoint=command.cube.y1 - 1)
                 else:
                     split_cubes = cube.split(y_midpoint=((cube.y1 + cube.y2) // 2))
             elif split_axis == 'z':
                 split_axis = 'x'
                 if cube.z1 == cube.z2:
                     split_cubes = (cube, )
                 if command.cube.z1 < cube.z1 and command.cube.z2 <= cube.z2:
                     split_cubes = cube.split(z_midpoint=command.cube.z2)
                 elif cube.z1 <= command.cube.z1 and cube.z2 < command.cube.z2:
                     split_cubes = cube.split(z_midpoint=command.cube.z1 - 1)
                 else:
                     split_cubes = cube.split(z_midpoint=((cube.z1 + cube.z2) // 2))
             ret = 0
             for split_cube in split_cubes:
                 ret += check(split_cube, split_axis)
             return ret

    if stats != None:
        stats.add_area(cube.area())

    if on == 'on':
        return cube.area()
    else:
        return 0

INT_MAX = (2 ** 31) - 1
INT_MIN = -(2 ** 31)
with open('day22.txt', 'r') as inp:
    raw_cmds = re.findall(r'(\w+) x=([-\d]+)\.\.([-\d]+),y=([-\d]+)\.\.([-\d]+),z=([-\d]+)\.\.([-\d]+)', inp.read())
    part1_bounds = Cube(-50, 50, -50, 50, -50, 50)
    part2_bounds = Cube(INT_MAX, INT_MIN, INT_MAX, INT_MIN, INT_MAX, INT_MIN)
    for raw_cmd in raw_cmds:
        type, coords = raw_cmd[0], tuple(int(num) for num in raw_cmd[1:])
        part2_bounds.x1 = min(part2_bounds.x1, coords[0])
        part2_bounds.x2 = max(part2_bounds.x2, coords[1])
        part2_bounds.y1 = min(part2_bounds.y1, coords[2])
        part2_bounds.y2 = max(part2_bounds.y2, coords[3])
        part2_bounds.z1 = min(part2_bounds.z1, coords[4])
        part2_bounds.z2 = max(part2_bounds.z2, coords[5])
        commands.append(Command(type, Cube(*coords)))

    #stats = Stats(part1_bounds.area())
    print(check(part1_bounds, 'x'))

    #stats = Stats(part2_bounds.area())
    print(check(part2_bounds, 'x'))
