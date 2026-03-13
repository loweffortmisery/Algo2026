def _quick_sort(arr, a, b):
    if a >= b:
        return

    L = a
    R = b

    a_m = arr[L + (R-L)//2]
    while True:
        while arr[L] < a_m:
            L += 1
        while arr[R] > a_m:
            R -= 1
        if L >= R:
            break

        arr[L], arr[R] = arr[R], arr[L]
        R -= 1
        L += 1
    _quick_sort(arr, a, R)
    _quick_sort(arr, R+1, b)



def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    _quick_sort(arr, 0, n-1)
    print(*arr)


if __name__ == "__main__":
    solve()
