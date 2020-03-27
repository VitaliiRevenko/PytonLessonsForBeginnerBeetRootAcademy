'''Task 3
A simple calculator.
Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
 (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments
  (only numbers) as the second parameter. Then return the sum or product of all the numbers
   in the arbitrary parameter. For example:
the call make_operation(‘+’, 7, 7, 2) should return 16
the call make_operation(‘-’, 5, 5, -10, -20) should return 30
the call make_operation(‘*’, 7, 6) should return 42  '''

def make_operation(action, abc):    #Функция выполняет математическое действие
    if action == '+':               # в зависимости от принятого математического знака
        answer = sum(abc)
    elif action == '*':
        answer = 1
        for i in abc:
            answer *= i
    elif action == '-':
        answer = 1
        for i in abc:
            answer -= i
    return (answer)
action = str(input('Enter action(+, -, *):\t'))  # Ввод действия
if action not in {'+', '-', '*'}:                # Проверка на верный введенный знак
    raise Exception("Oops! You Enter FALSE ACTION. Try again... ")  #Вызов ошибки, в случае неверного ввода операции
num = input('Enter numbers with a space:\t')    # Ввод чисел через пробел
try:
    abc = tuple(map(int, num.split(' ')))  # Записываю данные от пользователя в tuple()
    print(make_operation(action, abc))  # Запись в переменную d результат функции
except ValueError:                      # Вызов ошибки, если введена не цифра
    print("Oops!  That was no valid number.  Try again...")
