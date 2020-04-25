# Task 5
#
# def sum_of_digits(digit_string: str) -> int:
#     """
#     sum_of_digits('26') == 8
#     True
#
#     sum_of_digits('test')
#     ValueError("input string must be digit string")

#a+b = (a-1)+(b+1) - Extreme case(Крайний случай)
def sum_of_digits(digit_string: str) -> int:
    if digit_string.isdigit() == False:
        raise 'ValueError("input string must be digit string"'
    elif int(digit_string[0]) == 0:
        return digit_string[-1]
    return (int(digit_string[0]) - 1) + (int(digit_string[-1]) + 1)
print(sum_of_digits('26'))
assert sum_of_digits('26') == 8
sum_of_digits('test')