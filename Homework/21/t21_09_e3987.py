


if __name__ == "__main__":
    n, m = map(int, input().split())
    AM = [[0]*n for _ in range(n)] 
    for _ in range(m):
        v, u = map(int, input().split())
        AM[u-1][v-1] += 1
        AM[v-1][u-1] += 1
    for i in range(n):
        for j in range(i):
            if AM[i][j] == 0:
                print("NO")
                exit()
    print("YES")
