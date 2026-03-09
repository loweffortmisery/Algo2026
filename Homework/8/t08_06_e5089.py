def selection_sort(arr, n):
    for i in range(n-1):
        pos = i
        for j in range(i+1, n):
            if arr[j] < arr[pos]:
                pos = j
        arr[pos], arr[i] = arr[i], arr[pos]


def solve():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input())
    selection_sort(arr, n)
    for word in arr:
        print(word)


if __name__ == "__main__":
    solve()
