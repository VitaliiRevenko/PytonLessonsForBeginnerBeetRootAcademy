'''Task 1
from typing import Optional
def to_power(x: Optional[int, float], exp: int) -> Optional[int, float]:
    Returns  x ^ exp

    to_power(2, 3) == 8
    True

    to_power(3.5, 2) == 12.25
    True

    to_power(2, -1)
    ValueError: This function works only with exp > 0.
    pass'''

import math
#a(n) = a (n-1)*a - Extreme case(Крайний случай)
def to_power(a:float, n: int):
    if n < 0:
        raise 'ValueError: This function works only with exp > 0'
    elif n == 0:
        return 1
    elif n % 2 == 1:  # if n odd number (нечетное)
        return to_power(a,n-1)*a
    else:   #if n even number (четное)
        return to_power(a**2, n//2)
    print(to_power)
if __name__ == '__main__':
    print(to_power(2, 3))
    print(to_power(3.5, 2))
    print(to_power(2, -1))
    assert (to_power(2, 3) == 8)
    assert to_power(3.5, 2) == 12.25