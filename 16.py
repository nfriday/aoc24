import heapq

input = open("16.txt", "r").read().splitlines()

grid = [ list(row) for row in input ]
max_row = len(grid) - 1
max_col = len(grid[0]) - 1

class Vertex:

    def __init__(self,position):
        self.position = position
        self.adjacent = {}
        self.distance = 999999
        self.previous = None

    def add_neighbour(self,neighbour,weight):
        self.adjacent[neighbour] = weight

    def reset(self):
        self.distance = 999999
        self.previous = None
    
    def __lt__(self,other):
        return self.distance < other.distance

def find(vertices,x):
    for v in vertices:
        row,col = v.position
        if grid[row][col]==x: return v

class Graph:

    def __init__(self):
        self.vertices = {}
        self.origin = None
        self.end = None

    def add_vertex(self,vertex):
        is_origin = grid[vertex.position[0]][vertex.position[1]] == "S"
        is_end = grid[vertex.position[0]][vertex.position[1]] == "E"
        if is_origin:
            self.origin = vertex
            vertex.distance = 0
        if is_end:
            self.end = vertex
        self.vertices[vertex.position] = vertex

    def reset(self):
        for v in self.vertices.values(): v.reset()
        self.origin.distance = 0

    def visit(self,vertex,ignore_vertex=None):
        for nk,nv in vertex.adjacent.items():

            neighbour = self.vertices[nk]

            if neighbour not in self.visited:
            
                turn = False
                if vertex.previous == None and neighbour.position[0] != vertex.position[0]:
                    turn = True
                if vertex.previous and neighbour.position[0] != vertex.previous.position[0] and neighbour.position[1] != vertex.previous.position[1]:
                    turn = True

                new_distance = vertex.distance + nv + (1000 if turn else 0)

                if neighbour is ignore_vertex: new_distance *= 99

                if new_distance < neighbour.distance:
                    neighbour.distance = new_distance
                    neighbour.previous = vertex
                    heapq.heappush(self.queue, (neighbour.distance, neighbour))
    
    def get_shortest_path(self,ignore_vertex=None):
        self.reset()

        self.queue = []
        self.visited = set()
        heapq.heappush(self.queue, (self.origin.distance, self.origin))

        while self.queue:
            _, next_vertex = heapq.heappop(self.queue)
            
            if next_vertex in self.visited: continue

            self.visited.add(next_vertex)
            self.visit(next_vertex,ignore_vertex)
            if next_vertex is self.end: break

        path = [self.end]
        while path[-1] is not self.origin:
            if not path[-1].previous: break
            path.append(path[-1].previous)

        return (graph.end.distance, path)

graph = Graph()
# load horizontal vertexes
for row in range(1,max_row):
    last_vertex = None
    for col in range(1,max_col):
        if grid[row][col] in (".","S","E"):
            up_edge, down_edge, left_edge, right_edge = grid[row-1][col]=="#", grid[row+1][col]=="#", grid[row][col-1]=="#", grid[row][col+1]=="#"
            is_horizontal_edge = left_edge ^ right_edge
            is_vertical_edge = up_edge ^ down_edge
            double_intersection = not (left_edge or right_edge or up_edge or down_edge)
            if is_horizontal_edge or is_vertical_edge or double_intersection:
                this_vertex = Vertex((row,col))
                if last_vertex:
                    _,last_col = last_vertex.position
                    distance = abs(col - last_col)
                    this_vertex.add_neighbour(last_vertex.position,distance)
                    last_vertex.add_neighbour(this_vertex.position,distance)
                    graph.add_vertex(last_vertex)
                last_vertex = this_vertex
        else:
            if (last_vertex): graph.add_vertex(last_vertex)
            last_vertex = None
    if (last_vertex): graph.add_vertex(last_vertex)
# load vertical vertex
for col in range(1,max_col):
    vertices_in_col = [ graph.vertices[v] for v in graph.vertices if v[1]==col ]
    for last_vertex,this_vertex in zip(vertices_in_col[:-1],vertices_in_col[1:]):
        last_row,_ = last_vertex.position
        row,_ = this_vertex.position
        if "#" not in (grid[last_row+1][col],grid[row-1][col]):
            distance = abs(row - last_row)
            this_vertex.add_neighbour(last_vertex.position,distance)
            last_vertex.add_neighbour(this_vertex.position,distance)

part1,path = graph.get_shortest_path()

# part 2

def fill_line(a,b):
    r1,c1 = a.position
    r2,c2 = b.position
    if r1 == r2:
        cols = [c1,c2]
        cols.sort()
        for col in range(min(cols),max(cols)+1): grid[r1][col] = "O"
    elif c1 == c2:
        rows = [r1,r2]
        rows.sort()
        for row in range(min(rows),max(rows)+1): grid[row][c1] = "O"

def fill_path(path):
    for a,b in zip(path[:-1],path[1:]): fill_line(a,b)

fill_path(path)
visited = set()
to_visit = [ i for i in path if i is not graph.origin and i is not graph.end ]

while to_visit:
    test_vertex = to_visit.pop()
    visited.add(test_vertex)
    test_score,test_path = graph.get_shortest_path(ignore_vertex=test_vertex)
    print(f"trying with node {test_vertex.position} removed ... score is {test_score}")
    if test_score == part1:
        fill_path(test_path)
        for vertex in test_path:
            if vertex not in visited:
                to_visit.append(vertex)

for row in grid:
    print("".join([ f"\033[32m{i}\033[0m" if i=="O" else i for i in list(row) ]))

part2 = sum([ len([i for i in list(row) if i=="O"]) for row in grid ])
print(part2)