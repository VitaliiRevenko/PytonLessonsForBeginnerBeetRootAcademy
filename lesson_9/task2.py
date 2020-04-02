'''Task 2

Write a function that takes in two numbers from the user via input(), call the numbers a and b,
 and then returns the value of squared a divided by b, construct a try-except block which raises an exception
  if the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero).
      '''

def ab(a, b):
    c = a ** 2 / b
    return (c)
while True:
    try:
        a = int(input('Input A:\t'))
        b = int(input('Input B:\t'))
        print(ab(a, b))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    except ZeroDivisionError:
        print(ZeroDivisionError, "Oops... Division be zero")