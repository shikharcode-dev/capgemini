 # four pillars of oops
# 1. Encapsulation = binding data and functions together in a single unit called class. It also hides the internal details of the class from the outside world. It is achieved by using access specifiers like private, protected and public.
# 2. Inheritance = It allows a class to acquire the properties and methods of another class. The class that inherits is called derived class and the class from which it inherits is called base class.

# types of inheritance and their examples =
# 1. Single Inheritance = A class inherits from a single base class.
# example of single inheritance
# class Animal:
#     def eat(self):
#         print("Animal is eating")

# 2. Multiple Inheritance = A class inherits from multiple base classes.
# example of multiple inheritance
# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")
#create object of Dog class
# obj = Dog()
# obj.eat()
# obj.bark()

#Question = use single level inheritance for two classes , employee and develpoper. create parent class as employee inisitilise sally and create child class as developer add propgramming language and diaplay all detailes of employee and developer.
# Parent Class
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def show_employee(self):
#         print("Employee Name:", self.name)
#         print("Employee Salary:", self.salary)


# # Child Class
# class Developer(Employee):
#     def __init__(self, name, salary, language):
#         Employee.__init__(self, name, salary)
#         self.language = language

#     def show_developer(self):
#         print("Employee Name:", self.name)
#         print("Employee Salary:", self.salary)
#         print("Programming Language:", self.language)


# emp = Employee("Luffy", 50000)
# dev = Developer("Ichigo", 60000, "Python")

# print("Employee Details")
# emp.show_employee()

# print("\nDeveloper Details")
# dev.show_developer()




# using through function
# class employee:
#     def __init__(self, name, sallary):
#         self.name = name
#         self.sallary = sallary

#     def show_employee(self):
#         print(self.name, self.sallary)

# class developer(employee):
#     def __init__(self, name, sallary, lang):  # this is the constructor part and defined a self as default
#         # super() method is used to access methods and properties from the parent class
#         # It provides a way to call methods from the parent class without explicitly naming it
#         # super().__init__(name, sallary) is equivalent to employee.__init__(self, name, sallary)
#         # Benefits: 1) More maintainable - if parent class name changes, no need to update here
#         #          2) Supports multiple inheritance better
#         #          3) Cleaner and more Pythonic code
#         super().__init__(name, sallary)
#         self.lang = lang

#     def show_developer(self):
#         print(self.name, self.sallary, self.lang)

# # Example demonstration:
# # emp = employee("Luffy", 50000) - Creates an employee object with name "Luffy" and salary 50000
# # dev = developer("Ichigo", 60000, "Python") - Creates a developer object inheriting from employee
# # The developer class uses super() to call the parent constructor, then adds its own lang attribute
# # This shows inheritance where developer "is-a" employee with additional programming language skill
# emp = employee("Luffy", 50000)
# dev = developer("Ichigo", 60000, "Python")

# emp.show_employee()
# dev.show_developer() 




# # multilevel inheritance =  A class inherits from a derived class, making it a child of the child class. This creates a hierarchy of classes.
# # example of multilevel inheritance 
# # class A:
# #     def method_a(self):
# #         print("Method A")

# # class B(A):
# #     def method_b(self):
# #         print("Method B")

# # class C(B):
# #     def method_c(self):
# #         print("Method C")
# # obj = C()
# # obj.method_a() # inherited from class A

# # obj.method_b() # inherited from class B





# #example use the same example of employee and developer just add one more class as python developer and showing all inherit the above classes as multilevel inheritance
# class employee:
#     def __init__(self, name, sallary):
#         self.name = name
#         self.sallary = sallary
#     def show_employee(self):
#         print(self.name, self.sallary)


# class developer(employee):
#     def __init__(self, name, sallary, lang):
#         super().__init__(name, sallary)
#         self.lang = lang
#     def show_developer(self):
#         print(self.name, self.sallary, self.lang)


# class python_developer(developer):
#     def __init__(self, name, sallary, lang, framework):
#         super().__init__(name, sallary, lang)
#         self.framework = framework
#     def show_python_developer(self):
#         print(self.name, self.sallary, self.lang, self.framework)

# emp = employee("Luffy", 50000)
# dev = developer("Ichigo", 60000, "Python")
# py_dev = python_developer("Naruto", 70000, "Python", "Django")

# emp.show_employee()
# dev.show_developer()
# py_dev.show_python_developer() 




# # multiple inheritance = A class inherits from multiple base classes. This allows a class to have the properties and methods of more than one parent class.
# # example of multiple inheritance

# class cemera:
#     def take_photo(self):
#         print("it is use to take photo")

# class speaker:
#     def sound(self):
#         print("it is use to play music")

# class smartphone(cemera, speaker):
#     pass

# obj = smartphone()
# obj.take_photo() # inherited from cemera class
# obj.sound() # inherited from speaker class


# #MRO = method resolution order mean? = 
# # MRO (Method Resolution Order) is the order in which Python searches for methods in a class hierarchy
# # It determines which method gets called when there are multiple classes with the same method name
# # Python uses C3 linearization algorithm to determine MRO
# # You can check MRO using ClassName.__mro__ or ClassName.mro()

