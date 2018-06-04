# Merge Sort Implementation

class MergeSortImpl(object):
    def __init__(self, inputdata):
        self.inputdata = inputdata

    def merge_sort_impl(self, inputdata, left, right):
        if left < right:
            mid = (left + (right - 1)) // 2
            self.merge_sort_impl(inputdata, left, mid)
            self.merge_sort_impl(inputdata, mid + 1, right)
            self.merge(inputdata, left, mid, right)

    def merge(self, inputdata, left, mid, right):
        l_len = mid - left + 1
        r_len = right - mid
        l_arr = [0] * l_len
        r_arr = [0] * r_len

        for i in range(0, l_len):
            l_arr[i] = inputdata[left + i]

        for j in range(mid, r_len):
            r_arr[i] = inputdata[mid + 1 + j]

        ll = 0
        r = 0
        k = ll
        while ll < l_len and r < r_len:
            if l_arr[ll] <= r_arr[r]:
                inputdata[k] = l_arr[ll]
                ll += 1
            else:
                inputdata[k] = r_arr[r]
                r += 1
            k += 1

        while ll < l_len:
            inputdata[k] = l_arr[ll]
            ll += 1
            k += 1

        while r < r_len:
            inputdata[k] = r_arr[r]
            r += 1
            k += 1


if __name__ == '__main__':
    inputdata = [2, 25, 3, 78, 23, 65, 11, 88, 99, 12]
    input_len = len(inputdata)
    mergeSortImpl = MergeSortImpl(inputdata)
    mergeSortImpl.merge_sort_impl(inputdata, 0, input_len - 1)
    print(inputdata)
