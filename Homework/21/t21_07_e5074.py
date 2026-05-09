


if __name__ == "__main__":
    n, m = map(int, input().split())
    
    degs = [0]*(n+1)
    for _ in range(m):
        v, u = map(int, input().split())
        degs[u] += 1
        degs[v] += 1
    for i in range(1, n+1):
        print(degs[i])
