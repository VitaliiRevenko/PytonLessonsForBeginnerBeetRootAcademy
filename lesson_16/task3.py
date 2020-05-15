# Task 3
#
# Create your own implementation of an iterable, which could be used inside for-in loop. Also, add logic for retrieving
# elements using square brackets syntax.

class Iterable:
    def __init__(self, iter):
        self.iter = iter
        self.position = 0

    def __iter__(self):
        self.position = 0
        return self

    def __next__(self):
        if self.position < len(self.iter):
            result = self.iter[self.position]
            self.position += 1
            return result
        raise StopIteration

    def __getitem__(self, item):
        if item < len(self.iter):
            return self.iter[item]
        raise StopIteration

if __name__ == '__main__':
    itr = Iterable("123456789")
    print(itr[6])   # Output element by index
    for i in itr:   # loop for elements
        print(i)    # Output all iterable elements


