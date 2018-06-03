# Implementation of Insertion Sort Algorithm
class InsertionSortImpl(object):
    def __init__(self, inputdata):
        self.inputdata = inputdata

    def insertion_sort(self):
        for i in range(1, len(self.inputdata)):
            cur_ele = self.inputdata[i]
            j = i-1
            while j >= 0 and self.inputdata[j] > cur_ele:
                self.inputdata[j+1] = self.inputdata[j]
                j -=1
            self.inputdata[j+1] =cur_ele

        print(self.inputdata)
if __name__ == '__main__':
    inputdata = [6, 8, 1, 4, 5, 3, 7, 2]
    insertionSortImpl = InsertionSortImpl(inputdata)
    insertionSortImpl.insertion_sort()
