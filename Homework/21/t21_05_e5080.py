


if __name__ == "__main__":
    n = int(input())

    count = 0
    for _ in range(n):
        count += 1 if sum(list(map(int, input().split()))) == 1 else 0

    print(count)
