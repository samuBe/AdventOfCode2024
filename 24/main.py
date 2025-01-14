import sympy as sp

symbols = dict()

def s(string):
    if string in symbols:
        return symbols[string]
    symbol = sp.symbols(string, bool=True)
    symbols[string] = symbol
    return symbol

def eq(a, b):
    pass

fname = "input.txt"
with open(fname) as f:
    lines = f.readlines()
    index = lines.index("\n")

    inputs_lines = lines[:index]
    inputs = dict()
    for line in inputs_lines:
        name, val = line.split(':')
        inputs[s(name)] = bool(int(val.strip()))
        
    print(inputs)

    outputs_lines = lines[index + 1:]
    outputs = dict()
    output_constraints = list()
    for line in outputs_lines:
        in_1, op, in_2, _, out = line.split(' ')
        out = out.strip()
        match op:
            case "XOR":
                expr = sp.logic.boolalg.Equivalent(s(out), s(in_1) ^ s(in_2))
            case "AND":
                expr = sp.logic.boolalg.Equivalent(s(out), s(in_1) & s(in_2))
            case "OR":
                expr = sp.logic.boolalg.Equivalent(s(out), s(in_1) | s(in_2))
        print(expr)
        output_constraints.append(expr)
        if out[0] == 'z':
            outputs[out] = expr

    constraints = sp.logic.boolalg.And(*output_constraints)
    sol = (sp.logic.inference.satisfiable(constraints.subs(inputs)))
    print(sol)

    result = 0
    for i, key in enumerate(sorted(outputs.keys())):
        print(key, sol[s(key)])
        result += (2**i) * sol[s(key)]

print(result)
