import sympy as sp

symbols = dict()


# Read in the input
fname = "input.txt"
with open(fname) as f:
    lines = f.readlines()
    index = lines.index("\n")

    inputs_lines = lines[:index]
    inputs = dict()
    for line in inputs_lines:
        name, val = line.split(':')
        inputs[name] = bool(int(val.strip()))
        
    print(inputs)

    outputs_lines = lines[index + 1:]
    outputs = dict()
    for line in outputs_lines:
        in_1, op, in_2, _, out = line.split(' ')
        out = out.strip()
        outputs[(in_1, in_2, op)] = out


def find(in1, in2, op):
    if (in1, in2, op) in outputs:
        return outputs[(in1, in2, op)]
    if (in2, in1, op) in outputs:
        return outputs[(in2, in1, op)]
    return None


def write(in1, in2, op, out):
    if (in1, in2, op) in outputs:
        outputs[(in1, in2, op)] = out
    if (in2, in1, op) in outputs:
        outputs[(in2, in1, op)] = out
    return None

n = 44
i = 0
swap = list()
out_1 = find('x00', 'y00', 'XOR')
out_5 = find('x00', 'y00', 'AND')
for i in range(1, n):
    carry = out_5
    in_1 = f"x{i:02}"
    in_2 = f"y{i:02}"
    out_1 = find(in_1, in_2, 'XOR')
    out_2 = find(carry, out_1, 'XOR')
    out_3 = find(in_1, in_2, 'AND')
    if out_2 is None:
        print(2 * "!!!!")
        swap_1 = out_1
        swap_2 = out_3
        temp = out_1
        out_1 = out_3
        out_3 = temp
        out_2 = find(carry, out_1, 'XOR')
        swap.append(swap_1)
        swap.append(swap_2)
    # check if out_2 is ok:
    if out_2 != f"z{i:02}":
        print(2 * "!!!!")
        out_4 = find(carry, out_1, 'AND')

        # Check if swapping out_2 and out_5 solves the problem
        if out_3 == f"z{i:02}":
            swap_1 = out_2
            swap_2 = out_3
            # write to output dictionary
            write(carry, out_1, 'XOR', out_3)
            write(in_1, in_2, 'AND', out_2)
            temp = out_3
            out_3 = out_2
            out_2 = temp

        if out_4 == f"z{i:02}":
            swap_1 = out_2
            swap_2 = out_4
            # write to output dictionary
            write(carry, out_1, 'XOR', out_4)
            write(carry, out_1, 'AND', out_2)
            out_2 = out_4

        out_5 = find(out_3, out_4, 'OR')
        # Check if swapping out_2 and out_5 solves the problem
        if out_5 == f"z{i:02}":
            swap_1 = out_2
            swap_2 = out_5
            # write to output dictionary
            write(carry, out_1, 'XOR', out_5)
            write(out_3, out_4, 'OR', out_2)
            out_2 = out_5

        # Add to swapping list
        swap.append(swap_1)
        swap.append(swap_2)

    out_4 = find(carry, out_1, 'AND')
    out_5 = find(out_3, out_4, 'OR')
    print(i, out_1, out_2, out_3, out_4, out_5)

print(','.join(sorted(swap)))

