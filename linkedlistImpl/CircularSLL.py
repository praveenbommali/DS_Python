class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSLL:
    def __init__(self):
        self.head = None

    def insertToEmpty(self, data):
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
            newNode.next = newNode
        self.head = newNode

    def insertAtBegin(self, data):
        if self.head is None:
            return self.insertToEmpty(data)
        newNode = Node(data)
        newNode.next =self.head
        self.head.next = newNode
        self.head = newNode





    def printList(self):
        if self.head is None:
            return
        temp = self.head
        print(temp.data)
        while temp.next != temp:
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == '__main__':
    circularSLL = CircularSLL()
    circularSLL.insertToEmpty(10)
    circularSLL.printList()
    circularSLL.insertAtBegin(21)
    circularSLL.printList()
