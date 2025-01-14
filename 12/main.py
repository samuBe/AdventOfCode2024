directions = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

def build_region(start, grid, region):
    x, y = start
    plant = grid[x][y]
    for dir in directions:
        dir_x, dir_y = dir
        new_pos_x = x + dir_x
        new_pos_y = y + dir_y
        new_pos = (new_pos_x, new_pos_y)
        if new_pos_x < 0 or new_pos_y < 0:
            continue
        try:
            cell = grid[new_pos_x][new_pos_y]
            if cell is None:
                continue
            if new_pos in region:
                continue
            if cell == plant:
                # Add neighbor to region and search for its neighbors
                region.add(new_pos)
                build_region(new_pos, grid, region)

        except Exception as e:
            continue
    return region




def get_regions(grid):
    regions = list()
    visited = set()

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if (i, j) in visited:
                continue
            else:
                region = build_region((i, j), grid, {(i, j)})
                regions.append(region)
                visited = visited.union(region)

    return regions

def get_area(region):
    return len(region)

def get_perimeter(region):

    perimeter = 0
    for cell in region:
        x, y = cell
        neighbors = 0
        for dir in directions:
            dir_x, dir_y = dir
            neighbors += ((x+dir_x, y+dir_y) in region)
        perimeter += (4 - neighbors)
    return perimeter

def get_sides(region, grid):

    sides = 0

    # Get the bounding box
    upper_bound = min(region, key=lambda cell: cell[0])[0]
    lower_bound = max(region, key=lambda cell: cell[0])[0]
    left_bound = min(region, key=lambda cell: cell[1])[1]
    right_bound = max(region, key=lambda cell: cell[1])[1]

    # Check from left to right
    for i in range(left_bound, right_bound + 1):
        val = False
        for j in range(upper_bound, lower_bound + 1):
            temp = (j, i) in region and (j, i - 1) not in region
            if temp and not val:
                sides += 1
            val = temp

    print(sides)

    # check from right to left
    for i in range(right_bound + 1, left_bound - 1, -1):
        val = False
        for j in range(upper_bound, lower_bound + 1):
            temp = (j, i) in region and (j, i + 1) not in region
            if temp and not val:
                sides += 1
            val = temp

    print(sides)

    # check from left to right
    for i in range(upper_bound, lower_bound + 1):
        val = False
        for j in range(left_bound, right_bound + 1):
            temp = (i, j) in region and (i - 1, j) not in region
            if temp and not val:
                sides += 1
            val = temp
    print(sides)

    # check from bottom to top
    for i in range(lower_bound, upper_bound - 1, -1):
        val = False
        for j in range(left_bound, right_bound + 1):
            temp = (i, j) in region and (i + 1, j) not in region
            if temp and not val:
                sides += 1
            val = temp
    print(sides)

    return sides

# Read the grid
fname = "input.txt"
with open(fname) as f:
    lines = f.readlines()
    grid = list(map(lambda line: [cell for cell in line.strip()], lines))
print(grid)

# Get the regions
regions = get_regions(grid)
print(regions)

# For each region
# Get the area (count the number of plots)
# Get the perimeter (4 - the number of neighbors)
total = 0
for region in regions:
    area = get_area(region)
    perimeter = get_perimeter(region)
    sides = get_sides(region, grid)
    total += (area * sides)
    print(region, area, perimeter, sides)
print(total)

