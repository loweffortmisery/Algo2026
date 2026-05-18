import sys

def solve():
    data = sys.stdin.read().split()

    n, m = int(data[0]), int(data[1])
    
    AL = [[] for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u, v = int(data[idx]), int(data[idx+1])
        AL[u].append(v)
        AL[v].append(u)
        idx += 2
        
    visited = [0] * (n + 1) 
    components = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            component = []
            stack = [i]
            visited[i] = 1
            
            while stack:
                curr = stack.pop()
                component.append(curr)
                for neighbour in AL[curr]:
                    if not visited[neighbour]:
                        visited[neighbour] = 1
                        stack.append(neighbour)
                        
            components.append(component)
            
    print(len(components))
    for comp in components:
        print(len(comp))
        print(*comp)

if __name__ == '__main__':
    solve()
