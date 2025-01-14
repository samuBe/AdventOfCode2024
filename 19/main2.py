import re

# Binary tree pointing to the beginning of the letter

def find_i (char):

    match char:
        case 'b':
            return 0
        case 'g':
            return 1
        case 'r':
            return 2
        case 'u':
            return 3
        case 'w':
            return 4

class Tree:

    def __init__(self):
        self.children = [None] * 5
        self.end = False

    def insert(self, word):
        child = self
        for i in range(len(word)):
            temp = child.children[find_i(word[i])]
            if temp is None:
                temp = Tree()
                child.children[find_i(word[i])] = temp
            child = temp
        child.end = True


    def search(self, word):
        child = self
        for i in range(len(word)):
            temp = child.children[find_i(word[i])]
            if temp is None:
                return False
            child = temp
        return child.end


    def find_suffix(self, word):
        curr = self
        for i in range(len(word)):
            temp = curr.children[find_i(word[i])]
            if temp is None:
                return None

            if temp.end:
                yield word[i+1:]
            curr = temp

        return None



fname = "input.txt"
with open(fname) as f:
    lines = f.readlines()

    tree = Tree()
    patterns = sorted(re.sub(r'\s+', '', lines[0].strip()).split(','))
    print(patterns)

    for p in patterns:
        tree.insert(p)

    designs = list(map(lambda line: line.strip(), lines[2:]))
    print(designs)

# implement some sort of cache
cache = dict()
def count(design):
    if design is None:
        return 0
    if len(design) == 0:
        return 1
    if design in cache:
        return cache[design]
    match_generator = tree.find_suffix(design)
    sum_ = 0
    for match in match_generator:
        if match is not None:
            sum_ += count(match)
    cache[design] = sum_
    return sum_


total = 0
for design in designs:
    print(design, ":")
    total += count(design)
    print(total)

print(total)
