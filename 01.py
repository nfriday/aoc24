input = open("01.txt", "r").read().splitlines()

data = [ i.split("   ") for i in input ]
list1, list2 = [ [int(j) for j in sorted(list(i))] for i in zip(*data) ]

# part 1

part1 = sum([ abs(i-j) for i,j in zip(list1,list2) ])
print(part1)

# part 2

part2 = sum([ i * list2.count(i) for i in list1 ])
print(part2)