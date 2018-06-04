# Shell  Sort Algorithm implementation
class ShellSortImpl(object):
    def __init__(self, inputdata):
        self.inputdata = inputdata

    def shell_sort(self):
        input_len = len(self.inputdata)
        gap = input_len // 2

        while gap > 0:
            for i in range(gap, input_len):
                v = self.inputdata[i]
                j = i
                while j >= gap and self.inputdata[j - gap] > v:
                    self.inputdata[j] = self.inputdata[j - gap]
                    j -= gap
                self.inputdata[j] = v
            gap = gap // 2

        print(self.inputdata)


if __name__ == '__main__':
    inputdata = [14, 18, 19, 37, 23, 40, 9, 30, 11]
    shellSortImpl = ShellSortImpl(inputdata)
    shellSortImpl.shell_sort()
