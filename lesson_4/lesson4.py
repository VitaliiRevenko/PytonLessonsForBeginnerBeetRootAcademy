# Task 1
'''import random

print("Lets play the game 'Guess the number'")
while True:
    number_comp = random.randint(1, 10)
    number_user = int(input('Enter the number from 1 to 10:\t'))
    if number_comp == number_user:
        print('You are win!!!')
        print(f'Comp number {number_comp}\tUser number\t{number_user}')
        again = input('Try again? Y/N:\t')
        if again in {'Y', 'y'}:
            continue
        elif again in {'N', 'n'}:
            break
    else:
        print(f'Comp number {number_comp}\tUser number\t{number_user}')
        print('game over')
        again = input('Try again? Y/N:\t')
        if again in {'Y', 'y'}:
            continue
        elif again in {'N', 'n'}:
            break
'''
#Task 2
'''name = input('Enter your name:\t')
age = int(input('Enter yor age:\t'))
print(f"Hello {name} in your next birthday you'll be {age+1} age")
'''
#Task 3
import random
in_str = list(input('Enter a words:\t'))
i = 0
while i < 5:
    random.shuffle(in_str)
    print(in_str)
    i += 1

#Task 4
'''import random
num_1 = random.randint(1, 100)
num_2 = random.randint(1, 100)
result_1 = num_1 + num_2
result_2 = int(input(f'{num_1} + {num_2} =\t'))
while True:
    if result_1 == result_2:
        print('Its True')
        break
    else:
        print('Its False')
        break
'''