class Deque():
    def __init__(self, capacity=1000):
        self.data = [0] * capacity
        self.first = None
        self.last = None
        self.capacity = capacity
        self._size = 0

    def size(self):
        return self._size

    def empty(self):
        return self._size == 0

    def push_back(self, item):
        if self._size == 0:
            self.first = self.last = 0
        else:
            self.last += 1
            self.last %= self.capacity
        self._size += 1
        self.data[self.last] = item
        return "ok"

    def push_front(self, item):
        if self._size == 0:
            self.first = self.last = 0
        else:
            self.first -= 1
            self.first %= self.capacity
        self._size += 1
        self.data[self.first] = item
        return "ok"

    def pop_back(self):
        if self._size == 0:
            raise IndexError
        
        self._size -= 1
        item = self.data[self.last]
        self.last -= 1
        self.last %= self.capacity
        return item

    def pop_front(self):
        if self._size == 0:
            raise IndexError

        self._size -= 1
        item = self.data[self.first]
        self.first += 1
        self.first %= self.capacity
        return item

    def back(self):
        if self._size == 0:
            raise IndexError
        
        item = self.data[self.last]
        return item
   
    def front(self):
        if self._size == 0:
            raise IndexError
        
        item = self.data[self.first]
        return item
    
    def clear(self):
        self._size = 0
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        try:
            return getattr(self, method)(*args) 
        except IndexError:
            return("error")

if __name__ == '__main__':
    import sys
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    F = Deque(n)
    S = Deque(n)
    for i in range(1, n//2+1):
        F.push_back(data[i])
    for i in range(n//2+1, n+1):
        S.push_back(data[i])
    c = 0
    while c < 2*100_000:
        try:
            f = F.pop_front()
            s = S.pop_front()
            c += 1
        except IndexError:
            break
        #print(f"{S.data=}, \n, {F.data=}")
        #print(f"{S.size()=}, \n, {F.size()=}")
        #print(f"{f=},{s=}")
        f_edge_win = (f == 0 and s == n-1)
        s_edge_win = (s == 0 and f == n-1)
        if (f_edge_win) or (not(s_edge_win) and f > s):  
         #   print("F won")
            F.push_back(f)
            F.push_back(s)
            continue
        S.push_back(f)
        S.push_back(s)
    if F.empty():
        print("second", c)
    elif S.empty():
        print("first", c)
    else:
        print("draw")


