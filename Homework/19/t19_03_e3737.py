
def solve(arr):
    ind = int(arr[0])
    while (ind > 1):
        if int(arr[ind]) < int(arr[ind // 2]):
            print("NO\n")
            return
        ind -= 1
    print("YES\n")



if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    solve(data)
