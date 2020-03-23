#Task2
'''Create a function which takes as input two dicts with structure mentioned above,
then computes and returns the total price of stock.
''' 

stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
        }
prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
        }
total = {}
for key1, value1 in stock.items():
    for key2, value2 in prices.items():
        if key1 == key2:
            summa = value1 * value2
            print(key1, ':', summa)