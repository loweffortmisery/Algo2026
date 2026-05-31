import sys

INF = sys.maxsize

def solve():
    n, m = map(int, input().split())
    s, f = map(int, input().split())
    
    graph = [{} for _ in range(n + 1)]
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u][v] = w
        graph[v][u] = w

    distances = [INF for _ in range(n + 1)]
    distances[s] = 0
    sources = [-1 for _ in range(n + 1)]

    for _ in range(n - 1):
        relaxed = True
        for i in range(1, n + 1):
            for j in graph[i]:
                if distances[j] > distances[i] + graph[i][j]:
                    distances[j] = distances[i] + graph[i][j]
                    sources[j] = i
                    relaxed = False
        if relaxed:
            break

    if distances[f] < INF:
        print(distances[f])
        way = []
        i = f
        while i != -1:
            way.append(i)
            i = sources[i]
        way.reverse()
        print(*(way))
    else:
        print(-1)

if __name__ == '__main__':
    solve()
