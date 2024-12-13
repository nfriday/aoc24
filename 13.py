import re

input = open("13.txt", "r").read().split("\n\n")

machines = []
for i in input:
    a,b,p = i.splitlines()
    ax,ay = re.search(r"X\+(\d+), Y\+(\d+)",a).groups()
    bx,by = re.search(r"X\+(\d+), Y\+(\d+)",b).groups()
    px,py = re.search(r"X=(\d+), Y=(\d+)",p).groups()
    machines.append([int(i) for i in (ax,ay,bx,by,px,py)])

def solve(ax,ay,bx,by,px,py):
    an = ( (bx * py) - (by * px) ) // ( (bx * ay) - (by * ax) )
    bn = ( px - (an * ax) ) // bx
    if not (an * ax + bn * bx == px and an * ay + bn * by == py): return False
    return (3 * an) +  bn

part1 = sum([solve(*m) for m in machines])
print(part1)

def big(machine):
    ax,ay,bx,by,px,py = machine
    return [ax,ay,bx,by,px+10000000000000,py+10000000000000]

part2 = sum([solve(*big(m)) for m in machines])
print(part2)