# # Example of MRO:
# class A:
#     def show(self):
#         print("Class A")

# class B(A):
#     def show(self):
#         print("Class B")

# class C(A):
#     def show(self):
#         print("Class C")

# class D(B, C):  # Multiple inheritance
#     pass

# # Check MRO
# print("MRO for class D:", D.__mro__)
# # Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# # When we call show() method on D object, it follows MRO: D -> B -> C -> A -> object
# obj = D()
# obj.show()  # This will print "Class B" because B comes before C in MRO 


# create a calculator using multiple inheritance create a class addition with method to add two numbers and subtraction create a class with method subtract two number. create a class multiplication with a method to multiply two numbers at last create a class calculator that will inherit from addition and subtraction and multiplication 
#create a object for calculator and perform that 3 operations 

# class addition:
#     def add(self, a, b):
#         print("Addition:", a + b)

# class subtraction:
#     def subtract(self, a, b):
#         print("Subtraction:", a - b)

# class multiplication:
#     def multiply(self, a, b):
#         print("Multiplication:", a * b)

# class calculator(addition, subtraction, multiplication):
#     pass

# obj = calculator()
# obj.add(10, 5)
# obj.subtract(10, 5)
# obj.multiply(10, 5)


# Hierarchical inheritance = Multiple classes inherit from a single base class. This creates a tree-like structure where one parent class has multiple child classes.
# In hierarchical inheritance, one base class serves as a parent to multiple derived classes
# All child classes share the common properties and methods of the parent class


# mam example
class employee:
    def log_in(self):
        print("employee login")

class developer(employee):
    def write_code(self):
        print("developer writing code")

class tester(employee):
    def test(self):
        print("tester testing code")

obj = tester()
obj1 = developer()

obj.log_in()
obj1.log_in()


# home work
# Question. create a resume builder using multilevel inheritance. create a class 1oth resume to store the personal details and 10th accedimic detiled 
#creare a class resume 12th that inharit from resume 10th and store 12th accedmic detils.
#create a class resume degree that inharit resume 12th class and store the accedmic details. use constructor chaining to insilized all the data 
#use method to display the resume detailed at each level
# create ojcect for 10,12th and degree class and display their resume.

# Class for 10th Resume
class Resume10th:
    def __init__(self, name, age, tenth_marks):
        self.name = name
        self.age = age
        self.tenth_marks = tenth_marks

    def show_10th(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("10th Marks:", self.tenth_marks)


# Class for 12th Resume
class Resume12th(Resume10th):
    def __init__(self, name, age, tenth_marks, twelfth_marks):
        super().__init__(name, age, tenth_marks)
        self.twelfth_marks = twelfth_marks

    def show_12th(self):
        self.show_10th()
        print("12th Marks:", self.twelfth_marks)


# Class for Degree Resume
class ResumeDegree(Resume12th):
    def __init__(self, name, age, tenth_marks, twelfth_marks, degree_marks):
        super().__init__(name, age, tenth_marks, twelfth_marks)
        self.degree_marks = degree_marks

    def show_degree(self):
        self.show_12th()
        print("Degree Marks:", self.degree_marks)


# Object of 10th Resume
r1 = Resume10th("Shikhar", 19, 85)

# Object of 12th Resume
r2 = Resume12th("Shikhar", 19, 85, 88)

# Object of Degree Resume
r3 = ResumeDegree("Shikhar", 19, 85, 88, 90)

# Display Resume Details
print("----- 10th Resume -----")
r1.show_10th()

print("\n----- 12th Resume -----")
r2.show_12th()

print("\n----- Degree Resume -----")
r3.show_degree()



#Q. create an employee amangement system using Hierarchical inheritance create a parrent class employee with name email. create two child class tech team and support(mamagement and experiance) team (programing and experiance). using constructor chaining with super function. create two method in parent class display basic detailed and contact details both in parent. extand these two methos in child class by adding their own detailed. use method chaining to diaplay the information of this two child class.

# Parent Class
class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_basic(self):
        print("Name:", self.name)

    def display_contact(self):
        print("Email:", self.email)


# Child Class 1 - Tech Team
class TechTeam(Employee):
    def __init__(self, name, email, programming, experience):
        super().__init__(name, email)
        self.programming = programming
        self.experience = experience

    def display_basic(self):
        super().display_basic()
        print("Programming Language:", self.programming)

    def display_contact(self):
        super().display_contact()
        print("Experience:", self.experience, "Years")


# Child Class 2 - Support Team
class SupportTeam(Employee):
    def __init__(self, name, email, management, experience):
        super().__init__(name, email)
        self.management = management
        self.experience = experience

    def display_basic(self):
        super().display_basic()
        print("Management Skill:", self.management)

    def display_contact(self):
        super().display_contact()
        print("Experience:", self.experience, "Years")


# Object of Tech Team
tech = TechTeam("John", "john@gmail.com", "Python", 3)

# Object of Support Team
support = SupportTeam("Sally", "sally@gmail.com", "Team Management", 5)

# Display Tech Team Details
print("----- Tech Team -----")
tech.display_basic()
tech.display_contact()

# Display Support Team Details
print("\n----- Support Team -----")
support.display_basic()
support.display_contact()