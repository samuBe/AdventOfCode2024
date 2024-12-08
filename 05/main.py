# Read in the priority graph and the updates
file_name = "test.txt"
with open(file_name) as f:
    lines = list(map(lambda line: line.rstrip(), f.readlines()))
    index = lines.index("")
    updates = list(map(lambda line: list(map(int, line.split(","))), lines[index + 1:]))
    priority_graph = dict()
    for line in lines[:index]:
        before, after = line.split("|")
        before, after = int(before), int(after)
        if before in priority_graph:
            priority_graph[before].add(after)
        else:
            priority_graph[before] = {after}


def compare(page_1, page_2, priority_graph):
    if page_1 in priority_graph and page_2 in priority_graph[page_1]:
        return 1
    if page_2 in priority_graph and page_1 in priority_graph[page_2]:
        return -1
    return 0


def re_order(update, priority_graph):
    correct = True
    length = len(update)
    for i in range(length):
        for j in range(i + 1, length):
            if compare(update[i], update[j], priority_graph) < 0:
                update[i], update[j] = update[j], update[i]
    return correct


def is_correct_priority(update, priority_graph):
    correct = True
    length = len(update)
    for i in range(length):
        for j in range(i + 1, length):
            if compare(update[i], update[j], priority_graph) < 0:
                return False
    return correct


def get_middle(updates):
    return updates[len(updates) // 2]


middle_numbers = list()
for update in updates:
    if not is_correct_priority(update, priority_graph):
        re_order(update, priority_graph)
        middle_numbers.append(get_middle(update))

answer = sum(middle_numbers)
print(answer)
