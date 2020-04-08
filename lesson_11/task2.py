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
class Mathematician:
    def square_nums(self, *args):
        print(f"Incoming data:\n", args)
        print("Square nums:")
        for i in args:
            print(i**2, end=" "*5)
        return args
    def remove_positives(self, *args):
        print(f"\nIncoming data:\n", args)
        print("Remove positives:")
        for i in args:
            if i < 0:
                print(i, end=" "*5)
    def filter_leaps(self,*args):
        print(f"\nIncoming data:\n", args)
        print("Filter leaps:")

m = Mathematician()
m.square_nums(7, 11, 5, 4)
m.remove_positives(26, -11, -8, 13, -90)
m.filter_leaps(2001, 1884, 1995, 2003, 2020)
