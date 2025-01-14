from collections import defaultdict


# Get shortest route
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

def manhattan(end, start):
    xe, ye = end
    xs, ys = start
    return abs(xs - xe) + abs(ye - ys)


def shortest_path(start, end, grid):
    current_x, current_y = start
    temp = 0
    visited = {(current_x, current_y)}
    nodes = dict()
    heur = dict()
    prev = dict()
    while (current_x, current_y) != end:

        # Go forward
        for dir_x, dir_y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = current_x + dir_x, current_y + dir_y
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '#':
                cost = temp + manhattan(end, (nx, ny))
                if cost <= nodes.get((nx, ny), INF):
                    nodes[(nx, ny)] = temp + 1
                    heur[(nx, ny)] = cost
                    prev[(nx, ny)] = (current_x, current_y)

        # Get the next node with the minimum cost
        current_x, current_y = get_minimum(heur, set(visited))
        temp = nodes[(current_x, current_y)]
        visited.add((current_x, current_y))

    # Generate the route
    curr = end
    route = [end]
    while curr != start:
        temp = prev[curr]
        route.insert(0, temp)
        curr = temp

    return route


# Read the grid
fname = "input.txt"
with open(fname) as f:
    lines = list(map(lambda line: line.strip(), f.readlines()))
    grid = []
    for y in range(len(lines)):
        temp = []
        for x in range(len(lines[0])):
            el = lines[y][x].strip()
            if el == 'S':
                start = (y, x)
            if el == 'E':
                end = (y, x)
            temp.append(el)
        grid.append(temp)


threshold = 20
# Generate the shortest route
route = shortest_path(start, end, grid)
print(route)
# for each pair of points, check the manhattan distance and if lower than threshold, skip ahead
savings = defaultdict(lambda: 0)

for i, step in enumerate(route):
    for j in range(i + 1, len(route)):
        step2 = route[j]
        cost = manhattan(step, step2)
        if cost <= threshold:
            saving = j - i - cost
            savings[saving] += 1

print(list(map(lambda key: f"{key}: {savings[key]}", filter(lambda key: key >= 50, savings.keys()))))
answer = sum(map(lambda key: savings[key], filter(lambda key: key >= 100, savings.keys())))
print(answer)

