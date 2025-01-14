class Cell:

    def __init__(self, icon):
        self.icon = icon


def print_grid(grid):
    string = ""
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            string += cell
        string += "\n"
    print(string)

def build_shift(dir, start, grid):

    start_x, start_y = start
    dir_x, dir_y = dir
    add = [(start_x, start_y)]
    match grid[start_x][start_y]:
        case "@":
            temp = build_shift(dir, (start_x + dir_x, start_y + dir_y), grid)
            if temp is None:
                return None
            add += temp
        case "[":
            add += [(start_x, start_y + 1)]
            # Do some checks if None
            temp1 = build_shift(dir, (start_x + dir_x, start_y + dir_y), grid)
            temp2 = build_shift(dir, (start_x + dir_x, start_y + dir_y + 1), grid)
            if temp1 is None or temp2 is None:
                return None
            add += temp1
            add += temp2

        case "]":
            add += [(start_x, start_y - 1)]
            # Do some checks if None
            temp1 = build_shift(dir, (start_x + dir_x, start_y + dir_y), grid)
            temp2 = build_shift(dir, (start_x + dir_x, start_y + dir_y - 1), grid)
            if temp1 is None or temp2 is None:
                return None
            add += temp1
            add += temp2
        case ".":
            add = []
        case "#":
            add = None

    return add



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
    grid = [[(el) for el in line.strip().replace("#","##").replace("O", "[]").replace(".", "..").replace("@","@.")] for line in grid_lines]

    print_grid(grid)

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "@":
                print(cell)
                robot_pos_x, robot_pos_y = i, j
                break
    print(robot_pos_x, robot_pos_y)


    for step in step_string:
        print(step)
        dir = instructions[step]
        dir_x, dir_y = dir
        match step:
            case "^" | "v":
                # Build the shift list recursively
                robot_pos = (robot_pos_x, robot_pos_y)
                shift = build_shift(dir, robot_pos, grid)
            case ">" | "<":
                # Loop until you have . or #
                i = 0
                shift = []
                while True:
                    cur_x = robot_pos_x + i * dir_x
                    cur_y = robot_pos_y + i * dir_y
                    el = grid[cur_x][cur_y]
                    i += 1
                    if el == ".":
                        break
                    if el == "#":
                        shift = []
                        break
                    shift.append((cur_x, cur_y))
        if shift is None or len(shift) == 0:
            continue

        robot_pos_x += dir_x
        robot_pos_y += dir_y
        # sort shift so that it accounts for the direction
        shift_sorted = sorted(list(set(shift)), key=lambda tupL: tupL[0] * dir_x + tupL[1] * dir_y, reverse=True)
        for pos_x, pos_y in shift_sorted:
            old = grid[pos_x][pos_y]
            grid[pos_x][pos_y] = '.'
            grid[pos_x + dir_x][pos_y + dir_y] = old


    print_grid(grid)
    total = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "[":
                score = 100 * i + j
                total += score

    print("Total: ", total)
