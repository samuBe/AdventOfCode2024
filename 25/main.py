fname = "input.txt"
with open(fname) as f:
    lines = f.readlines()


keys = []
locks = []
block = []
max_h = 5
def count_h(block):
    # create the add the lock/key
    temp = []
    for j in range(len(block[0])):
        count = 0
        for i in range(len(block)):
            count += (block[i][j] == '#')
        temp.append(count - 1)
    return temp


for line in lines:

    if line == "\n":
        # create the add the lock/key
        temp = count_h(block)
        if block[0][0] == '.':
            keys.append(temp)
        else:
            locks.append(temp)

        block = []
    else:
        block.append([char for char in line.strip()])

temp = count_h(block)
if block[0][0] == '.':
    keys.append(temp)
else:
    locks.append(temp)


print(keys)
print(locks)


count = 0
for key in keys:
    for lock in locks:
        succes = True
        for i in range(len(key)):
            succes &= key[i] + lock[i] <= max_h
            if not succes:
                break
        count += int(succes)
print(count)


