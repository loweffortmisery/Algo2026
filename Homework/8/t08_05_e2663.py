
def count_swaps(arr, n):
    c = 0
    for i in range(n, 0, -1):
        for j in range(1, i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                c += 1
    return c


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_swaps(arr, n))


if __name__ == '__main__':
    solve()
