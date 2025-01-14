INF = float('inf')
grid_x, grid_y = 71, 71


def print_grid(grid):
    string = ""
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            string += grid[j][i]
        string += "\n"
    print(string)


def get_minimum(nodes, visited):

    min = INF
    min_pos = None
    for pos, dist in nodes.items():
        if pos in visited:
            continue
        if dist < min:
            min_pos = pos
            min = dist
    return min_pos


def shortest_path(grid):
    current_x = 0
    current_y = 0
    temp = 0
    visited = {(current_x, current_y)}
    nodes = dict()
    while (current_x, current_y) != (grid_x - 1, grid_y - 1):

        # Go forward
        for dir_x, dir_y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = current_x + dir_x, current_y + dir_y
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != "#":
                if temp + 1 <= nodes.get((nx, ny), INF):
                    nodes[(nx, ny)] = temp + 1

        # Get the next node with the minimum cost
        current = get_minimum(nodes, visited)
        if current is None:
            return None
        current_x, current_y = current
        temp = nodes[(current_x, current_y)]
        visited.add((current_x, current_y))
        if (current_x, current_y) == (grid_x - 1, grid_y - 1):
            return nodes[(current_x, current_y)]
    return None

def create_grid(index, lines):
    grid = [['.' for _ in range(grid_x)] for _ in range(grid_y)]
    for i, line in enumerate(lines[:index]):
        x, y = line.strip().split(',')
        x = int(x)
        y = int(y)
        grid[x][y] = '#'
    return grid


fname = "input.txt"
with open(fname) as f:
    lines = f.readlines()
    start = 0
    end = len(lines)
    while start < end:
        print(start, end)
        index = (start + end) // 2
        grid = create_grid(index, lines)
        dist = shortest_path(grid)
        if dist is None:
            end = index - 1
            answer = index
        else:
            start = index + 1

    print(lines[index])





