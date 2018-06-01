# Stack implementation using Linked list


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackImpl(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def push(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
        else:
            newNode.next = self.root
            self.root = newNode

    def pop(self):
        print("deleted node :", self.root.data)
        self.root = self.root.next

    def printStack(self):
        temp = self.root
        while temp is not None:
            print(temp.data, end=" ->")
            temp = temp.next


if __name__ == '__main__':
    stackImpl = StackImpl()
    stackImpl.push(10)
    stackImpl.push(20)
    stackImpl.push(30)
    stackImpl.printStack()
    stackImpl.pop()
    stackImpl.printStack()
