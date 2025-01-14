

def mix(a, b):
    return a ^ b


def prune(a):
    return a & (2**24-1)


def one(a):
    return prune(mix(a, a << 6))


def two(a):
    return prune(mix(a, a >> 5))


def three(a):
    return prune(mix(a, a << 11))

def calc(a):
    return three(two(one(a)))

fname = "input.txt"
with open(fname) as f:
    lines = f.readlines()
    numbers = []
    for line in lines:
        init = int(line.strip())
        for _ in range(2000):
            init = calc(init)
        numbers.append(init)
    print(numbers)
    print(sum(numbers))
