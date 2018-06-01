# Implementation of Stack ADT using Array Implementation

from enum import Enum


class StackCapacity(Enum):
    CAPACITY = 4


class Stack(object):
    def __init__(self):
        self.capacity = StackCapacity.CAPACITY
        self.stack = []
        self.top = 0

    def stack_size(self):
        return len(self.stack)

    def push(self, element):
        if self.stack_size() == 4:
            print("Stack is overflow")
            raise IndexError
        self.stack.append(element)

    def pop(self):
        if self.stack_size() == 0:
            print("Stack is underflow")
            raise IndexError
        return self.stack.pop()

    def print(self):
        print(self.stack)
        # self.stack.clear()


if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.print()
    # stack.pop()
    stack.print()

    stack.push(50)
    stack.push(60)
    stack.push(70)
