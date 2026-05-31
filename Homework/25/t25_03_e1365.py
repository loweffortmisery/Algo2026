import sys

INF = sys.maxsize

def solve():
    n, s, f = map(int, input().split())
    s -= 1
    f -= 1
    
    graph = []
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    distances = [INF for _ in range(n)]
    distances[s] = 0
    visited = [False for _ in range(n)]

    for _ in range(n):
        min_dist = INF
        u = -1
        for i in range(n):
            if not visited[i] and distances[i] < min_dist:
                min_dist = distances[i]
                u = i

        if u == -1:
            break

        visited[u] = True

        for v in range(n):
            if graph[u][v] != -1 and not visited[v]:
                if distances[v] > distances[u] + graph[u][v]:
                    distances[v] = distances[u] + graph[u][v]

    if distances[f] < INF:
        print(distances[f])
    else:
        print(-1)

if __name__ == '__main__':
    solve()
