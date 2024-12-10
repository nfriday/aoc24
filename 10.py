input = [ [ int(j) if j != "." else -1 for j in list(i) ] for i in open("10.txt", "r").read().splitlines() ]

max_row = len(input) - 1
max_col = len(input[0]) - 1

def neighbours(coord):
    row, col = coord
    neighbours = [ (r,c) for r,c in [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]
                  if 0 <= r <= max_row and 0 <= c <= max_col ]    
    return neighbours

# part 1

def score(start):
    def walk(x):
        visited.append(x)
        score = 0
        row,col = x
        if input[row][col] == 9: score += 1
        valid_neighbours = [ (r,c) for r,c in neighbours(x) if input[r][c] == input[row][col] + 1 and (r,c) not in visited ]
        for n in valid_neighbours:
            score += walk(n)
        return score
    visited = []
    return walk(start)

trailheads = [ (r,c) for r in range(max_row+1) for c in range(max_col+1) if input[r][c] == 0 ]
part1 = sum([ score(t) for t in trailheads ])
print(part1)

# part 2

def score2(start):
    def walk(x):
        score = 0
        row,col = x
        if input[row][col] == 9: score += 1
        valid_neighbours = [ (r,c) for r,c in neighbours(x) if input[r][c] == input[row][col] + 1 ]
        for n in valid_neighbours:
            score += walk(n)
        return score
    visited = []
    return walk(start)

trailheads = [ (r,c) for r in range(max_row+1) for c in range(max_col+1) if input[r][c] == 0 ]
part2 = sum([ score2(t) for t in trailheads ])
print(part2)