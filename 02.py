input = open("02.txt", "r").read().splitlines()

data = [ [int(j) for j in i.split(" ")] for i in input ]

# part 1

def safe(x):
    increasing = x[-1] > x[0]
    for a,b in zip(x[:-1],x[1:]):
        if not 1 <= abs(a-b) <= 3 or (b > a) != increasing:
            return False
    return True

part1 = len([i for i in data if safe(i)])
print(part1)

# part 2

def safe2(x):

    if safe(x):
        return True
    
    for i in range(0,len(x)):
        if safe(x[:i] + x[i+1:]):
            return True
    
    return False

part2 = len([i for i in data if safe2(i)])
print(part2)
