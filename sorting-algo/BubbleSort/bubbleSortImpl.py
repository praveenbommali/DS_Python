# Implementation of Bubble Sort Algorithm

class BubbleSortImpl(object):
    def __init__(self, inputdata):
        self.inputdata = inputdata

    # While implementing this , against the each pass , count how many time swap happend

    def bubbleSort(self):
        passlen = len(self.inputdata)
        swap = 1
        count = 0
        for ele in reversed(range(passlen)):
            if swap:
                swap = 0
                count = 0
                for i in range(passlen - 1):
                    print("pass :", ele, " count", count)
                    if self.inputdata[i] > self.inputdata[i + 1]:
                        temp = self.inputdata[i]
                        self.inputdata[i] = self.inputdata[i + 1]
                        self.inputdata[i + 1] = temp
                        swap = 1
                        count += 1

        print(self.inputdata)


if __name__ == '__main__':
    inputdata = [20, 5, 4, 13, 22, 10, 88, 55, 2, 85]
    bubbleSortImpl = BubbleSortImpl(inputdata)
    bubbleSortImpl.bubbleSort()
