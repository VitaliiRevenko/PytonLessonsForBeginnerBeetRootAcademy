# Task 2
# Write a Python program to access a function inside a function (Tips: use function, which returns another function)
def test(word):
    def low(it):
        if it.isdigit():
            return 'N'
        return it.lower()
    res = ''
    for i in word:
        res += low(i)
    return res
print(test('BEET Root Academy 2020'))
