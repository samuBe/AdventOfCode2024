direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def score(pos, grid):
    x, y = pos
    val = grid[x][y]
    if val == 9:
        return {pos}

    total = set()
    for dir in direction:
        newPos_x, newPos_y = x + dir[0], y + dir[1]
        if newPos_x < 0 or newPos_y < 0:
            continue
        try:
            new_val = grid[newPos_x][newPos_y]
            if new_val - val == 1:
                ans = (score((newPos_x, newPos_y), grid))
                total = total.union(ans)
        except:
            continue
    return total


fname = "input.txt"
with open(fname) as f:
    lines = f.readlines()
    grid = list(map(lambda line: [int(el) for el in line.strip()], lines))


total = 0
for i, row in enumerate(grid):
    for j, el in enumerate(row):
        if el == 0:
            ans = (score((i, j), grid))
            total += len(ans)

print(total)
