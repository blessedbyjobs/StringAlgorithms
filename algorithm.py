import numpy as np

class NaiveStringInclude(object):
    def __init__(self, file, pattern):
        self.file = file
        self.pattern = pattern

    def naive_string_match(self, line, line_number):
        n = len(line)
        m = len(self.pattern)

        for i in range(0, n - m + 1, 1):
            j = 0

            while j < m and self.pattern[j] == line[i + j]:
                j += 1

            if j == m:
                print("Есть вхождение на строке ", line_number, " в позиции ", i)

    def compare_strings(self, line):
        return len(line) > len(self.pattern)

    def check_text(self):
        with open(self.file) as fh:
            counter = 1
            for line in fh.readlines():
                if self.compare_strings(line):
                    self.naive_string_match(line, counter)
                    counter += 1


class StringBorder(object):
    def __init__(self, file):
        self.file = file

    def naive_string_border(self, line, counter):
        n = len(line)
        br = 0

        i = n - 1
        while not br and i:
            j = 0

            while j < i and line[j] == line[n - i + j]:
                j += 1

            if i == j:
                br = i

            i -= 1

        print("Наивный алгоритм - максимальная грань на", counter, "строке: ", br)

    def prefix_border_array(self, line, counter):
        n = len(line)
        bp = np.empty(n)
        bp[0] = 0

        for i in range(1, n, 1):
            bp_right = int(bp[i - 1])

            while bp_right and line[i] != line[bp_right]:
                bp_right = int(bp[bp_right - 1])

            if line[i] == line[bp_right]:
                bp[i] = bp_right + 1
            else:
                bp[i] = 0

        print("Алгоритм вычисления массива граней - массив граней на", counter, "строке: ", bp)

        self.prefix_border_array_m(line, counter, bp)

    def suffix_border_array(self, line, counter):
        n = len(line)
        bs = np.empty(n)
        bs[n - 1] = 0

        for i in range(n - 2, -1, -1):
            bs_left = int(bs[i + 1])

            while bs_left and line[i] != line[n - bs_left - 1]:
                bs_left = int(bs[n - bs_left])

            if line[i] == line[n - bs_left - 1]:
                bs[i] = bs_left + 1
            else:
                bs[i] = 0

        print("Алгоритм вычисления граней суффиксов - массив граней на", counter, "строке: ", bs)

        self.suffix_border_array_m(line, counter, bs)

    def prefix_border_array_m(self, line, counter, bp):
        n = len(line)
        bpm = np.empty(n)
        bpm[0] = 0
        bpm[n - 1] = bp[n - 1]

        for i in range(1, n - 1, 1):
            if bp[i] and (line[int(bp[i])] == line[i + 1]):
                bpm[i] = bpm[int(bp[i]) - 1]
            else:
                bpm[i] = bp[i]

        print("Алгоритм построения модифицированного массива bpm - массив граней на", counter, "строке: ", bpm)

        self.bpm_to_bp(bpm, line)

    def suffix_border_array_m(self, line, counter, bs):
        n = len(line)
        bsm = np.empty(n)
        bsm[n - 1] = 0
        bsm[0] = bs[0]

        for i in range(n - 2, 0, -1):
            if bs[i] and (line[int(bs[i])] == line[i - 1]):
                bsm[i] = bsm[n - int(bs[i])]
            else:
                bsm[i] = bs[i]

        print("Алгоритм построения модифицированного массива bsm - массив граней на", counter, "строке: ", bsm)

        self.bsm_to_bs(bsm, line)

    def bsm_to_bs(self, bsm, line):
        n = len(line)

        bs = np.empty(n)
        bs[0] = bsm[0]
        bs[n - 1] = 0
        for i in range(1, n - 1, 1):
            bs[i] = max(bs[i - 1] - 1, bsm[i])

        print("Алгоритм преобразования bsm в bs: ", bs)

    def bpm_to_bp(self, bpm, line):
        n = len(line)

        bp = np.empty(n)
        bp[n - 1] = bpm[n - 1]
        bp[0] = 0
        for i in range(n - 2, 0, -1):
            bp[i] = max(bp[i + 1] - 1, bpm[i])

        print("Алгоритм преобразования bpm в bp: ", bp)

    def check_text(self):
        with open(self.file) as fh:
            counter = 1
            for line in fh.readlines():
                self.naive_string_border(line, counter)
                self.prefix_border_array(line, counter)
                self.suffix_border_array(line, counter)
                counter += 1
