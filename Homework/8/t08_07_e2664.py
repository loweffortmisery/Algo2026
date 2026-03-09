def insertion_sort(arr, n):
    for i in range(1,n):
        pos = i
        x = arr[pos]
        while pos > 0:
            if arr[pos-1] > x:
                arr[pos] = arr[pos-1]
            else:
                break
            pos -= 1
        arr[pos] = x
        if pos != i:
            yield arr



def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    for array in insertion_sort(arr, N):
        print(*array)

if __name__ == "__main__":
    solve()

