import itertools

input = [list(i) for i in open("08.txt", "r").read().splitlines()]

# part 1

row_count = len(input)
col_count = len(input[0])
anntenae_data = {}
for type,row,col in [ [input[row][col],row,col] for row in range(row_count) for col in range(col_count) if input[row][col] not in [".","#"] ]:
    if type not in anntenae_data:
        anntenae_data[type] = [[row,col]]
    else:
        anntenae_data[type].append([row,col])

def antinodes(a,b):
    ar, ac = a
    br, bc = b

    dr = br - ar
    dc = bc - ac

    antinodes = [
        [ar - dr, ac - dc],
        [br + dr, bc + dc]
    ]

    return [ [row,col] for row,col in antinodes
            if row >= 0 and col >= 0 and row < row_count and col < col_count ]

nodes = []
for _, anntenae in anntenae_data.items():
    for a,b in itertools.combinations(anntenae,2):
        for node in antinodes(a,b):
            if node not in nodes: nodes.append(node)

print(len(nodes))

# part 2

def antinodes2(a,b):
    ar, ac = a
    br, bc = b

    dr = br - ar
    dc = bc - ac

    antinodes = []

    i = 0
    while True:
        nr = br + i*dr
        nc = bc + i*dc
        if nr >= 0 and nc >= 0 and nr < row_count and nc < col_count:
            antinodes.append([nr,nc])
            i += 1
        else:
            break

    i = 0
    while True:
        nr = ar - i*dr
        nc = ac - i*dc
        if nr >= 0 and nc >= 0 and nr < row_count and nc < col_count:
            antinodes.append([nr,nc])
            i += 1
        else:
            break

    return antinodes

nodes = []
for _, anntenae in anntenae_data.items():
    for a,b in itertools.combinations(anntenae,2):
        for node in antinodes2(a,b):
            if node not in nodes: nodes.append(node)

print(len(nodes))