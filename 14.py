import re

input = open("14.txt", "r").read().splitlines()

data = [ [int(i) for i in re.search(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)",line).groups()] for line in input ]

def get_pos(startx,starty,vx,vy,width,height,time):
    x = (startx + (vx * time)) % width
    y = (starty + (vy * time)) % height
    return (x,y)

width = 101
height = 103

# part 1

positions = [ get_pos(*i,width,height,100) for i in data ]

midx = width // 2
midy = height // 2

quad1 = [ (x,y) for x,y in positions if x < midx and y < midy ]
quad2 = [ (x,y) for x,y in positions if x < midx and y > midy ]
quad3 = [ (x,y) for x,y in positions if x > midx and y < midy ]
quad4 = [ (x,y) for x,y in positions if x > midx and y > midy ]

part1 = len(quad1) * len(quad2) * len(quad3) * len(quad4)
print(part1)

# part 2

def printgrid(positions):
    for y in range(0,height,3):
        for x in range(0,width,3):
            print("." if (x,y) not in positions else "O",end="",flush=False)
        print("\n",end="",flush=False)
    print("\n",flush=True)

def surrounded(pos,positions):
    x,y = pos
    neighbours = [
        (x-1,y-1),(x-1,y),(x-1,y+1),
        (x,y-1),(x,y+1),
        (x+1,y-1),(x+1,y),(x+1,y+1)
    ]
    for n in neighbours:
        if n not in positions: return False
    return True

# i literally just brute-force check for any position
# which contains a robot surrounded by 8 other robots
# and print the result hoping to find a pattern that looks
# like a christmas tree ...
for t in range(7000,10000):
    positions = [ get_pos(*i,width,height,t) for i in data ]
    valid = False
    for pos in positions:
        if surrounded(pos,positions):
            valid = True
            break
    if valid:
        printgrid(positions)
        print(t)