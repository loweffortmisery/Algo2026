def _merge_sort(robots, a, b):
    if a >= b:
        return
    
    m = a + (b-a)//2

    _merge_sort(robots, a, m)
    _merge_sort(robots, m+1, b)

    left = [[0,0] for _ in range((m+1)-a)] 
    for i in range(a, m+1):
        left[i-a][0], left[i-a][1] = robots[i][0], robots[i][1]
        
    i = 0
    j = m + 1
    k = a

    while i < len(left) and j <= b:
        if left[i][0] <= robots[j][0]:
            robots[k][0] = left[i][0]
            robots[k][1] = left[i][1]
            i += 1

        else:
            robots[k][0] = robots[j][0] 
            robots[k][1] = robots[j][1]
            j += 1

        k += 1

    while i < len(left):
        robots[k][0] = left[i][0]
        robots[k][1] = left[i][1]
        i += 1
        k += 1
            

def solve():
    N = int(input())
    robots = [[0,0] for _ in range(N)]
    for i in range(N):
        robots[i][0], robots[i][1] = map(int, input().split())
    
    _merge_sort(robots, 0, N-1)
    
    for i in range(N):
        print(*robots[i])

if __name__ == "__main__":
    solve()
