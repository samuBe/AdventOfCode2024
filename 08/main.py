class Grid:

    def __init__(self, lines):
        self.grid = list(map(lambda line: [Cell(icon) for icon in line.rstrip()], lines))
        self.shape = (len(self.grid), len(self.grid[0]))

    def __str__(self):
        string = ""
        for row in self.grid:
            for cell in row:
                string += str(cell)
            string += "\n"
        return string

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
                    print(cell.icon)
        return total



    def test_in_bounds(self, pos):
        x, y = pos
        max_x, max_y = self.shape
        return x >= 0 and y >= 0 and x < max_x and y < max_y


    def start(self):
        # Get the unique icons
        icons = dict()

        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if cell.icon == '.':
                    continue
                elif cell.icon in icons:
                    icons[cell.icon].append((i, j))
                else:
                    icons[cell.icon] = [(i, j)]

        for icon in icons.keys():
            pos = icons[icon]
            for i in range(len(pos)):
                for j in range(i + 1, len(pos)):
                    change = ((pos[i][0] - pos[j][0]), (pos[i][1] - pos[j][1]))
                    k = 0
                    while k <100:
                        up = self.get((pos[i][0] + k * change[0], pos[i][1] + k * change[1]))
                        if up is not None:
                            up.visited = True
                            k += 1
                            if up.icon == '.':
                                up.icon = '#'
                        else:
                            k = 0
                            break
                    while k <100:
                        down = self.get((pos[j][0] - k * change[0], pos[j][1] - k * change[1]))
                        if down is not None:
                            down.visited = True
                            k += 1
                            if down.icon == '.':
                                down.icon = '#'
                        else:
                            break

class Cell:

    def __init__(self, icon):
        self.icon = icon
        self.visited = False

    def __str__(self):
        return self.icon

fname = "input.txt"
with open(fname) as f:
    lines = f.readlines()
    grid = Grid(lines)
    print(grid)
    grid.start()
    print(grid)
    answer = grid.get_visited()
    print(answer)

