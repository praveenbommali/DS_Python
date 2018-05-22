import pdb
import math


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next

    def insertAtBegin(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = newNode

    def insertAfterNode(self, prevNode, data):
        if prevNode is None:
            print("previous node should not be null")
            return
        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode

    def deleteNode(self, data):
        temp = self.head
        if temp is not None:
            # head is node to delete
            if temp.data == data:
                self.head = temp.next
                temp = None
                return
            while temp is not None:
                if temp.data == data:
                    break
                prevNode = temp
                temp = temp.next

            # if no node found with that data
            if temp == None:
                return

            prevNode.next = temp.next
            temp = None

    def deleteAtPosition(self, position):
        if self.head is None:
            return
        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return
        if temp.next is None:
            return

        next = temp.next.next

        temp.next = None
        temp.next = next

    def getCount(self):
        temp = self.head
        count = 0
        while (temp):
            count += 1;
            temp = temp.next

        return count

    def getCountRec(self, node):
        if (not node):
            return 0
        else:
            return 1 + self.getCountRec(node.next)

    def getCountR(self):
        return self.getCountRec(self.head)

    def searchElement(self, data):
        if self.head is None:
            return
        temp = self.head
        while (temp):
            if temp.data == data:
                return True
            temp = temp.next

        return False

    def swapNodes(self, key1, key2):
        if key1 is key2:
            return

        prevX = None
        currX = self.head
        while currX is not None and currX.data is not key1:
            prevX = currX
            currX = currX.next

        prevY = None
        currY = self.head
        while currY is not None and currY.data is not key2:
            prevY = currY
            currY = currY.next

        if currX is None or currY is None:
            return

        if prevX is not None:
            prevX.next = currY
        else:
            self.head = currY

        if prevY is not None:
            prevY.next = currX
        else:
            self.head = currX

        temp = currX.next
        currX.next = currY.next
        currY.next = temp

    def findNthNode(self, index):
        if index < 0:
            print("make sure index should be in +ve")
            return
        temp = self.head
        count = 0
        while (temp):
            if count == index:
                return temp.data
            temp = temp.next
            count += 1

    def findMidNodeApp1(self):
        noOfNodes = self.getCountR()
        print("No of nodes in LL : ", noOfNodes)
        if noOfNodes % 2 == 0:
            middleNode = math.ceil((noOfNodes / 2))
        else:
            middleNode = math.floor(noOfNodes / 2)

        temp = self.head
        count = 0
        while temp.next != None:
            if (count == middleNode):
                print("\nMid Node value  : ", temp.data)

            temp = temp.next
            count += 1

    def findMidNodeApp2(self):
        faster = self.head
        slower = self.head
        if faster.next is None:
            return

        while faster is not None and faster.next is not None:
            faster = faster.next.next
            slower = slower.next

        print("\nMid Node value (Approach 2) ", slower.data)

    def findMidNodeApp3(self):
        mid = self.head
        temp = self.head
        count = 0
        if mid is None:
            return
        while temp.next is not None:
            if count % 2 != 0:
                mid = mid.next
            count = count + 1
            temp = temp.next
        print("\nMid Node value (Approach3) ", mid.data)

    def findNthNodeFromLstAprch1(self, nodeNo):
        temp = self.head
        noOfNodes = self.getCount()
        requiredNodeNo = noOfNodes - nodeNo + 1

        count = 1
        while temp.next is not None:

            if count == requiredNodeNo:
                print("nth node from last : ", nodeNo, " value : ", temp.data)
                return
            count = count + 1
            temp = temp.next

    def findNthNodeFromLstAprch2(self, nodeNo):
        mainP = self.head
        refP = self.head
        if mainP is None or refP is None:
            return

        count = 0
        while refP.next is not None:
            if count >= nodeNo:
                break
            refP = refP.next
            count += 1

        print(refP.data)
        while refP.next is not None:
            mainP = mainP.next
            refP = refP.next

        print("nth node from last : ", nodeNo, " value : ", mainP.data)

    def deleteList(self):
        current = self.head

        while current:
            nextNode = current.next
            del current.data
            current = nextNode
        print("\nList deleted completed ")

    def frequencyNum(self, dataP):
        current = self.head
        count = 0
        while current is not None:
            if current.data == dataP:
                count += 1
            current = current.next
        return count

    def reverseLL(self):
        prevN = None
        curN = self.head
        nextN = None

        while curN is not None:
            nextN = curN.next
            curN.next = prevN
            prevN = curN
            curN = nextN

        self.head = prevN

    def reverseLLAprch2(self, node):
        if node is None:
            return

        first = node
        rest = first.next

        if rest is None:
            return

        self.reverseLLAprch2(rest)
        first.next.next = first
        first.next = None
        self.head = rest


if __name__ == '__main__':
    singlyLL = SinglyLinkedList()
    singlyLL.head = Node(1)
    secondNode = Node(2)
    thirdNode = Node(4)
    singlyLL.head.next = secondNode
    secondNode.next = thirdNode
    # singlyLL.printList()

    # Insert node at beginning
    singlyLL.insertAtBegin(0)
    # singlyLL.printList()
    singlyLL.insertAtEnd(5)
    singlyLL.insertAtEnd(24)
    singlyLL.insertAtEnd(25)
    singlyLL.insertAtEnd(49)
    singlyLL.insertAtEnd(55)
    singlyLL.insertAtBegin(12)
    singlyLL.insertAtBegin(67)
    singlyLL.insertAtBegin(11)
    # singlyLL.printList()
    singlyLL.insertAfterNode(secondNode, 3)
    singlyLL.printList()
    singlyLL.deleteNode(0)
    print("\n")
    singlyLL.printList()
    singlyLL.deleteNode(5)
    print("\n")
    singlyLL.printList()
    print("\n")
    singlyLL.deleteAtPosition(2)
    singlyLL.printList()
    print("\n No of nodes :", singlyLL.getCount())
    print("\n No of nodes in rec:  ", singlyLL.getCountR())
    print("Search the element in the list : \n")
    print("Element available in list ::: ", singlyLL.searchElement(3))
    print("Swap nodes :\n ")
    singlyLL.swapNodes(67, 55)

    singlyLL.printList()
    print("\nFind nth node as follows:(n=2)", singlyLL.findNthNode(2))
    print("\nPrinting the middle node in the LL : Approach_01 : ")
    singlyLL.findMidNodeApp1()
    singlyLL.findMidNodeApp2()
    singlyLL.findMidNodeApp3()
    singlyLL.findNthNodeFromLstAprch1(2)
    singlyLL.findNthNodeFromLstAprch2(2)  # need to check

    singlyLL.printList()
    print("Frequency of data :: 55", " count :: ", singlyLL.frequencyNum(55), '\n')

    singlyLL.reverseLL()
    singlyLL.printList()
    print("\n")
    singlyLL.reverseLLAprch2(singlyLL.head) # need to analyze
    singlyLL.printList()

    singlyLL.deleteList()
    print("Printing list after deletion ")
