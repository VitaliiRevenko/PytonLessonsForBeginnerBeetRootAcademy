'''Task 1

Write a function called oops that explicitly raises an IndexError exception when called.
 Then write another function that calls oops inside a try/except state­ment to catch the error.
  What happens if you change oops to raise KeyError instead of IndexError?'''

def oops():
    a = (1, 2, 3)
    print(a[3])
#oops()
####################
def oops2():
    try:
        oops()

    except IndexError:
        print('Это ошибка')
    raise KeyError
oops2()