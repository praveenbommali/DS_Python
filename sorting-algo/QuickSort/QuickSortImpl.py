# Implementation of Quick Sort Algorithm
class QuickSortImpl(object):
    def __init__(self):
        pass

    def quick_sort(self, input_data, start, end):
        if start < end:
            pivot = self.partition(input_data, start, end)
            self.quick_sort(input_data, start, pivot - 1)
            self.quick_sort(input_data, pivot + 1, end)

    def partition(self, input_data, low, high):
        i = low - 1
        pivot = input_data[high]
        for j in range(low, high):
            if input_data[j] <= pivot:
                i += 1
                input_data[i], input_data[j] = input_data[j], input_data[i]
        input_data[i + 1], input_data[high] = input_data[high], input_data[i + 1]
        return i + 1


if __name__ == '__main__':
    input_data = [7, 2, 1, 6, 8, 5, 3, 4]
    quickSortImpl = QuickSortImpl()
    quickSortImpl.quick_sort(input_data, 0, len(input_data) - 1)
    for i in range(len(input_data)):
        print(input_data[i], end=" ")
