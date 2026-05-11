from collections import deque


class Graph:

    def __init__(self, n):
        self.vertices = {
            i: set() for i in range(1, n + 1)
        }

    def add_edge(self, u, v):
        self.vertices[u].add(v)
        self.vertices[v].add(u)

    def bfs(self, ignited, time_to_ignition):
        visited = [0]*(len(self.vertices) + 1)
        queue = deque()
        for start in ignited:
            time_to_ignition[start] = 0
            queue.append(start)
            visited[start] = 1
        while queue:
            vertex = queue.popleft()
            for neighbour in self.vertices[vertex]:
                if not visited[neighbour]:
                    queue.append(neighbour)
                    visited[neighbour] = 1
                    time_to_ignition[neighbour] = time_to_ignition[vertex] + 1


if __name__ == '__main__':
    f = open("input.txt")
    n, m = map(int, f.readline().split())
    graph = Graph(n)
    for _ in range(m):
        u, v = map(int, f.readline().split())
        graph.add_edge(u, v)
    k = int(f.readline())
    ignited = list(map(int, f.readline().split()))
    time_to_ignition = [-1]*(n+1)
    graph.bfs(ignited, time_to_ignition)
    _max = max(time_to_ignition)
    print(_max)
    print(time_to_ignition.index(_max))
  #  print(time_to_ignition)
    f.close()
