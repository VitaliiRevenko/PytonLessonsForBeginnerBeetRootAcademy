# Task 1
# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
# Напишите декоратор, который печатает функцию с переданными ей аргументами. НОТА! Следует печатать функцию, а не результат ее выполнения!
# For example:
#  "add called with 4, 5"

def logger(func):
    '''
    надо создать врапер функцию которая примет аргс и кваргс и внутри себя вызовет func с принятыми параметрами и вернет результат выполнения этого функа
    а так же напишет что функ был вызван с такими то параметрами.
    и вернуть из логера надо врапер а не функ
    '''
    def wrap(*args, **kwargs):
        print("Running func", func.__name__, args, kwargs)
        print(func(*args))
        return func(*args, **kwargs)
    return wrap

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

'''
традиционно прошу использовать if __name__ == "__main__"
'''
if __name__ == '__main__':
    add(4, 5)
    square_all(4, 5)
