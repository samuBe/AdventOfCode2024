# Read the string
fname = "input.txt"
with open(fname) as f:
    string = f.read().strip()
# 

# Read in free space and files
file_system = []
id = 0
for i, num in enumerate(string):
    if i % 2==0:
        file_system.append((id, int(num)))
        id += 1
    else:
        file_system.append(('.', int(num)))

def find_free(file_system, size):
    for i, free in enumerate(file_system):
        if free[0] == '.' and size<=free[1]:
            return i
    return -1


# Start from the back of files
for id in range(len(file_system)-1, 0, -1):
    # find the first free space that is smaller than the filesize and subtract it
    file = file_system[id]
    name, size = file
    if name != '.':
        insert = find_free(file_system[:id], size)
        if insert > 0:
            file_system[insert] = ('.', file_system[insert][1] - size)
            file_system[id] = ('.', size)
            file_system.insert(insert, file)

# calculate the checksum
total = 0
id = 0
for file in file_system:
    name, size = file
    if name != '.':
        for _ in range(size):
            total += name * id
            id += 1
    else:
        id += size

print(total)
