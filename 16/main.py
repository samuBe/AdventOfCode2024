from collections import defaultdict

INF = float('inf')


def get_minimum(nodes, visited):

    min = INF
    for pos, dist in nodes.items():
        if pos in visited:
            continue
        if dist < min:
            min_pos = pos
            min = dist
    return min_pos


fname = "input.txt"
with open(fname) as f:
    lines = f.readlines()
    # create the grid, nodes and get the starting point
    grid = []
    nodes = dict()
    for x in range(len(lines[0].strip())):
        temp = []
        for y in range(len(lines)):
            icon = lines[y][x]
            temp.append(icon)
            if icon == "S":
                nodes[(x, y, 1, 0)] = 0
                current_x = x
                current_y = y
                dir_x = 1
                dir_y = 0
        grid.append(temp)

visited = {(current_x, current_y)}
prev = defaultdict(set)
while grid[current_x][current_y] != "E":

    temp = nodes[(current_x, current_y, dir_x, dir_y)]

    # Go forward
    nx, ny = current_x + dir_x, current_y + dir_y
    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != "#":
        if temp + 1 == nodes.get((nx, ny, dir_x, dir_y), INF):
            nodes[(nx, ny, dir_x, dir_y)] = temp + 1
            prev[(nx, ny, dir_x, dir_y)].add((current_x, current_y, dir_x, dir_y))
        if temp + 1 < nodes.get((nx, ny, dir_x, dir_y), INF):
            nodes[(nx, ny, dir_x, dir_y)] = temp + 1
            prev[(nx, ny, dir_x, dir_y)] = {(current_x, current_y, dir_x, dir_y)}

    # Turn
    for l in (-1, 1):
        new_dir_x = l * dir_y
        new_dir_y = - l * dir_x
        if temp + 1000 == nodes.get((current_x, current_y, new_dir_x, new_dir_y), INF):
            nodes[(current_x, current_y, new_dir_x, new_dir_y)] = temp + 1000
            prev[(current_x, current_y, new_dir_x, new_dir_y)].add((current_x, current_y, dir_x, dir_y))
        if temp + 1000 < nodes.get((current_x, current_y, new_dir_x, new_dir_y), INF):
            nodes[(current_x, current_y, new_dir_x, new_dir_y)] = temp + 1000
            prev[(current_x, current_y, new_dir_x, new_dir_y)] = {(current_x, current_y, dir_x, dir_y)}

    # Get the next node with the minimum cost
    current_x, current_y, dir_x, dir_y = get_minimum(nodes, visited)
    visited.add((current_x, current_y, dir_x, dir_y))

answer = nodes[(current_x, current_y, dir_x, dir_y)]
print(answer)
print(prev)


# Count the number of paths
on_path = set()

def traverse_path(start):
    x, y, _, _ = start
    on_path.add((x, y))
    temp = prev[start]
    for s in temp:
        traverse_path(s)


traverse_path((current_x, current_y, dir_x, dir_y))

print(len(on_path))

