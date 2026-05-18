import sys

sys.setrecursionlimit(200000)

class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def empty(self):
        return len(self.items) == 0

class Vertex:
    def __init__(self, key):
        self._key = key
        self.neighbours = []

    def key(self):
        return self._key

    def add_neighbor(self, neighbor_key):
        self.neighbours.append(neighbor_key)

    def neighbors(self):
        return self.neighbours


class Graph:
    def __init__(self):
        self.mVertices = {}
        self.mVertexNumber = 0

    def __iter__(self):
        return iter(self.mVertices.values())

    def __contains__(self, key):
        return key in self.mVertices

    def __getitem__(self, key):
        if isinstance(key, Vertex):
            return self.mVertices[key.key()]
        return self.mVertices[key]

    def add_edge(self, u, v):
        if u not in self:
            self.addVertex(u)
        if v not in self:
            self.addVertex(v)
        self.mVertices[u].add_neighbor(v)
    
    def addVertex(self, vertex):
        pass


WHITE = 0 
GRAY = 1 
BLACK = 2 

class ColorVertex(Vertex):
    def __init__(self, key):
        super().__init__(key)
        self.mColor = WHITE
    
    def setColor(self, color):
        self.mColor = color

    def color(self):
        return self.mColor

class ColorGraph(Graph):
    def addVertex(self, vertex):
        if vertex in self: 
            return False

        new_vertex = ColorVertex(vertex)
        self.mVertices[vertex] = new_vertex 
        self.mVertexNumber += 1 
        return True

def __dfs_helper(graph, vertex, stack):
    if vertex.color() == BLACK: 
        return

    if vertex.color() == GRAY: 
        raise AssertionError

    
    vertex.setColor(GRAY) 
    for neighbour_key in graph[vertex].neighbors(): 
        neighbour = graph[neighbour_key]
        __dfs_helper(graph, neighbour, stack) 


    vertex.setColor(BLACK)
    stack.push(vertex.key()) 

def topological_sorting(graph):
    stack = Stack() 
    try:
        for vertex in graph: 
            __dfs_helper(graph, vertex, stack)
    except AssertionError:
        return [-1]

    sequence = []
    while not stack.empty():
        sequence.append(stack.pop())
    return sequence


if __name__ == '__main__':
    n, m = map(int, input().split())
    g = ColorGraph() 
    for i in range(1, n+1):
        g.addVertex(i)
    for _ in range(m):
        u, v = map(int, input().split())
        g.add_edge(u, v)
    print(*topological_sorting(g))
