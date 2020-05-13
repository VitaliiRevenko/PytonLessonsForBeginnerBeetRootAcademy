# Task 2
#
# Create your own implementation of a built-in function range, named in_range(), which takes three parameters:
# `start`, `end`, and optional step. Tips: See the documentation for `range` function

class in_range():
    def __init__(self, start, end, optional_step):
        self.start = start
        self.end = end
        self.optional_step = optional_step
    def __iter__(self):
        return self
    def __next__(self):
        if self.start < self.end:
            x = self.start
            self.start += self.optional_step
            return x
        else:
            raise StopIteration

iterator = in_range(1, 10, 2)
for ch in iterator:
    print(ch)