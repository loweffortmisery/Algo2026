class Stack:
    def __init__(self, m_size = 100+5):
        self._size = 0
        self.capacity = m_size
        self.arr = []
        self.resize()

    def top(self):
        #print(self.arr[self._size -1])
        #print(self._size)
        return self.arr[self._size - 1]


    def pop(self):
        self._size -= 1
        return self.arr[self._size]

    def back(self):
        return self.arr[self._size - 1]

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



def is_removable(prev_operand, used, next_operand):
    order = ["+", "-", "*", "/"]
    if prev_operand != "(":
        min_o = -1
        for i in range(len(order)):
            if order[i] in used:
                min_o = i
                break
        if prev_operand == "-":
            if min_o < 2:
                return False
        elif prev_operand == "*":
            if min_o < 2:
                return False
        elif prev_operand == "/":
            return False

    if next_operand in {"*", "/"}:
        if ("+" in used) or ("-" in used):
            return False
    return True


def simplify_brackets(expr):
    expr = '+' + expr + '+'
    L = len(expr)
    stack = Stack()
    to_skip = set()
    operands = {'+', '-', '*', '/'}
    for i in range(1, L-1):
        char = expr[i]
        if char == '(':
            stack.push([i, expr[i-1], set()])
            continue
        if char == ')':
            open_ind, prev_operand, used = stack.top()
            next_operand = expr[i+1]
            stack.pop()
            if is_removable(prev_operand, used, next_operand):
                to_skip.add(open_ind)
                to_skip.add(i)
                if not stack.empty():
                    stack.top()[2].update(used)
            continue
        if char in operands:
            if not stack.empty():
                stack.top()[2].add(char)
    res = ""
    for i in range(1, L-1):
        if i in to_skip:
            continue
        res = res + expr[i]
    #print(to_skip)
    #print(res)
    return res

def solve(S):
    L = len(S)
    stack = Stack()
    res = ""
    operands = {"*", "/", "+", "-"}
    for i in range(L-1, -1, -1):
        char = S[i]
        if not(char in operands):
            stack.push(char)
            continue
        
        a = stack.pop()
        b = stack.pop()
        s = '(' + a + char + b + ')'    
        stack.push(s)
    res = stack.pop()
    #print(res)
    res = simplify_brackets(res)
    return res



if __name__ == "__main__":
    S = input()
    print(solve(S))
