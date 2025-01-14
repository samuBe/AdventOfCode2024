from collections import defaultdict

INF = float('inf')

def print_grid(grid):
    string = ""
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            string += grid[j][i]
        string += "\n"
    print(string)


def get_minimum(nodes, visited):

    min = INF
    for pos, dist in nodes.items():
        if pos in visited:
            continue
        if dist < min:
            min_pos = pos
            min = dist
    return min_pos


grid_x, grid_y = 7, 7 
fname = "example.txt"
with open(fname) as f:
    lines = f.readlines()
    # create the grid, nodes and get the starting point
    grid = [['.' for _ in range(grid_x)] for _ in range(grid_y)]
    nodes = dict()
    for line in lines[:12]:
        x, y = line.strip().split(',')
        x = int(x)
        y = int(y)
        grid[x][y] = '#'

print_grid(grid)

current_x = 0
current_y = 0
temp = 0
visited = {(current_x, current_y)}
prev = defaultdict(None)
while (current_x, current_y) != (grid_x - 1, grid_y - 1):

    # Go forward
    for dir_x, dir_y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = current_x + dir_x, current_y + dir_y
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != "#":
            if temp + 1 <= nodes.get((nx, ny), INF):
                nodes[(nx, ny)] = temp + 1
                prev[(nx, ny)] = (current_x, current_y)

    # Get the next node with the minimum cost
    current_x, current_y = get_minimum(nodes, visited)
    temp = nodes[(current_x, current_y)]
    visited.add((current_x, current_y))

answer = nodes[(current_x, current_y)]
print(answer)
print(prev)


# Count the number of paths
on_path = set()

def traverse_path(start):
    x, y = start
    grid[x][y] = 'o'
    on_path.add((x, y))
    temp = prev[start]
    if temp is None:
        return
    traverse_path(temp)


traverse_path((current_x, current_y))

print_grid(grid)

print(len(on_path))

