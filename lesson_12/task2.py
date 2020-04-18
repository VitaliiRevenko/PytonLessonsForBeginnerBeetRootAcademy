'''Task 2
Library
Write a class structure that implements a library. Classes:
1) Library - name, books = [], authors = []
2) Book - name, year, author (author must be an instance of Author class)
3) Author - name, country, birthday, books = []
Library class
Methods:
- new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list
for the current library.
- group_by_author(author: Author) - returns a list of all books grouped by the specified author
- group_by_year(year: int) - returns a list of all the books grouped by the specified year
All 3 classes must have a readable __repr__ and __str__ methods.
Also, the book class should have a class variable which holds the amount of all existing books
'''
'''Библиотека Напишите структуру класса, которая реализует библиотеку. Классы: 
1) Библиотека - название, книги = [], авторы = [] 
2) Книга - имя, год, автор (автор должен быть экземпляром класса Author) 
3) Автор - имя, страна, день рождения, книги = [] 
Библиотечный класс Методы: - new_book (name: str, year: int, author: Author) - возвращает экземпляр класса Book
и добавляет книгу в список книг для текущей библиотеки. - group_by_author (автор: автор) - возвращает список всех книг,
сгруппированных указанным автором - group_by_year (year: int) - возвращает список всех книг,
сгруппированных по указанному году Все 3 класса должны иметь читаемые методы __repr__ и __str__. 
Кроме того, класс книги должен иметь переменную класса, которая содержит количество всех существующих книг.'''

class Library():
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
    def __repr__(self):
        pass
    def __str__(self):
        return "Name: {} | year: {} | author: {}".format(self.name, self.year, self.author)
        pass
    def new_book(self, name, year, author, *args):
        self.name = name
        self.year = year
        self.author = author
        list_book = []
        list_book.append(name)
        list_book.append(year)
        list_book.append(author)
        print(list_book)
        return Book
    pass
    def group_by_author(self, author):
        self.author = author
    def group_by_year(self, year):
        self.year = year
class Book(Library):
    def __repr__(self):
        pass
    def __str__(self):
        pass
    pass
class Author(Library):
    def __repr__(self):
        pass
    def __str__(self):
        pass
    pass
if __name__ == '__main__':
    book = Library()
    #book2 = Library()
    book.new_book("Book1", 1985, "Author1")
    book.new_book("Book2", 1986, "Author2")
    book.new_book("Book3", 1987, "Author3")
    #print(f"{book}\n{book2}")
    #print(Library.new_book())
