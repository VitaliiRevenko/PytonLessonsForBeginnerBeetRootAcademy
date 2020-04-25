'''Task 2

from typing import Optional
def is_palindrome(looking_str: str, index: int = 0) -> bool:
    """
    Checks if input string is Palindrome
    is_palindrome('mom')
    True

    is_palindrome('sassas')
    True

    is_palindrome('o')
    True
    """
    pass'''

#Recursion
import timeit
def is_palindrome(looking_str) -> bool:
    if len(looking_str) == 1:
        return looking_str
    return looking_str[-1] + is_palindrome(looking_str[:-1])
if __name__ == '__main__':
    print(is_palindrome('mom'))
    print(is_palindrome('vitalii'))
    print(is_palindrome('o'))
    print(timeit.repeat(lambda: is_palindrome(looking_str='mom')))
#####################################################################
#Вариант в одну строчку (in one line)
##def is_palindrome(looking_str): return looking_str[0] if len(looking_str)==1 else looking_str[len(looking_str)-1] + is_palindrome(looking_str[0:len(looking_str)-1])
#####################################################################
#Slise
# import timeit
# def is_palindrome1(looking_str, index:int = 0) -> bool:
#     rev = looking_str[::-1]
#     return looking_str == rev
#
# print(is_palindrome1('moma'))
# print(is_palindrome1('sassas'))
# print(is_palindrome1('o'))
# print(timeit.repeat(lambda: is_palindrome1(looking_str='mom')))
#####################################################################
#With Join and reversed
# def is_palindrome2(looking_str, index:int = 0) -> bool:
#     rev = "".join(reversed(looking_str))
#     return looking_str == rev
#
# print(is_palindrome('mom'))
# print(is_palindrome('sassas'))
# print(is_palindrome('o'))
# print(timeit.repeat(lambda: is_palindrome1(looking_str='mom')))
####################################################################


