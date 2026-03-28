NMAX = 1000 + 7

class Stack:
    def __init__(self, max_size = NMAX):
        self._arr = [0] * max_size
        self._s = 0

    def push(self, num):
        self._arr[self._s] = num
        self._s += 1

    def pop(self):
        if self._s == 0:
            raise IndexError
        self._s -= 1

    def back(self):
        if self._s == 0:
            raise IndexError
        return self._arr[self._s - 1]
        
    def clear(self):
        self._s = 0

    def size(self):
        return self._s



def solve(array, n):
    current = n
    stack = Stack()
    for i in range(n-1, -1, -1):
        stack.push(array[i])
        while   (stack.size() > 0 
                and stack.back() == current):
            stack.pop()
            current -= 1
    if current == 0:
        print("Yes")
        return
    print("No")


if __name__ == "__main__":
    n = -1
    while (1):
        try:
            if n == -1:
                n = int(input())
                continue
            array = list(map(int, input().split()))
            if array[0] == 0:
                print()
                n = -1
                continue
            solve(array, n)

        except EOFError:
            break

