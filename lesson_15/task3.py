'''
Task 3
Write a class TypeDecorators which has several methods for converting results of functions to a specified type (if it's possible):
methods:
to_int
to_str
to_bool
to_float
Don't forget to use @wraps

class TypeDecorators:
    pass
@TypeDecorators.to_int
def do_nothing(string: str):
    return string

@TypeDecorators.to_bool

def do_something(string: str):

    return string

assert do_nothing('25') == 25

assert do_something('True') is True'''


class TypeDecorators:

    @staticmethod
    def to_int(func):
        def wrapper (arg):
            return int(func(arg))
        return wrapper
    @staticmethod
    def to_str(func):
        def wrapper(arg):
            return str(func(arg))
        return wrapper
    @staticmethod
    def to_bool(func):
        def wrapper(arg):
            return func(bool(arg))
        return wrapper
    @staticmethod
    def to_float(func):
        def wrapper(arg):
            return func(float(arg))
        return wrapper

@TypeDecorators.to_int
def do_nothing(string: str):
    return string

@TypeDecorators.to_bool
def do_something1(string: str):
    return string

@TypeDecorators.to_str
def do_something2(string: int):
    return string

@TypeDecorators.to_float
def do_something3(string: str):
    return string

assert do_nothing('25') == 25
assert do_something1("True") is True
assert do_something2(18) == '18'
assert do_something3("3.14") == 3.14











































