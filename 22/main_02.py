from collections import defaultdict

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
    prices = []
    for line in lines:
        init = int(line.strip())
        price = [init % 10]
        for _ in range(2000):
            init = calc(init)
            price.append(init % 10)
        prices.append(price)

def get_sequence(price,start):
    return tuple((price[start + i + 1] - price[start + i]) for i in range(4))


total = defaultdict(lambda: 0)
for seller in prices:
    temp = dict()
    for start in range(len(seller)-4):
        seq = get_sequence(seller, start)
        if (seq not in temp):
            temp[seq] = seller[start + 4]

    # merge into total
    for seq in temp.keys():
        total[seq] += temp[seq]

ans = (max(total, key=total.get))
print(ans, total[ans])
