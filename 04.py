input = open("04.txt", "r").read().splitlines()

data = [ list(i) for i in input ]

rows = len(data)
cols = len(data[0])

# part 1

target = list('XMAS')
def is_match(word):
    return word == target or word[::-1] == target

part1 = 0
for row in range(rows):
    for col in range(cols):
        # look horizontal
        if cols - col >= len(target) and is_match(data[row][col:col+len(target)]): part1 +=1
        # look vertical
        if rows - row >= len(target) and is_match([data[i][col] for i in range(row,row+len(target))]): part1 +=1
        # look diagonal down
        if cols - col >= len(target) and rows - row >= len(target) and is_match([data[row][col], data[row+1][col+1], data[row+2][col+2], data[row+3][col+3]]): part1 += 1
        # look diagonal up
        if cols - col >= len(target) and row >= len(target) - 1 and is_match([data[row][col], data[row-1][col+1], data[row-2][col+2], data[row-3][col+3]]): part1 += 1

print(part1)

# part 2

def is_match2(grid):
    if grid[1][1] != "A": return False
    valid = [["M","S"], ["S","M"]]
    if [grid[0][0],grid[2][2]] not in valid: return False
    if [grid[0][2],grid[2][0]] not in valid: return False
    return True

part2 = 0
for row in range(rows-2):
    for col in range(cols-2):
        grid = [ data[i][col:col+3] for i in range(row,row+3) ]
        if is_match2(grid): part2 += 1

print(part2)