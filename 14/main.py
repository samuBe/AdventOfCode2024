import re
from numpy import log

width = 101
mid_x = width // 2
num_x = width // 13
height = 103
mid_y = height // 2
num_y = width // 13


grid = height * [width * [" "]]
print(len(grid))
print(len(grid[0]))

class Robot:

    def __init__(self, pos, v):
        self.pos = pos
        self.v = v

    def simulate(self, t):
        new_pos_x = (self.pos[0] + t * self.v[0]) % width
        new_pos_y = (self.pos[1] + t * self.v[1]) % height
        # Account for teleportation
        self.pos = (new_pos_x, new_pos_y)

    def get_quadrant(self):
        pos_x, pos_y = self.pos
        if pos_x  > mid_x and pos_y > mid_y:
            return 3
        if pos_x  > mid_x and pos_y < mid_y:
            return 2
        if pos_x  < mid_x and pos_y > mid_y:
            return 1
        if pos_x  < mid_x and pos_y < mid_y:
            return 0
        return None

    def get_box(self):
        pos_x, pos_y = self.pos
        return num_x * (pos_y // 13) + (pos_x // 13)


expr_pos = r"p=(\d+),(\d+)"
def get_pos(line):
    return list(map(int, re.findall(expr_pos, line)[0]))


expr_v = r"v=(-?\d+),(-?\d+)"
def get_v(line):
    return list(map(int, re.findall(expr_v, line)[0]))

# Read in the positions
fname = "input.txt"
with open(fname) as f:
    lines = f.readlines()
    robots = [Robot(get_pos(line), get_v(line)) for line in lines]

# count the robots per quadrant
quadrants = 4 * [0]
for robot in robots:
    #robot.simulate(100)
    q = robot.get_quadrant()
    if q is not None:
        quadrants[q] += 1

print(quadrants)
tot = 1
for num in quadrants:
    tot *= num
print(tot)

def show_grid(robots):
    grid = height * [width * [" "]]
    print(grid)
    for robot in robots:
        x, y = robot.pos
        temp = list(grid[y])
        temp[x] = "#"
        grid[y] = temp

    string = ""
    for row in grid:
        for cell in row:
            string += cell
        string += "\n"
    print(string)


num_robots = len(robots)
entropy = []
min_entropy = 10
index = 0
for i in range(10000):
    grid = (num_x + 1) * (num_y + 1)*[0]
    for robot in robots:
        robot.simulate(1)
        grid[robot.get_box()] += 1

    ent = 0
    for box in grid:
        if box != 0:
            ent += -box/num_robots * log(box/num_robots)
    entropy.append(ent)
    if ent < min_entropy:
        print(ent)
        min_entropy = ent
        index = i
        show_grid(robots)

print(index + 1)
print(min(entropy))

import matplotlib.pyplot as plt
plt.plot(entropy)
plt.plot(index, entropy[index], "g*")
plt.show()
