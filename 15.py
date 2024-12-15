input = open("15.txt", "r").read()

def start(grid):
    return [ (row,col) for row in range(max_row+1) for col in range(max_col+1) if grid[row][col] == "@" ][0]

bearings ={
    "^": (-1,0),
    "v": (1,0),
    "<": (0,-1),
    ">": (0,1)
}

# part 1

grid, moves = input.split("\n\n")
grid  = [ list(row) for row in grid.splitlines() ]
moves = [ i for i in list(moves) if i != "\n" ]

max_row = len(grid)-1
max_col = len(grid[0])-1

def go(grid,move,robot):
    bearing = bearings[move]
    dr,dc = bearing
    rr, rc = robot
    
    r = rr + dr
    c = rc + dc
    boxes = 0
    while grid[r][c] == "O":
        r += dr
        c += dc
        boxes += 1

    if grid[r][c] == "#": return robot

    if boxes > 0:
        grid[r][c] = "O"

    grid[rr][rc] = "."    
    grid[rr+dr][rc+dc] = "@"

    return (rr+dr,rc+dc)

robot = start(grid)
for move in moves:
    robot = go(grid,move,robot)

boxes = [ (row,col) for row in range(max_row+1) for col in range(max_col+1) if grid[row][col] == "O" ]
part1 = sum([ 100*row + col for row,col in boxes ])
print(part1)

# part 2

grid, moves = input.split("\n\n")

def widen(x):
    if x == "#": return "##"
    if x == "O": return "[]"
    if x == ".": return ".."
    if x == "@": return "@."

moves = [ i for i in list(moves) if i != "\n" ]
grid  = [ list("".join([widen(i) for i in list(row)])) for row in grid.splitlines() ]   

max_row = len(grid)-1
max_col = len(grid[0])-1

def adjacent_vertical_boxes(grid,pos,bearing):
    dr,_ = bearing
    r,c = pos

    possible_positions = [ (r+dr,c), (r+dr,c+1), (r+dr,c-1) ]
    adjacent = [ (r,c) for r,c in possible_positions if grid[r][c]=="[" ]

    for a in adjacent:
        a2 = adjacent_vertical_boxes(grid,a,bearing)
        if a2: adjacent.extend(a2)

    return list(set(adjacent))

def can_move_box_vertical(grid,pos,bearing):
    dr,_ = bearing
    r,c = pos
    for check_r,check_c in ((r+dr,c), (r+dr,c+1)):
        if grid[check_r][check_c] == "#": return False    
    return True

def move_boxes(grid,boxes,bearing):
    dr,dc = bearing

    new_boxes_left = []
    new_boxes_right = []
    for box in boxes:
        r,c = box
        grid[r][c] = "."
        grid[r][c+1] = "."
        new_boxes_left.append((r+dr,c+dc))
        new_boxes_right.append((r+dr,c+1+dc))

    for box in new_boxes_left:
        r,c = box
        grid[r][c] = "["

    for box in new_boxes_right:
        r,c = box
        grid[r][c] = "]"

def go2(grid,move,robot):
    bearing = bearings[move]
    dr,dc = bearing
    rr, rc = robot

    r = rr + dr
    c = rc + dc

    # if space is empty, move into it
    if grid[r][c] == ".":
        grid[rr][rc] = "."
        grid[r][c] = "@"
        return (r,c)
    
    # if space is a wall, do nothing
    if grid[r][c] == "#":
        return robot
    
    # if space is a box:
    vertical_move = dc == 0

    if vertical_move:
        this_box = (r,c) if grid[r][c]=="[" else (r,c-1)
        adjacent = adjacent_vertical_boxes(grid,this_box,bearing)
        adjacent.append(this_box)
        for box in adjacent:
            if not can_move_box_vertical(grid,box,bearing): return robot
        move_boxes(grid,adjacent,bearing)
        grid[rr][rc] = "."
        grid[r][c] = "@"
        return (r,c)
    else:
        while grid[r][c] in ("[","]"):
            c += dc
        if grid[r][c] == "#": return robot
        while grid[r][c] != "@":
            grid[r][c] = grid[r][c-dc]
            c -= dc
        grid[rr][rc] = "."
        grid[r+dr][c+dc] = "@"
        return((r+dr),(c+dc))

robot = start(grid)
for move in moves:
    robot = go2(grid,move,robot)

boxes = [ (row,col) for row in range(max_row+1) for col in range(max_col+1) if grid[row][col] == "[" ]
part2 = sum([ 100*row + col for row,col in boxes ])
print(part2)