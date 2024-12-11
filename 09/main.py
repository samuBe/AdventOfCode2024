# Read the string
fname = "input.txt"
with open(fname) as f:
    string = f.read().strip()

print(string)

# construct the free space and id thing
file_system = []
free = False
id = 0
for num in string:
    if free:
        file_system += ['.'] * int(num)
    else:
        file_system += [id] * int(num)
        id += 1
    free = not free

# read from the back filling the space until back > front
start = 0
end = len(file_system) - 1
while end - start > 1:
    for i in range(start, end + 1):
        if file_system[i] == '.':
            start = i
            break
    for i in range(end, start, -1):
        if file_system[i] != '.':
            end = i
            break

    file_system[start], file_system[end] = file_system[end], file_system[start]
    print(start - end)
print(file_system)

# calculate the checksum
total = 0
for i, id in enumerate(file_system[:end]):
    total += i * id

print(total)
