


if __name__ == "__main__":
    n, m = map(int, input().split())
    
    ins = [0]*(n+1)
    outs = [0]*(n+1)
    for _ in range(m):
        v, u = map(int, input().split())
        ins[u] += 1
        outs[v] += 1
    for i in range(1, n+1):
        print(ins[i], outs[i])
