#Task 1
#
# Create your own implementation of a built-in function enumerate, named `with_index`, which takes two parameters:
# `iterable` and `start`, default is 0. Tips: see the documentation for the enumerate function

# iterator protocol

class with_index():
    def __init__(self, iterable):
        self.iterable = iterable
        self.start = 0
    def __iter__(self):
        self.start = 0
        return self
    def __next__(self):
        if self.start < len(self.iterable):
            result = self.iterable[self.start]
            self.start += 1
            return self.start, result
        raise StopIteration


iterator = with_index('BeetRoot')
for ch in iterator:
    print(ch)
