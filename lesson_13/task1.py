# Task 1
# Write a Python program to detect the number of local variables declared in a function.
def variable():
    x = 1
    y = 2
    str1 = "BeetRoot"
    lst = [1, 2, 3]
    dct = {"1": 1, "2": 2}
    print("BeetRoot")
def variable2():
    z = 3
    str2 = "BeetRoot"
    lst = [1, 2, 3]
    print("BeetRoot")
#Function __code__(code object containing compiled function bytecode),co_nlocals (number of local variables)
print(variable.__code__.co_nlocals)
print(variable2.__code__.co_nlocals)