import re

with open("input_day3.txt") as f:
    input_string = "".join(f.readlines())

#input_string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def get_mul(input_string):
    expr = r"mul\((\d+),(\d+)\)"
    matches = re.findall(expr, input_string)
    total = 0
    for match in matches:
        total += int(match[0]) * int(match[1])

    return total

# Run through the string
expr = r"(don\'t\(\)|do\(\))"
search_string = input_string
match = re.search(expr, search_string)
index = match.span()[1]
total = get_mul(search_string[:index + 1]) 
search_string = search_string[index:]
previous_match = match.group()
while True:
    match = re.search(expr, search_string)
    if match is None:
        break
    index = match.span()[1]
    if previous_match == "do()":
        total += get_mul(search_string[:index + 1])
    search_string = search_string[index:]
    previous_match = match.group()
    if len(search_string)<1:
        break
if previous_match == "do()":
    total += get_mul(search_string)


print(total)
