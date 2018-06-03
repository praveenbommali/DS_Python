# Implementation of Selection Sort

class SelectionSortImpl(object):

    def __init__(self, inputdata):
        self.inputdata = inputdata

    def selection_sort(self):
        input_lenght = len(self.inputdata)
        for i in range(input_lenght):
            min = i
            for j in range(i + 1, input_lenght):
                if self.inputdata[j] < self.inputdata[min]:
                    min = j

            temp = self.inputdata[min]
            self.inputdata[min] = self.inputdata[i]
            self.inputdata[i] = temp

        print(self.inputdata)

if __name__ == '__main__':
    inputdata = [20, 10, 5, 6, 2, 12, 17, 88, 76]
    selectionSortImpl = SelectionSortImpl(inputdata)
    selectionSortImpl.selection_sort()
