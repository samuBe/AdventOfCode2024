class Cell:

    def __init__(self, icon):
        self.icon = icon


def print_grid(grid):
    string = ""
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            string += cell.icon
        string += "\n"
    print(string)



instructions = {
        "^": (-1,0),
        ">": (0,1),
        "v": (1,0),
        "<": (0,-1),
        }


fname = "input.txt"
with open(fname) as f:
    lines = f.readlines()
    split = lines.index("\n")
    grid_lines = lines[:split]
    step_lines = lines[split + 1:]
    print(grid_lines)
    print(step_lines)

    step_string = "".join([line.strip() for line in step_lines])

    # Make the grid
    grid = [[Cell(el) for el in line.strip()] for line in grid_lines]

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell.icon == "@":
                robot_pos_x, robot_pos_y = i, j
                break
    print(robot_pos_x, robot_pos_y)

    for step in step_string:
        dir_x, dir_y = instructions[step]
        shift = []
        i = 0
        while True:
            el = grid[robot_pos_x + i * dir_x][robot_pos_y + i * dir_y]
            shift.append(el)
            i += 1
            if el.icon == ".":
                for i in range(len(shift) - 1, 0, -1):
                    shift[i].icon = shift[i - 1].icon
                grid[robot_pos_x][robot_pos_y].icon = "."
                robot_pos_x += dir_x
                robot_pos_y += dir_y
                break
            if el.icon == "#":
                break

    total = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell.icon == "O":
                score = 100 * i + j
                total += score

    print("Total: ", total)





