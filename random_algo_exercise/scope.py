class Difference:
    def __init__(self, a):
        sel.elements = a

    def computeDifference(self):
        max = 0
        for i in range(len(self._elements)):
            absolute = abs(self._elements[i] - self.elements[j])
            if absolute > max:
                max = absolute
        self.maximumDifference = max



_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference
