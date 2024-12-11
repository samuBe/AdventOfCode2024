def transform(stone):

    if stone == 0:
        return [1]
    string_stone = str(stone)
    if len(string_stone) % 2 == 0:
        mid = len(string_stone)//2
        return [int(string_stone[:mid]), int(string_stone[mid:])]
    return [stone * 2024]


fname = "input.txt"

with open(fname) as f:
    input_string = f.read().strip()
    stones = map(int, input_string.split(" "))

total = 0
n = 35
for i in range(n):
    temp = []
    for stone in stones:
        ans = transform(stone)
        temp += ans
    stones = temp

print(len(stones))
