import numpy as np

fname = "input_day4.txt"
with open(fname) as f:
    lines = f.readlines()
    string = "\n".join(map(lambda s: " ".join([str(ord(letter)) for letter in s.strip()]), lines))
    print(string)
    input_matrix = np.matrix(string).reshape((len(lines), -1))
    print(input_matrix)

direction_dict = {
    "North": (-1, 0),
    "North-East": (-1, 1),
    "East": (0, 1),
    "South-East": (1, 1),
    "South": (1, 0),
    "South-West": (1, -1),
    "West": (0, -1),
    "North-West": (-1, -1)
}


def check(matrix, letter, dir, pos):
    direction = direction_dict.get(dir)
    x, y = pos
    x, y = pos[0] + direction[0], pos[1] + direction[1]
    if x < 0 or y < 0 or x > matrix.shape[0] - 1 or y > matrix.shape[1] - 1:
        print(x, y)
        return False
    return matrix[x, y] == ord(letter)


def find(matrix):
    result = []
    indices = np.where(matrix == ord("A"))
    positions = list(zip(indices[0], indices[1]))
    for pos in positions:
        temp = True
        # Check North-East diagonal (top-left to bottom-right)
        temp &= (check(matrix, "M", "North-East", pos) or check(matrix, "S", "North-East", pos))

        # Check South-West diagonal (bottom-left to top-right)
        temp &= (check(matrix, "M", "South-West", pos) or check(matrix, "S", "South-West", pos))

        # Check that there's no MM or SS on both diagonals
        temp &= not (check(matrix, "M", "North-East", pos) and check(matrix, "M", "South-West", pos))  # No MM
        temp &= not (check(matrix, "S", "North-East", pos) and check(matrix, "S", "South-West", pos))  # No SS

        # Check North-West diagonal (top-right to bottom-left)
        temp &= (check(matrix, "M", "North-West", pos) or check(matrix, "S", "North-West", pos))

        # Check South-East diagonal (bottom-right to top-left)
        temp &= (check(matrix, "M", "South-East", pos) or check(matrix, "S", "South-East", pos))

        # Ensure there's no MM or SS in the reverse diagonals as well
        temp &= not (check(matrix, "M", "North-West", pos) and check(matrix, "M", "South-East", pos))  # No MM
        temp &= not (check(matrix, "S", "North-West", pos) and check(matrix, "S", "South-East", pos))  # No SS
        result.append(temp)
        print(temp)
    return result

res = find(input_matrix)
print(res)
print(sum(res))
