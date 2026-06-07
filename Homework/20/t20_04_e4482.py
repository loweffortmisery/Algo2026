from math import ceil, log2

class SegmentTree:
    def __init__(self, array):
        k = len(array)
        p = ceil(log2(k))
        n = 1 << p
        self.tree = 2 * n * [(float('inf'), -float('inf'))]
        for i in range(k):
            self.tree[i + n] = (array[i], array[i])
        for i in range(n - 1, 0, -1):
            self.tree[i] = (min(self.tree[2 * i][0], self.tree[2 * i + 1][0]), 
                            max(self.tree[2 * i][1], self.tree[2 * i + 1][1]))
        self.n = n

    def update(self, i, item):
        i = self.n + i
        self.tree[i] = (item, item)
        while i > 1:
            i = i // 2
            self.tree[i] = (min(self.tree[i * 2][0], self.tree[i * 2 + 1][0]), 
                            max(self.tree[i * 2][1], self.tree[i * 2 + 1][1]))

    def query(self, left, right):
        left += self.n
        right += self.n
        res_min = float('inf')
        res_max = -float('inf')
        while left <= right:
            if left % 2 == 1:
                res_min = min(res_min, self.tree[left][0])
                res_max = max(res_max, self.tree[left][1])
            if right % 2 == 0:
                res_min = min(res_min, self.tree[right][0])
                res_max = max(res_max, self.tree[right][1])

            left = (left + 1) // 2
            right = (right - 1) // 2
        return res_min == res_max


if __name__ == '__main__':
    f = open("input.txt")
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))
    m = int(f.readline())
    tree = SegmentTree(arr)
    
    for _ in range(m):
        q, a, b = map(int, f.readline().split())
        if q == 1:
            if tree.query(a - 1, b - 1):
                print("draw")
            else:
                print("wins")
        elif q == 2:
            tree.update(a - 1, b)
            
    f.close()
