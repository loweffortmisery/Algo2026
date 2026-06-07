import sys

class MaxPriorityQueue:
    def __init__(self):
        self.items = [(0, "")]
        self.pos = {}

    def swap(self, i, j):
        self.pos[self.items[i][1]] = j
        self.pos[self.items[j][1]] = i
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def sift_up(self, i):
        while i > 1 and self.items[i][0] > self.items[i // 2][0]:
            self.swap(i, i // 2)
            i //= 2

    def sift_down(self, i):
        size = len(self.items) - 1
        while 2 * i <= size:
            j = 2 * i
            if j < size and self.items[j + 1][0] > self.items[j][0]:
                j += 1
            if self.items[i][0] >= self.items[j][0]:
                break
            self.swap(i, j)
            i = j

    def add(self, item_id, priority):
        self.items.append((priority, item_id))
        idx = len(self.items) - 1
        self.pos[item_id] = idx
        self.sift_up(idx)

    def pop(self):
        self.swap(1, len(self.items) - 1)
        priority, item_id = self.items.pop()
        del self.pos[item_id]
        
        if len(self.items) > 1:
            self.sift_down(1)
            
        return item_id, priority

    def change(self, item_id, new_priority):
        idx = self.pos[item_id]
        old_priority = self.items[idx][0]
        self.items[idx] = (new_priority, item_id)
        
        if new_priority > old_priority:
            self.sift_up(idx)
        else:
            self.sift_down(idx)


if __name__ == '__main__':
    pq = MaxPriorityQueue()
    commands = sys.stdin.read().splitlines()
    
    for line in commands:
        cmd, *args = line.split()
        
        if cmd == "ADD":
            pq.add(args[0], int(args[1]))
        elif cmd == "POP":
            result = pq.pop()
            print(f"{result[0]} {result[1]}")
        elif cmd == "CHANGE":
            pq.change(args[0], int(args[1]))
