'''Task 1
Method overloading.
Create a base class named Animal with a method called talk and then create two subclasses: Dog and Cat,
and make their own implementation of the method talk be different. For instance, Dog’s can be to print ‘woof woof’,
while Cat’s can be to print ‘meow’.
Also, create a simple generic function, which takes as input instance of a Cat or Dog classes and performs talk method
 on input parameter. '''

def animals_sey_hello(animal):
    print(animal.talk())
class Animal:
    def talk(self):
        pass
class Cat (Animal):
    def talk(self):
        return 'meow'
class Dog(Animal):
    def talk(self):
        return 'gaw'
cat = Cat()
dog = Dog()
animals_sey_hello(cat)
animals_sey_hello(dog)