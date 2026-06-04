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


# # Without using ABC import, we can achieve abstraction by raising NotImplementedError
# # This approach doesn't enforce implementation at instantiation time, but at method call time

# class Shape:
#     def area(self):
#         raise NotImplementedError("Subclass must implement abstract method")

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
    
#     def area(self):
#         print(  self.length * self.width)

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
    
#     def area(self):
#         print(  self.side * self.side)


# # Creating objects
# b1 = Rectangle(5, 3)
# b2 = Square(5)

# b2.area()
# b1.area() 





# # with import
# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
    
#     def area(self):
#         print(  self.length * self.width)

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
    
#     def area(self):
#         print(  self.side * self.side)


# # Creating objects
# b1 = Rectangle(5, 3)
# b2 = Square(5)

# b2.area()
# b1.area()

# #Q. create abstract class payment with an abstract method pay now create a child class, cradit card class and UPI and empliment the pay method in each child class

# from abc import ABC, abstractmethod

# class Payment(ABC):
#     @abstractmethod
#     def pay(self):
#         pass

# class CreditCard(Payment):
#     def pay(self):
#         print("Payment processed using Credit Card")

# class UPI(Payment):
#     def pay(self):
#         print("Payment processed using UPI")

# payment1 = CreditCard()
# payment1.pay()

# payment2 = UPI()
# payment2.pay()










# from abc import ABC, abstractmethod

# # Abstract Class
# class Payment(ABC):

#     @abstractmethod
#     def pay(self, amount):
#         pass


# # Credit Card Class
# class CreditCard(Payment):

#     def __init__(self, balance):
#         self.balance = balance

#     def pay(self, amount):
#         self.balance = self.balance - amount   # Decrement
#         print("Payment by Credit Card")
#         print("Remaining Balance =", self.balance)


# # UPI Class
# class UPI(Payment):

#     def __init__(self, balance):
#         self.balance = balance

#     def pay(self, amount):
#         self.balance = self.balance - amount   # Decrement
#         print("Payment by UPI")
#         print("Remaining Balance =", self.balance)


# # Objects
# c = CreditCard(5000)
# u = UPI(3000)

# # Payments
# c.pay(1000)
# u.pay(500)




# # LAMBDA FUNCTIONS IN PYTHON
# # Lambda functions are small anonymous functions defined using the 'lambda' keyword
# # They can have any number of arguments but only one expression
# # Syntax: lambda arguments: expression
# # They are useful for short, simple operations that are used once

# # Basic Lambda Function Examples

# # 1. Simple lambda function - add two numbers
# add = lambda x, y: x + y
# print(add(5, 3))  # Output: 8

# # 2. Lambda function with single argument - square a number
# square = lambda x: x ** 2
# print(square(4))  # Output: 16

# # 3. Lambda function to check if number is even
# is_even = lambda x: x % 2 == 0
# print(is_even(10))  # Output: True
# print(is_even(7))   # Output: False

# # 4. Lambda function with multiple arguments
# multiply = lambda x, y, z: x * y * z
# print(multiply(2, 3, 4))  # Output: 24

# # LAMBDA WITH BUILT-IN FUNCTIONS

# # 5. Using lambda with map() - applies function to all items in a list
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(lambda x: x ** 2, numbers))
# print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# # 6. Using lambda with filter() - filters items based on condition
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# # 7. Using lambda with reduce() - reduces list to single value
# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# sum_all = reduce(lambda x, y: x + y, numbers)
# print(sum_all)  # Output: 15

# # 8. Using lambda with sorted() - custom sorting
# students = [('Alice', 85), ('Bob', 75), ('Charlie', 90)]
# sorted_by_marks = sorted(students, key=lambda x: x[1])
# print(sorted_by_marks)  # Output: [('Bob', 75), ('Alice', 85), ('Charlie', 90)]

# # 9. Lambda function with conditional expression
# max_value = lambda x, y: x if x > y else y
# print(max_value(10, 20))  # Output: 20

# # 10. Lambda function with string operations
# uppercase = lambda text: text.upper()
# print(uppercase("hello"))  # Output: HELLO

# # PRACTICAL EXAMPLES

# # 11. Lambda with list of dictionaries
# products = [
#     {'name': 'Laptop', 'price': 1000},
#     {'name': 'Mouse', 'price': 20},
#     {'name': 'Keyboard', 'price': 50}
# ]
# sorted_products = sorted(products, key=lambda x: x['price'])
# print(sorted_products)

# # 12. Lambda for calculating discount
# calculate_discount = lambda price, discount: price - (price * discount / 100)
# print(calculate_discount(1000, 10))  # Output: 900.0

# # 13. Lambda with multiple conditions
# grade = lambda marks: 'A' if marks >= 90 else 'B' if marks >= 80 else 'C' if marks >= 70 else 'F'
# print(grade(85))  # Output: B

# # ADVANTAGES OF LAMBDA FUNCTIONS:
# # - Concise and readable for simple operations
# # - Can be used inline without defining a separate function
# # - Useful with map(), filter(), reduce(), sorted()
# # - Reduces code length for one-time use functions

# # LIMITATIONS OF LAMBDA FUNCTIONS:
# # - Can only contain a single expression
# # - Cannot contain statements or multiple expressions
# # - Less readable for complex operations
# # - Cannot include documentation strings
# # - Difficult to debug compared to regular functions





# #mam ex=
# def add(a,b):
#     print(a+b)
# add(3,2)

# var1 = lambda a,b : (a+b)
# print(var1)

# # writa a lamba function to find wether a number is less than 10 and grater than 0
# range = lambda x: 0 < x < 10
# print(range(5))   
# print(range(15))  
# print(range(-1))  

# # Alternative method using if-else statements
# def check_range(x):
#     return 0 < x < 10

# print(check_range(5))
# print(check_range(15))
# print(check_range(-1))


# #Q. WRP to check string is pallidrom or not
# is_palindrome = lambda s: s == s[::-1]
# print(is_palindrome("racecar"))  
# print(is_palindrome("hello"))    
# print(is_palindrome("madam"))    

# # Alternative method using if-else statements
# def check_palindrome(s):
#     return s == s[::-1]

# print(check_palindrome("racecar"))
# print(check_palindrome("hello"))
# print(check_palindrome("madam"))



# WAP to check if a character is present in a string or not
char_in_string = lambda s, char: char in s
print(char_in_string("hello", "e")) 
print(char_in_string("hello", "z"))   
print(char_in_string("python", "p"))

#Q. WAP to check the given is string is keyword or not
import keyword
is_keyword_control = lambda s: True if s in keyword.kwlist else False
print(is_keyword_control("if"))      
print(is_keyword_control("hello"))   
print(is_keyword_control("for"))     
print(is_keyword_control("class"))   


# Find maximum of two numbers using lambda
max_of_two = lambda a, b: a if a > b else b
print(max_of_two(10, 20))  
print(max_of_two(50, 30))  
print(max_of_two(15, 15))  



# WAP to return square if collection has even length, otherwise return cube
square_or_cube = lambda collections: len(collections) ** 2 if len(collections) % 2 == 0 else len(collections) ** 3
print(square_or_cube([1, 2, 3, 4]))      
print(square_or_cube([1, 2, 3]))         
print(square_or_cube("hello"))           
print(square_or_cube("test")) 



# WAP return a dictonry of a numbers and square of the number pair
numbers_to_squares = lambda nums: {num: num**2 for num in nums} # this is comprehension part. 
print(numbers_to_squares([1, 2, 3, 4, 5]))
print(numbers_to_squares([10, 20, 30]))
print(numbers_to_squares(range(1, 6)))
