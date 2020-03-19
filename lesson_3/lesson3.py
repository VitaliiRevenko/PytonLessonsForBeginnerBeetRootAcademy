#task1
'''while True:
    s1 = input("Input word: \t")
    if len(s1) < 2:
        print('Empty String. Input please more than 1 simbol')
    else:
        print(s1[:2] + s1[-2:])
        print("Well done!!!")
        exit()

#task2

while True:
    number = input("Input telephone number: \t")
    if number.isdigit() and len(number) == 10:
        print('Данные введены корректно!')

        exit()
    else:
        print('Неверно введенные данные. Строка должна содержать 10 цифр')

#task3

while True:
    name = 'vitalii'
    name_input = input("Enter your name: \t")
    if name_input.lower() == name:
        print('Correct name!')
        exit()
    else:
        print('Please, enter correct name')
'''

# call to client

# Check valid telephone number
mobile_operators = ['067', '068', '063', '066', '050', '073', '097']
while True:
    phone_number = input("Enter your name telephone number(format +380 and 9 numbers of telephone number): \t")
    phone_number_slise = phone_number[1:]
    if phone_number[:2] == '+3':
        print('ok')
        if phone_number_slise[2:5] in mobile_operators:
            print('Your telephone operator is correct')
            if phone_number_slise.isdigit() \
                    and len(phone_number_slise) == 12 \
                    and phone_number_slise[2:5] in mobile_operators:
                print('Your telephone number is correct')
                break
            else:
                print('Please, enter correct telephone number')
        else:
            print('Please, enter correct of mobile operators code')

    else:
        print('First simbols of number must be +3')

# Check order
while True:
    oder = input("Is the order correct?:\t")
    if oder in {'Y', 'y'}:
        print('order confirmed')
    elif oder in {'N', 'n'}:
        print('order not confirmed')
        continue
# Check address delivery
    address = input("Is the address correct?:\t")
    if address in {'Y', 'y'}:
        print('Address is correct')
    elif address in {'N', 'n'}:
        print("Address isn't correct")
# Delivery method
    delivery1 = 'NewPost'
    delivery2 = 'UkrPost'
    delivery3 = 'MeestExpress'
    delivery = input(f'Input delivery method:\n {delivery1}\t {delivery2}\t {delivery3}')
    print(f'Your delivery method is {delivery}')
    print('Warranty terms bla bla bla...... ')
# Payment options
    pay1 = 'card'
    pay2 = 'cash'
    pay = input(f'Payment option {pay1} or {pay2}')
    if pay == pay1:
        print('Card payment')
    elif pay == pay2:
        print('Cash payment')
# Additional products
    add_product = input('Do You want buy additional products? Y/N')
    if add_product in {'Y', 'y'}:
        print('I want buy additional products')
        break
    elif add_product in {'N', 'n'}:
        print("I don't want buy additional products")
        break
print('END')