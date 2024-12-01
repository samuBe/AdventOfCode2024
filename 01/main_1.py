with open("test.txt") as f:
    first = list()
    second = list()
    for line in f.readlines():
        temp = line.rstrip().split(" ")
        first.append(int(temp[0]))
        second.append(int(temp[-1]))
    dist = sum(map(lambda pair: abs(pair[0]-pair[1]), zip(sorted(first), sorted(second))))
    print(dist)
