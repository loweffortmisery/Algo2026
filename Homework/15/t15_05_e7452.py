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


    def PrintReverse(self) -> None:
        """Вивести елементи Зв'язного Списку в зворотному порядку"""
        data = self.get_data()
        for i in range(len(data)-1, -1, -1):
            print(data[i], end=" ")

if __name__ == "__main__":
    n = int(input())
    mylist = List()
    for x in input().split():
        mylist.addToTail(int(x))
    mylist.Print()
    mylist.PrintReverse()
