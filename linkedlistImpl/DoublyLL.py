import gc


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLLImpl:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        newNode = Node(data)
        newNode.next = self.head

        if self.head is not None:
            self.head.prev = newNode

        self.head = newNode

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        newNode.prev = temp
        temp.next = newNode

    def insertAftNode(self, prevNode, data):
        if prevNode is None:
            return
        newNode = Node(data)

        newNode.prev = prevNode
        newNode.next = prevNode.next

        prevNode.next = newNode

    def deleteNode(self, delNode):
        if self.head is None or delNode is None:
            return
        if self.head == delNode:
            self.head - delNode.next

        if delNode.prev is not None:
            delNode.prev.next = delNode.next
        gc.collect()

    def reverseDLL(self):
        if self.head is None:
            return

        curr = self.head
        while curr:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev

        if temp is not None:
            self.head = temp.prev

    def printList(self):
        if self.head is None:
            return
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("\n")


if __name__ == '__main__':
    doublyLLImpl = DoublyLLImpl()
    doublyLLImpl.insertAtBegin(23)
    doublyLLImpl.insertAtBegin(24)
    doublyLLImpl.insertAtBegin(25)
    doublyLLImpl.insertAtBegin(26)
    doublyLLImpl.insertAtBegin(28)
    doublyLLImpl.printList()
    doublyLLImpl.insertAtEnd(45)
    doublyLLImpl.insertAtEnd(46)
    doublyLLImpl.printList()

    doublyLLImpl.insertAftNode(doublyLLImpl.head.next, 34)
    doublyLLImpl.printList()
    doublyLLImpl.deleteNode(doublyLLImpl.head.next.next)
    doublyLLImpl.printList()
    doublyLLImpl.reverseDLL()
    print("::::  Reverse List :::: ")
    doublyLLImpl.printList()
