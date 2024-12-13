input = [ list(i) for i in open("12.txt", "r").read().splitlines() ]

max_row = len(input) - 1
max_col = len(input[0]) - 1

plots = {}

def neighbours(pos):
    r,c = pos
    return [
        (nr,nc) for nr,nc in [ (r+1,c), (r-1,c), (r,c+1), (r,c-1) ]
        if 0 <= nr <= max_row and 0 <= nc <= max_col and input[r][c] == input[nr][nc]
    ]

def all_neighbours(pos):
    r,c = pos
    return [ (r,c) for r,c in [ (r-1,c), (r,c-1), (r+1,c), (r,c+1) ] ]

def fill_region(pos):
    unvisited = [pos]
    visited = []
    while unvisited:
        this = unvisited.pop()
        visited.append(this)
        for n in neighbours(this):
            if n not in visited and n not in unvisited: unvisited.append(n)
    return visited

def area(plot): return len(plots[plot])

def perimiter(plot):    
    neighbours = [ j for i in [ all_neighbours(pos) for pos in plots[plot] ] for j in i ]
    perimiter = len([ n for n in neighbours if n not in plots[plot] ])
    return perimiter

visited = []
plot = 0
for pos in [ (r,c) for r in range(max_row+1) for c in range(max_col+1) ]:
    if pos not in visited:
        this_region = fill_region(pos)
        visited.extend(this_region)
        plots[plot] = this_region
        plot += 1

part1 = sum([ area(i) * perimiter(i) for i in plots ])
print(part1)

def is_edge(pos,neighbour):
    r,c = pos
    nr,nc = neighbour
    if not (0 <= nr <= max_row and 0 <= nc <= max_col): return True
    if input[r][c] != input[nr][nc]: return True
    return False

def discount_perimeter(plot):

    horizontal_edges = []
    vertical_edges = []

    for pos in plots[plot]:
        r,c = pos
        # check up,down,left,right edges
        if is_edge(pos,(r-1,c)): horizontal_edges.append((r,c))
        if is_edge(pos,(r+1,c)): horizontal_edges.append((r+1,c))
        if is_edge(pos,(r,c-1)): vertical_edges.append((r,c))
        if is_edge(pos,(r,c+1)): vertical_edges.append((r,c+1))

    vertices = 0
    for ver,vec in vertical_edges:
        if (ver,vec) in horizontal_edges or (ver,vec-1) in horizontal_edges:
            vertices += 1
        if (ver+1,vec) in horizontal_edges or (ver+1,vec-1) in horizontal_edges:
            vertices += 1
    return vertices

part2 = sum([ area(i) * discount_perimeter(i) for i in plots ])
print(part2)