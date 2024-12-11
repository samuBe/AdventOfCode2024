# Read the string
fname = "input.txt"
with open(fname) as f:
    string = f.read().strip()
# 
file_system = []

# Read in free space and files
free = list(map(int, ))
files = list(map(int, ))

# Start from the back of files
for id, file in enumerate(file[::-1]):
    # find the first free space that is smaller than the filesize and subtract it
    # fill in the free space with the ids
    pass


# calculate the checksum
total = 0
for i, id in enumerate(file_system):
    if id == '.':
        continue
    total += i * id

print(total)
