#task1
'''
The greatest number
Write a Python program to get the largest number from a list of random numbers with the length of 10
Constraints: use only while loop and random module to generate numbers'''

import random
list_2 = []
while len(list_2) <= 9:
    list_1 = random.randint(1, 10)
    list_2.append(list_1)
print(f'Output random list {list_2}')
print("Output MAX NUMBER:\t", max(list_2))

############################################

#task2
'''Exclusive common numbers.
Generate 2 lists with the length of 10 with random integers from 1 to 10,
and make a third list containing the common integers between the 2 initial lists without any duplicates.
Constraints: use only while loop and random module to generate numbers'''

import random
list_1, list_2 = [], []
while len(list_1) <= 9:
    r1, r2 = random.randint(1, 10), random.randint(1, 10)
    list_1.append(r1)
    list_2.append(r2)
list_3 = list_1 + list_2
print(f'LIST1{list_1}\nLIST2{list_2}\nLIST3{set(list_3)}')

#############################################

#task3

'''Extracting numbers.
Make a list that contains all integers from 1 to 100, 
then find all integers from the list that are divisible by 7 but not a multiple of 5,
 and store them in a separate list. Finally, print the list.'''
import random
list_1 = []
list_2 = []
for i in range(0, 101):
    list_1.append(i)
    if list_1[i] % 7 == 0 and list_1[i] % 5 != 0:
        list_2.append(i)
    else:
        continue

print(list_1)
print(list_2)


