# Circular Linked list implementation with 2nd approach

from enum import Enum


class NodeConstants(Enum):
    FRONT_NODE = 1


class Node:
    def __init__(self, element=None, next_node=None):
        self.element = element
        self.next_node = next_node

    def __str__(self):
        if self.element:
            return self.element.__str__()
        else:
            return 'Empty Node'

    def __repr__(self):
        return self.__str__()


class CircularLL:
    def __init__(self):
        self.head = Node(element=NodeConstants.FRONT_NODE)
        self.head.next_node = self.head

    def size(self):
        count = 0
        current = self.head.next_node
        while current != self.head:
            count += 1
            current = current.next_node
        return count

    def insert_front(self, data):
        newNode = Node(element=data, next_node=self.head.next_node)
        self.head.next_node = newNode

    def insert_last(self, data):
        current_node = self.head.next_node
        while current_node.next_node != self.head:
            current_node = current_node.next_node

        newNode = Node(element=data, next_node=current_node.next_node)
        current_node.next_node = newNode

    def insert_position(self, data, position):
        if position == 0:
            self.insert_front(data)
        elif position == self.size():
            self.insert_last(data)
        else:
            if 0 < position < self.size():
                current_node = self.head.next_node
                current_pos = 0

                while current_pos < position - 1:
                    current_pos += 1
                    current_node = current_node.next_node

                newNode = Node(element=data, next_node=current_node.next_node)
                current_node.next_node = newNode
            else:
                raise IndexError

    def printList(self):
        temp = self.head.next_node
        while temp != self.head:
            print(temp.element, end="->")
            temp = temp.next_node


if __name__ == '__main__':
    circularLL = CircularLL()
    circularLL.insert_front(10)
    circularLL.insert_last(20)
    circularLL.insert_position(13, 1)
    circularLL.printList()
