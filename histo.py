#!/usr/bin/env python
import fileinput
import math


class Histogram(object):

    """Statistical histograms based on Sturges rule"""

    def __init__(self, data):
        self.data = sorted(data)
        self.size = len(self.data)
        self.max_value = max(self.data)
        self.min_value = min(self.data)

        if self.min_value != self.max_value:
            classes = round(1.0 + 3.32 * math.log10(self.size))
        else:
            classes = 1
        self.step = (self.max_value - self.min_value) / classes
        self.classes = int(classes)

    def _get_ranges(self):
        for klass in range(self.classes):
            range_l = int(self.min_value + self.step * klass)
            range_r = int(self.min_value + self.step * (klass + 1))
            yield str(range_l) + " - " + str(range_r)

    def _get_frequencies(self):
        index = 0
        step = self.min_value + self.step
        frequencies = [0 for _ in range(self.classes)]

        for value in self.data:
            if value <= step:
                frequencies[index] += 1
            else:
                while value > step + 1:
                    step += self.step
                    index += 1
                try:
                    frequencies[index + 1] += 1
                except IndexError:
                    frequencies[index] += 1
        for index in range(self.classes):
            frequencies[index] = frequencies[index] * 100.0 / self.size
        return frequencies

    def plot(self):
        width = len(str(self.max_value)) * 2 + 3
        hr = '-' * (width + 13)
        print hr
        print '{0:>{width}} | {1:>10}'.format('Range', 'Frequency', width=width)
        print hr
        for _range, freq in zip(self._get_ranges(), self._get_frequencies()):
            print '{0:>{width}} | {1:>8.4f} %'.format(_range, freq, width=width)
        print hr


def main():
    data = [int(line) for line in fileinput.input()]
    Histogram(data).plot()

if __name__ == '__main__':
    main()
