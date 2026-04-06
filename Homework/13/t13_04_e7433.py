class Stack:
    def __init__(self, m_size = 100+5):
        self._size = 0
        self.capacity = m_size
        self.arr = []
        self.resize()
    def pop(self):
        self._size -= 1
        return self.arr[self._size]
    def back(self):
        return self.arr[self._size-1]
    def push(self, el):
        if self._size > self.capacity * 0.9:
            self.capacity *= 2
            self.resize()
        self.arr[self._size] = el
        self._size += 1
    def empty(self):
        return self._size == 0

    def size(self):
        return self._size
    
    def resize(self):
        old = self.arr
        self.arr = [None] * self.capacity
        for i in range(self._size):
            self.arr[i] = old[i]

    

def solve(A, P):
    stack = Stack()
    n = A
    while n>0:
        stack.push(n % P)
        n //= P
    num = ""
    while not stack.empty():
        a = stack.pop()
        s = ""
        if a > 9:
            s = "[" + str(a) + "]"
        else:
            s = str(a)
        num = num + s
    return num
        



if __name__ == "__main__":
    A = int(input())
    P = int(input())
    print(solve(A, P))
