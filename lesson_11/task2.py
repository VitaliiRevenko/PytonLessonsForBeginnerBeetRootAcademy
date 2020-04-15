'''Task 2
Mathematician
Implement a class Mathematician which is a helper class for doing math operations on lists
The class doesn't take any attributes and only has methods:
square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without positive numbers
filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'''
################
'''Задача 2 Математик Реализуйте класс Mathematician, который является вспомогательным классом 
для выполнения математических операций над списками. Класс не принимает никаких атрибутов и имеет только методы:
square_nums (принимает список целых чисел и возвращает список квадратов) 
remove_positives (берет список целых чисел и возвращает его без положительных чисел 
filter_leaps (берет список дат (целых) и удаляет те, которые не являются «високосными годами»'''
################
'''class Mathematician:
        pass
        m = Mathematician()
        assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
        assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
        assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]'''
from datetime import date
today = date.today()
class Mathematician:
    def square_nums(self, args):
        print(f"Incoming data:\n{args}")
        new_list = []
        for i in args:
            new_list.append(int(i**2))
        print(f"Square nums:{new_list}")
        return new_list
    def remove_positives(self, args):
        print(f"\nIncoming data:\n", args)
        new_list = []
        for i in args:
            if i < 0:
                new_list.append(i)
        print(f"Remove positives:{new_list}")
        return new_list
    def filter_leaps(self, args):
        print(f"\nIncoming data:\n", args)
        new_list = []
        for i in args:
            '''Определить високосный год или нет
            Если год не делится на 4, значит он обычный.
            Иначе надо проверить не делится ли год на 100.
            Если не делится, значит это не столетие и можно сделать вывод, что год високосный.
            Если делится на 100, значит это столетие и его следует проверить его делимость на 400.
            Если год делится на 400, то он високосный.'''
            # Если остаток от деления на 4 не равен нулю,
            # значит год не делится нацело на 4 и
            # не является високосным, т. е. он обычный.
            # Исключаем столетия, которые не делятся на 400
            if i % 4 != 0 or (i % 100 == 0 and i % 400 != 0):
                pass
            else:
                new_list.append(i)
        print(f"Filter leaps:{new_list}")
        return new_list
if __name__ == '__main__':
    m = Mathematician()
    assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
    assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
    assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
