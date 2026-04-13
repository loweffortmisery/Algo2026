class Node:

    def __init__(self, data: int):
        self.data: int = data
        self.next: [Node | None] = None

class List:

    def __init__(self):
        self.head: [Node | None] = None
        self.tail: [Node | None] = None
        self.size = 0

    def addToTail(self, val: int) -> None:
        """Додати число val в кінець Зв'язного Списку"""
        self.size += 1
        if self.head == None:
            self.head = self.tail = Node(val)
            return
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def RotateLeft(self, k: int) -> None:
        """Rotate the list to the left by k places"""
        
        k %= self.size
        if k == 0:
            return
        self.tail.next = self.head
        node = self.head
        while k > 1:
            node = node.next
            k -= 1
        self.tail = node
        self.head = node.next
        self.tail.next = None

    def RotateRight(self, k: int) -> None:
        """Rotate the list to the right by k places"""
        self.RotateLeft(self.size - (k % self.size))

    def get_data(self):
        data = []
        node = self.head
        while node is not None:
            data.append(node.data)
            node = node.next   
        return data

    def Print(self) -> None:
        """Вивести елементи Зв'язного Списку"""
        print(*(self.get_data()))


if __name__ == "__main__":
    n = int(input())
    mylist = List()
    for x in input().split():
        mylist.addToTail(int(x))
    try:
        while 1:
            k = int(input())
            mylist.RotateRight(k)
            mylist.Print()
    except Exception:
        pass
