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
for j, stone in enumerate(stones):
    temp = [stone]
    for i in range(25):
        temp2 = []
        for s in temp:
            ans = transform(s)
            temp2 += ans
        temp = temp2
    total += len(temp)

print(total)




