# Implementation of Queue using Circular Array

class CircularArrayQueueImpl(object):
    def __init__(self, capacity):
        self.front = 0
        self.rear = capacity - 1
        self.queueds = [None] * capacity
        self.size = 0
        self.capacity = capacity

    def enqueue(self, data):
        if self.isFull():
            print("Queue is full")
            return
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.queueds[self.rear] = data
            self.size += 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        else:
            delEle = self.queueds[self.front]
            print("\ndequeue element : ", delEle,"\n")
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
    def isEmpty(self):
        return self.size ==0


    def isFull(self):
        return self.size == self.capacity

    def printQueue(self):
        for i in self.queueds:
            print(i , end=" ")
        print("\n")


if __name__ == '__main__':
    circularArrayQueueImpl = CircularArrayQueueImpl(10)
    circularArrayQueueImpl.enqueue(10)
    circularArrayQueueImpl.enqueue(20)
    circularArrayQueueImpl.enqueue(30)
    circularArrayQueueImpl.enqueue(40)
    circularArrayQueueImpl.enqueue(50)
    circularArrayQueueImpl.enqueue(60)
    circularArrayQueueImpl.enqueue(70)
    circularArrayQueueImpl.enqueue(80)

    circularArrayQueueImpl.printQueue()
    circularArrayQueueImpl.dequeue()
    circularArrayQueueImpl.printQueue()
    circularArrayQueueImpl.enqueue(90)
    circularArrayQueueImpl.enqueue(100)
    circularArrayQueueImpl.enqueue(110)
    circularArrayQueueImpl.dequeue()
    circularArrayQueueImpl.enqueue(120)
    circularArrayQueueImpl.printQueue()


