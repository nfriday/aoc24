input = [ list(i) for i in open("06.txt", "r").read().splitlines() ]

start = [ [row,col] for row in range(len(input)) for col in range(len(input[0])) if input[row][col] == "^" ][0]

max_row = len(input) - 1
max_col = len(input[0]) - 1

def turn_right(direction):
    row_direction, col_direction = direction
    return [col_direction, -row_direction]

# part 1
grid = [row[:] for row in input]

cursor = start
direction = [-1, 0]

while True:
    row, col = cursor
    row_direction, col_direction = direction

    row += row_direction
    col += col_direction

    # if off the grid, exit
    if row < 0 or col < 0 or row > max_row or col > max_col: break

    # if obstacle, turn
    if grid[row][col] == "#":
        direction = turn_right(direction)
        continue

    # otherwise step
    grid[row][col] = "X"
    cursor = [row,col]

part1 = sum([ len([i for i in row if i in ["X","^"]]) for row in grid])

print(part1)

# part 2
grid = [ [{i} if i != "." else set() for i in row[:] ] for row in input ]

def direction_indicator(x):
    match x:
        case [-1, 0]: return "^"
        case [1, 0]: return "v"
        case [0, -1]: return "<"
        case [0, 1]: return ">"
    raise Exception("invalid")

def check_for_loop(grid,obstacle):

    cursor = start
    direction = [-1, 0]

    # deep copy grid
    grid = [ [set(i) for i in row[:] ] for row in grid ]

    # add obstacle
    obstacle_row, obstacle_col = obstacle
    grid[obstacle_row][obstacle_col] = {"#"}

    while True:

        row, col = cursor
        row_direction, col_direction = direction

        # mark pos
        grid[row][col].add(direction_indicator(direction))

        # move
        row += row_direction
        col += col_direction

        # if off the grid, no loop
        if row < 0 or col < 0 or row > max_row or col > max_col: return False

        # if i've been in this pos facing this direction before
        if direction_indicator(direction) in grid[row][col]: return True

        # if obstacle, turn
        if "#" in grid[row][col]:
            direction = turn_right(direction)
            continue

        # shift cursor
        cursor = [row,col]

part2 = len([ [row, col] for row in range(max_row+1) for col in range(max_col+1) if [row,col] != start and check_for_loop(grid,[row,col]) ])
print(part2)