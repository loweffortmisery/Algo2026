class Node:

    def __init__(self, data: int):
        self.data: int = data
        self.next: [Node | None] = None

class List:

    def __init__(self):
        self.head: [Node | None] = None
        self.tail: [Node | None] = None

    def addToTail(self, val: int) -> None:
        """Додати число val в кінець Зв'язного Списку"""
        if self.head == None:
            self.head = self.tail = Node(val)
            return
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def _swap_by_num(self, a, b) -> None:
        if a > b:
            return self._swap(b, a)
        ind = 0
        node = self.head
        while node is not None:
            if ind == a:
                A = node
            if ind == b:
                B = node
                break
            ind += 1
            node = node.next
        A.data, B.data = B.data, A.data
        return

    def _swap_nodes(self, node_A, node_B):
        node_A.data, node_B.data = node_B.data, node_A.data
        return

    def ReorderList(self) -> None:
        """Перевпорядкувати список, як описано вище"""
        ind = 0
        node = self.head
        data = self.get_data()
        even = 0
        odd = len(data)-1
        while node is not None:
            if ind % 2 == 0:
                node.data = data[even]
                even += 1
            else:
                node.data = data[odd]
                odd -= 1
            ind += 1
            node = node.next
        return

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
    mylist.ReorderList()
    mylist.Print()
