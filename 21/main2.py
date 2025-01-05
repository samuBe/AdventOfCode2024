from collections import defaultdict

number_pad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]
direction_pad = [[None, "^", "A"], ["<", "v", ">"]]

INF = float('INF')


def get_minimum(nodes, visited):

    min = INF
    for pos, dist in nodes.items():
        if pos in visited:
            continue
        if dist < min:
            min_pos = pos
            min = dist
    return min_pos


def manhattan(curr, end):
    return (abs(curr[1] - end[1]) + abs(curr[0] - end[0]) + 1)


def get_prev(start, end, grid):
    current_x, current_y = start
    temp = 0
    visited = {(current_x, current_y)}
    nodes = dict()
    prev = defaultdict(set)
    while len(visited)!= len(grid) * len(grid[0]) - 1:

        # Go forward
        for dir_x, dir_y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = current_x + dir_x, current_y + dir_y
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] is not None:
                if temp + 1 == nodes.get((nx, ny), INF):
                    nodes[(nx, ny)] = temp + 1
                    prev[(nx, ny)].add((current_x, current_y))
                if temp + 1 < nodes.get((nx, ny), INF):
                    nodes[(nx, ny)] = temp + 1
                    prev[(nx, ny)] = {(current_x, current_y)}

        # Get the next node with the minimum cost
        current_x, current_y = get_minimum(nodes, visited)
        temp = nodes[(current_x, current_y)]
        visited.add((current_x, current_y))

    return prev

def shortest_path(start, end, grid):

    if start == end:
        return ['A']

    prev = get_prev(start, end, grid)
    route_to = {end: ['A']}
    gen_route(prev, end, start, route_to)
    return route_to[start]



def gen_route(prev, end, start, route_to = dict()):

    # Generate the route
    curr = end
    previous = prev[curr]
    for p in previous:
        match (curr[0]-p[0], curr[1]-p[1]):
            case (-1, 0):
                add = "^"
            case (0, 1):
                add = ">"
            case (0, -1):
                add = "<"
            case (1, 0):
                add = "v"

        if p not in route_to:
            route_to[p] = []

        for route in route_to[curr]:
            route_to[p].append(add + route)

        if p != start:
            gen_route(prev, p, start, route_to)


def gen_dict(pad):

    dir = dict()
    for x_1, row_1 in enumerate(pad):
        for y_1, n_1 in enumerate(row_1):
            for x_2, row_2 in enumerate(pad):
                for y_2, n_2 in enumerate(row_2):
                    if n_1 is not None and n_2 is not None:
                        route = (n_1, n_2)
                        start = (x_1, y_1)
                        end = (x_2, y_2)
                        seq = shortest_path(start, end, pad)
                        dir[route] = seq

    return dir

def gen_seq(seq, dir):

    out = dir[("A", seq[0])]
    for i in range(len(seq)-1):
        out += dir[(seq[i], seq[i + 1])]
    return out

dir_dir = gen_dict(direction_pad)
# Combine into a dictionary by checking the best path

cache = dict()
def cost(start, end, i, dir):
    if (start, end, i) in cache:
        return cache[(start, end, i)]
    if start == end:
        return 1
    if i == 0:
        return 1

    seqs = dir[(start, end)]
    c = min([cost("A", seq[0], i-1, dir) + sum([cost(seq[j], seq[j + 1], i-1, dir) for j in range(len(seq)-1)]) for seq in seqs])
    cache[(start, end, i)] = c
    return c

n = 25
cost_dict = dict()
for k in dir_dir.keys():
    start, end = k
    print(start, end)
    cost_dict[k] = cost(start, end, n, dir_dir)
print(cost_dict)

# Recursively build the cost here with caching
dir_dir_optimized = dict()
for key, val in dir_dir.items():
    min_length = INF
    min_p = None
    for seq in val:
        temp = dir_dir[("A", seq[0])]
        for i in range(len(seq)-1):
            sub_seqs = dir_dir[(seq[i], seq[i + 1])]
            temp2 = []
            for sub_seq in sub_seqs:
                for t in temp:
                    temp2.append(t + sub_seq)
            temp = temp2
        min_seq = min(temp, key=lambda seq: len(seq))
        if len(min_seq) < min_length:
            min_p = seq
    dir_dir_optimized[key] = min_p

n = 25
cost_dict = dict()
for k in dir_dir_optimized.keys():
    start, end = k
    print(start, end)
    cost_dict[k] = cost(start, end, n, dir_dir_optimized)
print(cost_dict)


number_dir = gen_dict(number_pad)
# Combine into a new dictionary by checking the best path

number_dir_cost = dict()
for key, val in number_dir.items():
    min_cost = INF
    for path in val:
        cost = cost_dict[("A", path[0])]
        for i in range(len(path)-1):
            cost += cost_dict[(path[i], path[i + 1])]
        if cost < min_cost:
            min_cost = cost
    number_dir_cost[key] = min_cost

fname = "input.txt"
with open(fname) as f:
    total = 0
    lines = f.readlines()
    for line in lines:
        seq = line.strip()
        cost = number_dir_cost[("A", seq[0])]
        for i in range(len(seq) - 1):
            cost += number_dir_cost[(seq[i], seq[i + 1])]
        print("cost", cost)

        complexity = int(seq[:-1]) * cost
        total += complexity
    print(total)

