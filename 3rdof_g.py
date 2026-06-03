# Hybrid Inheritance = It is a combination of multiple types of inheritance (like multilevel + multiple inheritance)
# Hybrid inheritance combines two or more types of inheritance in a single program
# It creates a complex inheritance structure where classes can inherit from multiple parents
# and also have multi-level inheritance chains

# Example: University Management System
# This example demonstrates hybrid inheritance combining:
# 1. Multilevel inheritance: Person -> Student -> GraduateStudent
# 2. Multiple inheritance: GraduateStudent inherits from both Student and ResearchAssistant

# Base Class - Level 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Derived Class - Level 2 (Multilevel inheritance from Person)
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def show_student(self):
        self.show_person()
        print(f"Student ID: {self.student_id}")


# Another Base Class for Multiple Inheritance
class ResearchAssistant:
    def __init__(self, research_area):
        self.research_area = research_area
    
    def show_research(self):
        print(f"Research Area: {self.research_area}")


# Hybrid Inheritance - Level 3
# GraduateStudent inherits from Student (multilevel) and ResearchAssistant (multiple)
class GraduateStudent(Student, ResearchAssistant):
    def __init__(self, name, age, student_id, research_area, thesis_topic):
        Student.__init__(self, name, age, student_id)
        ResearchAssistant.__init__(self, research_area)
        self.thesis_topic = thesis_topic
    
    def show_graduate(self):
        self.show_student()
        self.show_research()
        print(f"Thesis Topic: {self.thesis_topic}")


# Creating objects and displaying details
print("===== Graduate Student Details =====")
grad = GraduateStudent("Alex", 24, "GS001", "Artificial Intelligence", "Deep Learning in Healthcare")
grad.show_graduate()

# This demonstrates hybrid inheritance:
# - Person -> Student (Multilevel)
# - Student + ResearchAssistant -> GraduateStudent (Multiple + Multilevel = Hybrid) 








# Polymorphism: The ability of different objects to respond to the same method call in their own unique way.
# It allows methods with the same name to behave differently based on the object that calls them.
# In Python, polymorphism enables objects of different classes to be treated uniformly through a common interface.
# There are two main types: Method Overriding (runtime polymorphism) and Method Overloading (compile-time polymorphism).
# Types of Polymorphism in Python

# 1. Compile-time Polymorphism (Method Overloading)
# Python doesn't support traditional method overloading, but we can achieve it using default arguments or variable-length arguments

class Calculator:
    # Using default arguments to simulate method overloading
    def add(self, a, b=0, c=0):  # here c and b also overide and change the value to during when i call that in argument but bydefault it is 0.
        return a + b + c   # or print(a+b, a+b+c, a+b+c+d) kike that also

calc = Calculator()
print(calc.add(5))  #or calc.add(5) also like that        # Output: 5
print(calc.add(5, 10))       # Output: 15
print(calc.add(5, 10, 15))   # Output: 30



# Q. #create a classs area with a methiod calculate method in this method calculate of area of reactnge and square 
# This class demonstrates method overloading simulation in Python using default parameters
class Area:

    # The calculate method can work with one or two parameters
    # width=None is a default parameter - if no second argument is provided, width will be None
    def calculate(self, length, width=None):

        # Square calculation
        # Control flow: This if condition checks if width is None (meaning only one argument was passed)
        # None is a special Python value representing "no value" or "null"
        # When width is None, we treat the shape as a square
        if width is None:
            # For a square, area = side × side (both dimensions are equal)
            area = length * length
            print("Area of Square =", area)

        # Rectangle calculation
        # Control flow: The else block executes when width is NOT None (two arguments were passed)
        # When width has a value, we treat the shape as a rectangle
        else:
            # For a rectangle, area = length × width (two different dimensions)
            area = length * width
            print("Area of Rectangle =", area)


# Creating an object of the Area class
a = Area()

# First call: Only one argument (5) is passed
# Control flow: width remains None, so the if block executes → calculates square area
a.calculate(5)

# Second call: Two arguments (10, 4) are passed
# Control flow: width gets value 4 (not None), so the else block executes → calculates rectangle area
a.calculate(10, 4)

#simple way 
# class Area:

#     def calculate(self, length, width=None):
#         if width is None:
#             area = length * length
#             print("Area of Square =", area)
#         else:
#             area = length * width
#             print("Area of Rectangle =", area)



# a = Area()
# a.calculate(5)
# a.calculate(10, 4)










# 2. Runtime Polymorphism (Method Overriding)
# Child class provides a specific implementation of a method that is already defined in its parent class

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Demonstrating runtime polymorphism
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    animal.sound()

# Monkey Patching: The practice of dynamically modifying or extending classes or modules at runtime
# It allows you to change the behavior of existing code without modifying the original source code
# The term "monkey patching" comes from "guerrilla patching" - making quick fixes or changes on the fly
# While powerful, it should be used carefully as it can make code harder to understand and maintain
# Common use cases: fixing bugs in third-party libraries, adding features temporarily, or testing


















# 3. Duck Typing (Dynamic Polymorphism)
# "If it walks like a duck and quacks like a duck, it must be a duck"
# Python doesn't check the type of object, only if it has the required method

class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

class Butterfly:
    def fly(self):
        print("Butterfly is flying")

def make_it_fly(flying_object):
    flying_object.fly()

# All objects with fly() method can be used
make_it_fly(Bird())
make_it_fly(Airplane())
make_it_fly(Butterfly())











# 4. Operator Overloading
# Changing the behavior of operators for user-defined classes

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Overloading + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    # Overloading * operator
    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2  # Using overloaded + operator
p4 = p1 * 3   # Using overloaded * operator
print(p3)     # Output: Point(6, 8)
print(p4)     # Output: Point(6, 9)

