def find_sum(current_sum, N, start, end, tracks, calculated):
    if start in calculated:
        return calculated[start]
    if current_sum > N:
        return 0
    if current_sum == N:
        return N
    if start == end: 
        return current_sum
    take = find_sum(current_sum + tracks[start],    N, start+1, end, tracks, calculated)
    skip = find_sum(current_sum,                    N, start+1, end, tracks, calculated)

    r = max(take, skip)
    calculated[start] = r
    return r

def solve():
    data = list(map(int, input().split()))
    N = data[0]
    s = data[1]
    data = data[2:]
    calculated = dict()
    print("sum:", find_sum(0, N, 0, s, data, calculated), sep='')


if __name__ == "__main__":
    while True:
        try:
            solve()
        except EOFError:
            break

