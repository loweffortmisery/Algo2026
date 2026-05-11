
from collections import deque


class Graph:
    def __init__(self, n):
        self.vertices = {
            i: set() for i in range(1, n + 1)
        }

    def add_edge(self, u, v):
        self.vertices[u].add(v)
        self.vertices[v].add(u)

    def dfs(self, start, finish, d, visited):
        if start == finish:
            return 1
        if d == 0:
            return 0
        
        num_of_ways = 0
        for neighbour in self.vertices[start]:
            if neighbour not in visited:
                visited.add(neighbour)
                num_of_ways += self.dfs(neighbour, finish, d - 1, visited)
                visited.remove(neighbour)
        return num_of_ways


if __name__ == '__main__':
    f = open("input.txt")
    n, m, a, b, d = map(int, f.readline().split())
    graph = Graph(n)
    for _ in range(m):
        u, v = map(int, f.readline().split())
        graph.add_edge(u, v)
    print(graph.dfs(a, b, d, {a}))
    f.close()