#Q. create a box class with a weight attributes and overload the class operator to add the weight of boxes. try to perform addition between two objects

# Creating a Box class to demonstrate operator overloading
class Box:

    def __init__(self, weight):
        self.weight = weight

    def __add__(self, other):
        return self.weight + other.weight


box1 = Box(10)
box2 = Box(20)

total_weight = box1 + box2
print("Total Weight =", total_weight) 








# Encapsulation: The bundling of data (attributes) and methods that operate on that data within a single unit (class)
# It restricts direct access to some of an object's components, which is a means of preventing accidental interference and misuse
# Encapsulation is achieved by using access modifiers (public, protected, private) to control the visibility of class members
# It helps in data hiding and provides better control over data by using getter and setter methods
# Benefits: Increases security, provides data hiding, makes code more maintainable and flexible, and reduces complexity

# Access Specifiers in Python
# Access specifiers control the visibility and accessibility of class members (attributes and methods)
# Python uses naming conventions to indicate access levels, unlike other languages that use keywords

# 1. PUBLIC - Accessible from anywhere (inside class, outside class, in derived classes)
# Convention: Normal naming (no underscore prefix)
# These members can be accessed and modified from anywhere in the program

class PublicExample:
    def __init__(self):
        self.public_var = "I am public"  # Public attribute
    
    def public_method(self):  # Public method
        print("This is a public method")

obj = PublicExample()
print(obj.public_var)  # Can access directly - Output: I am public
obj.public_method()    # Can call directly - Output: This is a public method


# 2. PROTECTED - Should only be accessed within the class and its subclasses
# Convention: Single underscore prefix (_variable)
# It's a weak internal use indicator - Python doesn't enforce this, it's just a convention
# Other programmers understand they shouldn't access these members directly

class ProtectedExample:
    def __init__(self):
        self._protected_var = "I am protected"  # Protected attribute
    
    def _protected_method(self):  # Protected method
        print("This is a protected method")

class Child(ProtectedExample):
    def access_protected(self):
        print(self._protected_var)  # Can access in child class
        self._protected_method()    # Can call in child class

obj2 = ProtectedExample()
print(obj2._protected_var)  # Can still access (Python doesn't restrict), but shouldn't
child = Child()
child.access_protected()    # Proper way to access protected members


# 3. PRIVATE - Should only be accessed within the class itself
# Convention: Double underscore prefix (__variable)
# Python performs name mangling to make it harder to access from outside
# Name mangling changes __variable to _ClassName__variable

class PrivateExample:
    def __init__(self):
        self.__private_var = "I am private"  # Private attribute
    
    def __private_method(self):  # Private method
        print("This is a private method")
    
    def access_private(self):  # Public method to access private members
        print(self.__private_var)
        self.__private_method()

obj3 = PrivateExample()
# print(obj3.__private_var)  # This will cause an error - AttributeError
obj3.access_private()  # Correct way - Output: I am private, This is a private method

# You can still access using name mangling (but you shouldn't)
print(obj3._PrivateExample__private_var)  # Output: I am private


# Summary Example - All three together
class BankAccount:
    def __init__(self, name, balance):
        self.name = name              # Public - anyone can see account holder name
        self._account_number = "1234" # Protected - internal use, subclasses can access
        self.__pin = "5678"           # Private - only this class should access PIN
    
    def get_balance(self):            # Public method
        return f"Balance for {self.name}"
    
    def _verify_account(self):        # Protected method
        return "Account verified"
    
    def __check_pin(self, pin):       # Private method
        return pin == self.__pin

account = BankAccount("John", 1000)
print(account.name)           # ✓ Public - accessible
print(account._account_number) # ⚠ Protected - accessible but shouldn't use
# print(account.__pin)         # ✗ Private - will cause error



# create a procted variable in employee id and ascess in a inside a child 
class employee:
    def __init__(self,empid):
        self._empid= empid  #protected variable  

class manager(employee):
    def display(self):
        print("empid:", self._empid) 

m = manager(223)
m.display()


# There are 3 ways to access the private data or property:

# 1. NAME MANGLING - Using the mangled name format: _ClassName__variableName
# Syntax: object._ClassName__private_variable
# Python internally converts __variable to _ClassName__variable
# Example:
# class MyClass:
#     def __init__(self):
#         self.__private_var = "secret"
# obj = MyClass()
# print(obj._MyClass__private_var)  # Accessing using name mangling

# 2. GETTER METHOD - Creating a public method inside the class to return private data
# Syntax: Define a public method that returns the private variable
# This is the recommended and proper way to access private data
# Example:
# class MyClass:
#     def __init__(self):
#         self.__private_var = "secret"
#     def get_private_var(self):  # Getter method
#         return self.__private_var
# obj = MyClass()
# print(obj.get_private_var())  # Accessing through getter method

# 3. PROPERTY DECORATOR - Using @property to create a getter that can be accessed like an attribute
# Syntax: Use @property decorator above a method to make it accessible without parentheses
# This provides a cleaner syntax while maintaining encapsulation
# Example:
# class MyClass:
#     def __init__(self):
#         self.__private_var = "secret"
#     @property
#     def private_var(self):  # Property method
#         return self.__private_var
# obj = MyClass()
# print(obj.private_var)  # Accessing like an attribute (no parentheses needed)


#Ex
class student:
    def __init__(self):
        self.__marks= 95      #private variable

    #Setter method
    def set_marks(self, marks):
        self.__marks= marks

    #getter method
    def get_marks(self):
        return self.__marks
    
#creating metho
s= student()

#setting value
s.set_marks(98)

#getting value
print("Marks:",s.get_marks())