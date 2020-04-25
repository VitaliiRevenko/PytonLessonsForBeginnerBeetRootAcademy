'''Task 3

from typing import Optional
def mult(a: int, n: int) -> int:
    """
    This function works only with positive integers

    mult(2, 4) == 8
    True

    mult(2, 0) == 0
    True

    mult(2, -4)
    ValueError("This function works only with postive integers")
    """'''
from typing import Optional
import math
def mult(a: int, n: int) -> int:
    if a == 1:
        return n
    elif a < 0 or n < 0:
        raise "This function works only with postive integers"
    return n + mult(a-1, n)

if __name__ == '__main__':
    print(mult(2, 4))
    print(mult(2, 0))
    print(mult(2, -4))
    assert mult(2, 4) == 8
    assert mult(2, 0) == 0
