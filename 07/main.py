def f(num1, num2, op):
    if op == '*':
        return num1 * num2
    elif op == '+':
        return num1 + num2
    elif op == '|':
        return int(str(num1) + str(num2))


def eval(numbers, operators):
    temp = f(numbers[0], numbers[1], operators[0])

    for i in range(1, len(operators)):
        temp = f(temp, numbers[i + 1], operators[i])
    return temp


fname = "input.txt"
with open(fname) as file:
    lines = file.readlines()
    total = 0
    for line in lines:
        test, rest = line.split(':')
        test = int(test)
        numbers = list(map(int, rest.strip().split(' ')))
        print(numbers, test)
        possible = [[]]
        for _ in range(len(numbers) - 1):
            temp = []
            for p in possible:
                temp.append(p + ['*'])
                temp.append(p + ['+'])
                temp.append(p + ['|'])
            possible = temp
        for p in possible:
            number = eval(numbers, p)
            if number == test:
                total += test
                break


print(total)
