import re

input = open("03.txt", "r").read()

# part 1

part1 = sum([int(i.group(1)) * int(i.group(2)) for i in re.finditer(r'mul\((\d+),(\d+)\)',input)])
print(part1)

# part 2

enabled = True
part2 = 0
for i in re.finditer(r'(mul)\((\d+),(\d+)\)|(do(?:n\'t)?)\(\)',input):
    if i.group(4) == "do": enabled = True; continue
    if i.group(4) == "don't": enabled = False; continue
    if i.group(1) == "mul" and enabled:
        part2 += int(i.group(2)) * int(i.group(3))
print(part2)