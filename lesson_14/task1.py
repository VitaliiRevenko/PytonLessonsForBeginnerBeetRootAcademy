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
    return func

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

'''
традиционно прошу использовать if __name__ == "__main__"
'''
x = 4
y = 5
print(add(x=4, y=5)) #Печатаем функцию add
add_var = add(x, y)
print(add_var)
#print(logger(add(x, y)))
print(square_all(4, 5)) #Печатаем функцию square_all
square_all_func = square_all(4, 5)
print(square_all_func)
