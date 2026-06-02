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
class employee:
    def __init__(self, name, sallary):
        self.name = name
        self.sallary = sallary

    def show_employee(self):
        print(self.name, self.sallary)

class developer(employee):
    def __init__(self, name, sallary, lang):  # this is the constructor part and defined a self as default
        # super() method is used to access methods and properties from the parent class
        # It provides a way to call methods from the parent class without explicitly naming it
        # super().__init__(name, sallary) is equivalent to employee.__init__(self, name, sallary)
        # Benefits: 1) More maintainable - if parent class name changes, no need to update here
        #          2) Supports multiple inheritance better
        #          3) Cleaner and more Pythonic code
        super().__init__(name, sallary)
        self.lang = lang

    def show_developer(self):
        print(self.name, self.sallary, self.lang)

# Example demonstration:
# emp = employee("Luffy", 50000) - Creates an employee object with name "Luffy" and salary 50000
# dev = developer("Ichigo", 60000, "Python") - Creates a developer object inheriting from employee
# The developer class uses super() to call the parent constructor, then adds its own lang attribute
# This shows inheritance where developer "is-a" employee with additional programming language skill
emp = employee("Luffy", 50000)
dev = developer("Ichigo", 60000, "Python")

emp.show_employee()
dev.show_developer() 




# multilevel inheritance =  A class inherits from a derived class, making it a child of the child class. This creates a hierarchy of classes.
# example of multilevel inheritance 
# class A:
#     def method_a(self):
#         print("Method A")

# class B(A):
#     def method_b(self):
#         print("Method B")

# class C(B):
#     def method_c(self):
#         print("Method C")
# obj = C()
# obj.method_a() # inherited from class A

# obj.method_b() # inherited from class B





#example use the same example of employee and developer just add one more class as python developer and showing all inherit the above classes as multilevel inheritance
class employee:
    def __init__(self, name, sallary):
        self.name = name
        self.sallary = sallary
    def show_employee(self):
        print(self.name, self.sallary)


class developer(employee):
    def __init__(self, name, sallary, lang):
        super().__init__(name, sallary)
        self.lang = lang
    def show_developer(self):
        print(self.name, self.sallary, self.lang)


class python_developer(developer):
    def __init__(self, name, sallary, lang, framework):
        super().__init__(name, sallary, lang)
        self.framework = framework
    def show_python_developer(self):
        print(self.name, self.sallary, self.lang, self.framework)

emp = employee("Luffy", 50000)
dev = developer("Ichigo", 60000, "Python")
py_dev = python_developer("Naruto", 70000, "Python", "Django")

emp.show_employee()
dev.show_developer()
py_dev.show_python_developer() 