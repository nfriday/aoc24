input = [ int(i) for i in open("11.txt", "r").read().split(" ") ]

def parse(input):
    stones = {}
    for i in input:
        if i in stones:
            stones[i] += 1
        else:
            stones[i] = 1
    if 0 not in stones: stones[0] = 0
    if 1 not in stones: stones[1] = 0
    return stones

def dictadd(d,a,n):
    if a in d:
        d[a] += n
    else:
        d[a] = n

def blink(stones):
    new_stones = {}

    for i in stones:
        if i == 0:
            dictadd(new_stones,1,stones[i])
            continue

        str_stone = str(i)
        if len(str_stone) % 2 == 0:
            middle = len(str_stone) // 2
            a = int(str_stone[:middle])
            b = int(str_stone[middle:])
            dictadd(new_stones,a,stones[i])
            dictadd(new_stones,b,stones[i])
            continue

        dictadd(new_stones,i*2024,stones[i])    

    return new_stones


stones = parse(input)
for i in range(25): stones = blink(stones)
part1 = sum( [ stones[i] for i in stones ] )
print(part1)

stones = parse(input)
for i in range(75): stones = blink(stones)
part2 = sum( [ stones[i] for i in stones ] )
print(part2)