n = 75
cache = dict()


def transform(stone, start, total):
    if (stone, start) in cache:
        return cache[(stone, start)]
    if start >= n:
        return 1

    string_stone = str(stone)
    if stone == 0:
        if start>=n-1:
            return 1
        if start>n-5:
            return transform(2024, start + 2, total)
        return 2 * transform(2, start + 4, total) + transform(2024, start + 6, total) + transform(4, start + 4, total)
    if stone == 2:
        if start>n-4:
            return transform(4048, start + 1, total)
        return 2 * transform(4, start + 3, total) + transform(2024, start + 5, total) + transform(8, start + 3, total)
    if stone == 4:
        if start>n-4:
            return transform(8096, start + 1, total)
        return transform(8, start + 3, total) + transform(2024, start + 5, total) + transform(9, start + 3, total) + transform(6, start + 3, total)
    if len(string_stone) % 2 == 0:
        mid = len(string_stone)//2
        # here the total changes
        left_half = int(string_stone[:mid])
        right_half = int(string_stone[mid:])
        res= transform(left_half, start + 1, total) + transform(right_half, start + 1, total)
    else:
        res = transform(stone * 2024, start + 1, total)
    cache[(stone, start)] = res

    return res


fname = "input.txt"

with open(fname) as f:
    input_string = f.read().strip()
    stones = map(int, input_string.split(" "))

total = 0
for stone in stones:
    print(stone)
    total += transform(stone, 0, 1)

print(total)
