def permutations(current, unused, k):
    if k == 0:
        print(*current)
        return
    k -= 1
    for i in range(len(unused)):
        _current = current + [unused[i]]
        _unused = unused[:i] + unused[i+1:]
        permutations(_current, _unused, k)


def solve():
    n, k = map(int, input().split())
    unused = [i for i in range(1, n+1)]
    current = []
    permutations(current, unused, k)


if __name__ == "__main__":
    solve()
