import heapq

class Vertex:

    def __init__(self,position):
        self.position = position
        self.adjacent = []
        self.g = 999999
        self.h = None
        self.previous = None

    def __str__(self):
        return f"{self.position} - g:{self.g}, adjacent{[v.position for v,_ in self.adjacent]}"

    def __lt__(self,other):
        return self.f() < other.f()

    def f(self):
        return self.g + self.h
    
    def add_adjacent(self, vertex, weight):
        self.adjacent.append((vertex,weight))

class Graph:

    def __init__(self,):
        self.vertices = {}
        self.start = None
        self.end = None

    def calc_h(self):
        for vertex in self.vertices.values():
            r1,c1 = vertex.position
            r2,c2 = self.end.position
            vertex.h = abs(r2-r1) + abs(c2-c1) - 1

    def add_vertex(self,position):
        self.vertices[position] = Vertex(position)

    def a_star(self):
        open = []
        closed = set()

        heapq.heappush(open, self.start)
        self.start.g = 0

        while open:
            this = heapq.heappop(open)

            if this is self.end: break

            closed.add(this)

            for neighbour, weight in this.adjacent:
                tenantive_g = this.g + weight
                if tenantive_g < neighbour.g:
                    neighbour.previous = this
                    neighbour.g = tenantive_g
                    if neighbour not in open:
                        heapq.heappush(open, neighbour)

input = open("18.txt","r").read().splitlines()
data = [ [ int(j) for j in i.split(",") ] for i in input ]

max_row = 70
max_col = 70

def compute(byte_count):

    grid = [ ["."]*(max_col+1) for i in range(max_col+1)]

    for r,c in data[0:byte_count]:
        grid[r][c] = "#"

    def adjacent(pos,grid):
        r,c = pos
        return [ (nr,nc) for nr,nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
                    if 0 <= nr <= max_row and 0 <= nc <= max_col
                    and grid[nr][nc] == "." ]

    graph = Graph()
    [ graph.add_vertex((r,c)) for r in range(max_row+1) for c in range(max_col+1) ]

    for vertex in graph.vertices.values():
        for a in adjacent(vertex.position,grid):
            vertex.add_adjacent(graph.vertices[a],1)

    graph.start = graph.vertices[(0,0)]
    graph.end = graph.vertices[(max_row,max_col)]

    graph.calc_h()
    graph.a_star()

    return graph.end.g

part1 = compute(1024)
print(part1)

# part 2

step = len(data) // 2
n = step
while True:
    step = step // 2
    path = compute(n)
    if compute(n) < 999999:
        n += step
    else:
        if compute(n-1) < 999999:
            solution = n
            break
        else:
            n -= step

print(data[solution-1])


