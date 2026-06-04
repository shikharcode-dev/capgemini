# # Abstraction
# # This is just the definition/concept for now - no implementation yet
# # Abstraction is a fundamental OOP principle that hides complex implementation details
# # and shows only the essential features of an object to the user
# # It focuses on what an object does rather than how it does it
# # In Python, abstraction can be achieved using abstract classes and abstract methods
# # from the abc (Abstract Base Class) module


# # Abstraction
# # This is just the definition/concept for now - no implementation yet
# # Abstraction is a fundamental OOP principle that hides complex implementation details
# # and shows only the essential features of an object to the user
# # It focuses on what an object does rather than how it does it
# # In Python, abstraction can be achieved using abstract classes and abstract methods
# # from the abc (Abstract Base Class) module

# # THREE KEY TERMINOLOGIES IN ABSTRACTION:

# # 1. ABSTRACT METHOD
# # - A method declared in an abstract class but has no implementation (no body)
# # - Must be implemented by any concrete (non-abstract) subclass
# # - Defined using @abstractmethod decorator
# # - Forces child classes to provide their own implementation
# # Syntax:
# # @abstractmethod
# # def method_name(self):
# #     pass

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass

# class Dog(Animal):
#     def sound(self):
#         return "Bark"

# # 2. ABSTRACT CLASS
# # - A class that cannot be instantiated (cannot create objects directly)
# # - Contains one or more abstract methods
# # - Serves as a blueprint for other classes
# # - Inherits from ABC (Abstract Base Class)
# # - Used to define common interface for subclasses
# # Syntax:
# # class ClassName(ABC):
# #     @abstractmethod
# #     def method_name(self):
# #         pass

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
    
#     @abstractmethod
#     def perimeter(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
    
#     def area(self):
#         return self.length * self.width
    
#     def perimeter(self):
#         return 2 * (self.length + self.width)

# # 3. CONCRETE CLASS
# # - A regular class that inherits from an abstract class
# # - Must implement all abstract methods from the parent abstract class
# # - Can be instantiated (objects can be created)
# # - Provides actual implementation of abstract methods
# # Syntax:
# # class ConcreteClass(AbstractClass):
# #     def abstract_method(self):
# #         # implementation here
# #         pass

# class Vehicle(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass

# class Car(Vehicle):  # Concrete class
#     def start_engine(self):
#         return "Car engine started"

# Example usage:
# dog = Dog()
# print(dog.sound())  # Output: Bark
# rect = Rectangle(5, 3)
# print(rect.area())  # Output: 15
# car = Car()
# print(car.start_engine())  # Output: Car engine started


# Without using ABC import, we can achieve abstraction by raising NotImplementedError
# This approach doesn't enforce implementation at instantiation time, but at method call time

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        print(  self.length * self.width)

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        print(  self.side * self.side)


# Creating objects
b1 = Rectangle(5, 3)
b2 = Square(5)

b2.area()
b1.area() 





# with import
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        print(  self.length * self.width)

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        print(  self.side * self.side)


# Creating objects
b1 = Rectangle(5, 3)
b2 = Square(5)

b2.area()
b1.area()

#Q. create abstract class payment with an abstract method pay now create a child class, cradit card class and UPI and empliment the pay method in each child class

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class CreditCard(Payment):
    def pay(self):
        print("Payment processed using Credit Card")

class UPI(Payment):
    def pay(self):
        print("Payment processed using UPI")

payment1 = CreditCard()
payment1.pay()

payment2 = UPI()
payment2.pay()










from abc import ABC, abstractmethod

# Abstract Class
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Credit Card Class
class CreditCard(Payment):

    def __init__(self, balance):
        self.balance = balance

    def pay(self, amount):
        self.balance = self.balance - amount   # Decrement
        print("Payment by Credit Card")
        print("Remaining Balance =", self.balance)


# UPI Class
class UPI(Payment):

    def __init__(self, balance):
        self.balance = balance

    def pay(self, amount):
        self.balance = self.balance - amount   # Decrement
        print("Payment by UPI")
        print("Remaining Balance =", self.balance)


# Objects
c = CreditCard(5000)
u = UPI(3000)

# Payments
c.pay(1000)
u.pay(500)




