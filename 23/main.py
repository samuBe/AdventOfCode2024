fname = "input.txt"
with open(fname) as f:
    lines = f.readlines()
    vertices = map(lambda line: tuple(sorted(line.strip().split('-'))), lines)
    graph = set(vertices)
    nodes = sorted(list(set([node for vertex in graph for node in vertex])))
    print(graph)
    print(nodes)

    thing = set()
    for vertex in graph:
        fro, to = vertex
        for node in nodes:
            if node == fro or node == to:
                continue
            if tuple(sorted((fro,node))) in graph and tuple(sorted((to, node))) in graph:
                thing.add(tuple(sorted([fro, to, node])))

    print(thing)

    smaller_thing = list()
    for cycle in thing:
        for node in cycle:
            if node[0] == 't':
                smaller_thing.append(cycle)
                break
    print(len(smaller_thing))

    max = 0
    max_v = None
    for node in nodes:
        thing = [node]
        for node_2 in nodes:
            if node_2 in thing:
                continue

            add = True
            for t in thing:
                add &= tuple(sorted([t, node_2])) in graph
                if not add:
                    break
            if add:
                thing.append(node_2)

        print(thing)
        if len(thing)> max:
            max = len(thing)
            max_v = thing

print(','.join(sorted(max_v)))
