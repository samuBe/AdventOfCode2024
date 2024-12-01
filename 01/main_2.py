with open("input.txt") as f:
    counter = dict()
    l = list()
    for line in f.readlines():
        temp = line.rstrip().split(" ")
        first = (int(temp[0]))
        second = (int(temp[-1]))
        if counter.get(first) is None:
            counter[first] = 0
        counter[second] = counter.get(second, 0) + 1
        l.append(first)
    dist = sum(map(lambda val: val * counter[val], l))
    print(dist)
