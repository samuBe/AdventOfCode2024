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
                    return Guard(pos, dir, self)


    def get(self, pos):
        x, y = pos
        if not self.test_in_bounds(pos):
            return None
        return self.grid[x][y]

    def get_visited(self):

        total = 0
        for row in self.grid:
            for cell in row:
                if cell.visited:
                    total += 1
        return total



    def test_in_bounds(self, pos):
        x, y = pos
        max_x, max_y = self.shape
        return x >= 0 and y >= 0 and x < max_x and y < max_y


    def start(self):

        guard = self.guard
        is_in_bounds = True

        while is_in_bounds:
            guard.forward()
            print(guard.pos)
            is_in_bounds = self.test_in_bounds(guard.pos)



class Cell:

    def __init__(self, icon):
        self.icon = icon
        self.obstacle = icon == '#'
        self.visited = False

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
            self.grid.get(self.pos).icon = "X"
            self.pos = newPos
            return

        if cell.obstacle:
            self.turn()
            print(self.dir)
        else:
            self.grid.get(self.pos).icon = "X"
            self.pos = newPos
            cell.visited = True
            cell.icon = "^"


fname = "input.txt"
with open(fname) as f:
    lines = f.readlines()
    grid = Grid(lines)
    print(grid.shape)
    print(grid.guard.pos)
    print(grid)
    grid.start()
    answer = grid.get_visited()
    print(answer)

