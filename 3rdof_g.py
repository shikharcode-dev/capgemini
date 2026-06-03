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
