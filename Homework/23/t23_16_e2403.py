global counter

def solve():   
    global counter
    counter = 0
    n, m = map(int, input().split())
    AL = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        AL[u].append(v)



    def reachable(start, target):
        if start == target: 
            return True
        visited = [0] * (n + 1)
        stack = [start]
        visited[start] = 1
        while stack:
            curr = stack.pop()
            if curr == target: 
                return True
            for neighbour in AL[curr]:
                if not visited[neighbour]:
                    visited[neighbour] = 1
                    stack.append(neighbour)
        return False

    def explore(current_set):
        global counter
        biggest = True
        for v in range(1, n + 1):
            if v not in current_set:
                can_add = True
                for u in current_set:
                    if not (reach[u][v] and reach[v][u]):
                        can_add = False
                        break

                if can_add:
                    biggest = False
                    new_set = current_set.copy()
                    new_set.add(v)
                    vertices = tuple(sorted(list(new_set)))
                    if vertices not in sorted_visited_sets:
                        sorted_visited_sets.add(vertices)
                        explore(new_set) 
        if biggest:
            counter += 1

    reach = [[False] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            reach[i][j] = reachable(i, j)

    sorted_visited_sets = set()

    explore(set())

    print(counter)

if __name__ == '__main__':
    solve()
