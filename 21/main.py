number_pad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]
direction_pad = [[None, "^", "A"], ["<", "v", ">"]]

INF = float('INF')


def get_minimum(nodes, visited):

    min = INF
    print(nodes)
    print(visited)
    for pos, dist in nodes.items():
        if pos in visited:
            continue
        if dist < min:
            min_pos = pos
            min = dist
    return min_pos


def manhattan(curr, end):
    return (abs(curr[1] - end[1]) + abs(curr[0] - end[0]) + 1)


def shortest_path(start, end, grids, level=0):
    current_x, current_y = start
    temp = 0
    visited = {(current_x, current_y)}
    nodes = dict()
    heuristic = dict()
    prev = dict()
    grid = grids[level]
    while (current_x, current_y) != end:

        # Go forward
        for dir_x, dir_y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = current_x + dir_x, current_y + dir_y
            print(nx, ny)
            print("end", end)
            print(current_x, current_y)
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] is not None:
                cost = 1
                print(level, cost)
                if temp + cost <= nodes.get((nx, ny), INF):
                    nodes[(nx, ny)] = temp + cost
                    heuristic[(nx, ny)] = temp + cost + manhattan(end, (nx, ny)) ** (4 - level)
                    prev[(nx, ny)] = (current_x, current_y)

        # Get the next node with the minimum cost
        current_x, current_y = get_minimum(heuristic, set(visited))
        temp = nodes[(current_x, current_y)]
        visited.add((current_x, current_y))

    # Generate the route
    curr = end
    route = ""
    while curr != start:
        temp = prev[curr]
        match (curr[0]-temp[0], curr[1]-temp[1]):
            case (-1, 0):
                route += "^"
            case (0, 1):
                route += ">"
            case (0, -1):
                route += "<"
            case (1, 0):
                route += "v"
        curr = temp

    route += "A"

    return route


def gen_dict(pad, grids, level):

    print(grids)
    dir = dict()
    for x_1, row_1 in enumerate(pad):
        for y_1, n_1 in enumerate(row_1):
            for x_2, row_2 in enumerate(pad):
                for y_2, n_2 in enumerate(row_2):
                    if n_1 is not None and n_2 is not None:
                        route = (n_1, n_2)
                        start = (x_1, y_1)
                        end = (x_2, y_2)
                        seq = shortest_path(start, end, grids, level)
                        dir[route] = seq

    return dir


def gen_seq(seq, dir):

    out = dir[('A', seq[0])]
    for i in range(len(seq)-1):
        out += dir[(seq[i], seq[i + 1])]

    return out


number_dir = gen_dict(number_pad, [number_pad] + [direction_pad for _ in range(3)], level=0)

fname = "example.txt"
with open(fname) as f:
    total = 0
    lines = f.readlines()
    for line in lines:
        seq = line.strip()
        final = gen_seq(seq, number_dir)
        print(len(final))
        print()


        complexity = int(seq[:-1]) * len(final)
        total += complexity
        print(total)

