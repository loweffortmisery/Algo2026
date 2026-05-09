





if __name__ == "__main__":
    n, m = map(int, input().split())
    
    AJ = [set() for _ in range(n+1)]

    for _ in range(m):
        v, u = map(int, input().split())
        if u in AJ[v]:
            print("YES")
            exit()
        AJ[v].add(u)
    print("NO")
