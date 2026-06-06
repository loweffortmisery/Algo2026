class Node():
    def __init__(self, item):
        self.data = item
        self.next = None
        self.prev = None

class Deque():
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def size(self):
        return self._size


    def push(self, item):
        return self.push_back(item)

    def push_back(self, item):
        if self._size == 0:
            self.first = self.last = Node(item)
        elif self._size == 1:
            node = Node(item)
            self.first.next = node
            node.prev = self.first
            self.last = node
        else:
            node = Node(item)
            node.prev = self.last
            self.last.next = node 
            self.last = node
        self._size += 1
        return "ok"

    def push_front(self, item):
        if self._size == 0:
            self.first = self.last = Node(item)
        elif self._size == 1:
            node = Node(item)
            self.last.prev = node
            node.next = self.last
            self.first = node
        else:
            node = Node(item)
            node.next = self.first
            self.first.prev = node
            self.first = node
        self._size += 1
        return "ok"

    def pop_back(self):
        if self._size == 0:
            raise IndexError
         
        item = self.back()
        if self._size == 1:
            self.clear()
        else:
            self._size -= 1
            self.last = self.last.prev
            self.last.next = None
        return item

    def pop(self):
        return self.pop_front()

    def pop_front(self):
        if self._size == 0:
            raise IndexError

        item = self.front()
        if self._size == 1:
            self.clear()
        else:
            self._size -= 1
            self.first = self.first.next
            self.first.prev = None
        return item

    def back(self):
        if self._size == 0:
            raise IndexError
        
        item = self.last.data
        return item
   
    def front(self):
        if self._size == 0:
            raise IndexError
        
        item = self.first.data
        return item
    
    def clear(self):
        self.first = self.last = None
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
    queue = Deque()
    with open("input.txt") as f:
        for line in f:
            res = queue.execute(line)
            # print(queue._items)
            print(res)
            if res == "bye":
                break
