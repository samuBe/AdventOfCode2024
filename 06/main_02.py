class Grid:

    def __init__(self, lines):
        self.grid = list(map(lambda line: [Cell(icon) for icon in line.rstrip()], lines))
        self.guard = self.get_guard()
        self.shape = (len(self.grid), len(self.grid[0]))

    def __str__(self):
        string = ""
        for row in self.grid:
            for cell in row:
                string += str(cell)
            string += "\n"
        return string

    def get_guard(self):

        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if cell.icon == "^":
                    pos = (i, j)
                    dir = (-1, 0)
                    cell.visited = True
                    cell.dir_visited = dir
                    return Guard(pos, dir, self)

    def get(self, pos):
        x, y = pos
        if not self.test_in_bounds(pos):
            return None
        return self.grid[x][y]

    def get_possible(self):

        total = 0
        for row in self.grid:
            for cell in row:
                if cell.possible:
                    total += 1
        return total

    def test_in_bounds(self, pos):
        x, y = pos
        max_x, max_y = self.shape
        return x >= 0 and y >= 0 and x < max_x and y < max_y

    def start(self):
        guard = self.guard
        is_in_bounds = True
        route = list()

        while is_in_bounds:
            route.append((guard.pos, guard.dir))
            guard.forward()
            is_in_bounds = self.test_in_bounds(guard.pos)

        return route


class Cell:

    def __init__(self, icon):
        self.icon = icon
        self.obstacle = icon == '#' or icon == 'O'
        self.visited = False
        self.possible = False
        self.dir_visited = None

    def __str__(self):
        return self.icon


class Guard:

    def __init__(self, pos, direction, grid):

        self.pos = pos
        self.dir = direction
        self.grid = grid

    def turn(self):
        x, y = self.dir
        self.dir = (y, -x)

    def forward(self):
        newPos_x = self.pos[0] + self.dir[0]
        newPos_y = self.pos[1] + self.dir[1]
        newPos = (newPos_x, newPos_y)
        cell = self.grid.get(newPos)
        if cell is None:
            self.pos = newPos
            return None

        if cell.obstacle:
            self.turn()
        else:
            self.pos = newPos
        return self.pos


fname = "input.txt"
with open(fname) as f:
    lines = f.readlines()
    grid = Grid(lines)
    print(grid.shape)
    print(grid.guard.pos)
    orig_p = grid.guard.pos
    orig_d = grid.guard.dir
    print(grid)
    route = grid.start()
    t = set()
    for temp in route:
        pos, dir = temp
        new_pos_x, new_pos_y = pos[0] + dir[0], pos[1] + dir[1]
        if not grid.test_in_bounds((new_pos_x, new_pos_y)):
            break
        if grid.grid[new_pos_x][new_pos_y].icon == '#':
            continue
        grid.grid[new_pos_x][new_pos_y] = Cell('O')
        grid.guard = Guard(orig_p, orig_d, grid)
        is_in_bounds = True
        visited = set()
        while is_in_bounds:
            visited.add((grid.guard.pos, grid.guard.dir))
            grid.guard.forward()
            is_in_bounds = grid.test_in_bounds(grid.guard.pos)
            if grid.guard.pos is None:
                break
            if grid.guard.pos is not None and (grid.guard.pos, grid.guard.dir) in visited:
                print(grid)
                t.add((new_pos_x, new_pos_y))
                break
        grid.grid[new_pos_x][new_pos_y] = Cell('.')

    print(t)
    print(len(t))
