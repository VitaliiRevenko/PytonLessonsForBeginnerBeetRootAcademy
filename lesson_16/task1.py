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
        return self
    def __next__(self):
        try:
            result = self.iterable[self.start]
        except IndexError:
            raise StopIteration
        self.start += 1
        return self.start, result


iterator = with_index('BeetRoot')
for ch in iterator:
    print(ch)