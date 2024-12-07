import re
import itertools

input = open("07.txt", "r").read().splitlines()

# part 1

def parse(line):
    target,numbers = re.match(r"^(\d+): (.*)$", line).groups()
    target = int(target)
    numbers = [ int(i) for i in numbers.split(" ") ]
    return [target, numbers]

def result(numbers, combo):
    total = numbers[0]
    for number, op in zip(numbers[1:], combo):
        total = total + number if op == "+" else total * number
    return total

def possible(target, numbers):
    combos = itertools.product(["+", "*"], repeat=len(numbers)-1)
    for combo in combos:
        if result(numbers,combo) == target: return True
    return False

data = [ parse(line) for line in input ]

part1 = sum([ target for target, numbers in data if possible(target, numbers) ])
print(part1)

# part 2

def possible2(target, numbers):
    combos = itertools.product(["+", "*", "|"], repeat=len(numbers)-1)
    for combo in combos:
        if check(numbers,combo,target): return True
    return False

def check(numbers, combo, target):
    total = numbers[0]
    for number, op in zip(numbers[1:], combo):
        if op == "+":
            total += number
        elif op == "*":
            total *= number
        elif op == "|":
            total = int(str(total) + str(number))
        if total > target: return False
    if total == target: return True
    return False

part2 = sum([ target for target, numbers in data if possible2(target, numbers) ])
print(part2)