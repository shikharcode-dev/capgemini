# # # Question. create a resume builder using multilevel inheritance. create a class 1oth resume to store the personal details and 10th accedimic detiled 
# # #creare a class resume 12th that inharit from resume 10th and store 12th accedmic detils.
# # #create a class resume degree that inharit resume 12th class and store the accedmic details. use constructor chaining to insilized all the data 
# # #use method to display the resume detailed at each level
# # # create ojcect for 10,12th and degree class and display their resume.



# # #Q. create an employee amangement system using Hierarchical inheritance create a parrent class employee with name email. create two child class tech team and support(mamagement and experiance) team (programing and experiance). using constructor chaining with super function. create two method in parent class display basic detailed and contact details both in parent. extand these two methos in child class by adding their own detailed. use method chaining to diaplay the information of this two child clas

# # # create a procted variable in employee id and ascess in a inside a child 
# # # create a procted variable in employee id and ascess in a inside a child 
# # class employee:
# #     def __init__(self,empid):
# #         self._empid= empid  #protected variable  

# # class manager(employee):
# #     def display(self):
# #         print("empid:", self._empid) 

# # m = manager(223)
# # m.display()


# # # H.W.=  create a parent class vecheil with the method start engin now create a child class car bike. override the methos start engin.





# # #Ex
# # class student:
# #     def __init__(self):
# #         self.__marks= 95      #private variable

# #     #Setter method
# #     def set_marks(self, marks):
# #         self.__marks= marks

# #     #getter method
# #     def get_marks(self):
# #         return self.__marks
    
# # #creating metho
# # s= student()

# # #setting value
# # s.set_marks(98)

# # #getting value
# # print("Marks:",s.get_marks())

# # # Property Decorator: A cleaner way to implement getters and setters in Python
# # # Instead of calling methods like get_marks() and set_marks(), we can access attributes directly
# # # The @property decorator makes a method behave like an attribute

# # class Student:
# #     def __init__(self):
# #         self._marks = 95  # Using single underscore as convention for "internal use"
    
# #     # Getter method - allows reading the value using student.marks
# #     @property
# #     def marks(self):
# #         return self._marks
    
# #     # Setter method - allows setting the value using student.marks = value
# #     @marks.setter
# #     def marks(self, value):
# #         if value >= 0 and value <= 100:  # Adding validation
# #             self._marks = value
# #         else:
# #             print("Invalid marks! Must be between 0 and 100")

# # # Creating object
# # s = Student()

# # # Getting value - no need to call get_marks(), just use it like an attribute
# # print("Marks:", s.marks)

# # # Setting value - no need to call set_marks(), just assign directly
# # s.marks = 98
# # print("Updated Marks:", s.marks)

# # # Validation in action
# # s.marks = 150  # This will print error message.


# # #test Q come on saturday
# # #Q. test cases question, 







# # # Alternative method using regular function
# # def check_char_in_string(s, char):
# #     return char in s

# # print(check_char_in_string("hello", "e"))
# # print(check_char_in_string("hello", "z"))
# # print(check_char_in_string("python", "p"))







# # #Q. WAP to check the given is string is keyword or not
# # import keyword
# # is_keyword = lambda s: keyword.iskeyword(s)
# # print(is_keyword("if"))      
# # print(is_keyword("hello"))   
# # print(is_keyword("for"))     
# # print(is_keyword("class")) 


# # WAP to return square if collection has even length, otherwise return cube
# # square_or_cube = lambda collection: len(collection) ** 2 if len(collection) % 2 == 0 else len(collection) ** 3
# # print(square_or_cube([1, 2, 3, 4]))      
# # print(square_or_cube([1, 2, 3]))         
# # print(square_or_cube("hello"))           
# # print(square_or_cube("test")) 



# # numbers_to_squares = lambda nums: {num: num**2 for num in nums}
# # print(numbers_to_squares([1, 2, 3, 4, 5]))
# # print(numbers_to_squares([10, 20, 30]))
# # print(numbers_to_squares(range(1, 6)))






# # # Method 2: Using map with custom function (more readable)
# # numbers = ['123', '345', '764']
# # def reverse_and_convert(string_num):
# #     reversed_string = string_num[::-1]  # Reverse the string using slicing
# #     return int(reversed_string)  # Convert to integer

# # result2 = list(map(reverse_and_convert, numbers))

# # print("\nUsing custom function:")
# # print("Original String List:", numbers)
# # print("Reversed Integer List:", result2)

# # Explanation:
# # x[::-1] reverses the string ('123' becomes '321')
# # int() converts the reversed string to integer
# # map() applies this operation to every element in the list





# # f = open("student.txt", "w")
# # f.write("Shikhar")
# # f.close()







# # l = [1,-5,-6,23]

# # # Filter positive numbers and calculate sum
# # result = sum(list(filter(lambda x: x > 0, l)))

# # print("Original List:", l)
# # print("Sum of Positive Numbers:", result)






# # Create a parent class Animal with a method eat().
# # Create a child class Dog that inherits from Animal.
# # Add a method bark() in the child class.
# # Create an object of Dog and call both methods.
# class Animal:
#     def eat(self):
#         print("The animal is eating")
# class Dog(Animal):
#     def bark(self):
#         print("The dog is barking: Woof! Woof!")

# my_dog = Dog()
# my_dog.eat()   
# my_dog.bark()





# # Create a parent class Employee.
# # Initialize:
# # employee name
# # salary
# # Create child class Developer.
# # Add:
# # programming language
# # Display all details.
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
    
#     def display_details(self):
#         print("Employee Name:", self.name)
#         print("Salary:", self.salary)
# class Developer(Employee):
#     def __init__(self, name, salary, programming_language):
#         super().__init__(name, salary)
#         self.programming_language = programming_language
    
#     def display_details(self):
#         super().display_details()
#         print("Programming Language:", self.programming_language)
# dev = Developer("John", 50000, "Python")
# dev.display_details() 








# class Resume10th:

#     def __init__(self, name, age, marks10):
#         self.name = name
#         self.age = age
#         self.marks10 = marks10

#     def show10(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("10th Marks:", self.marks10)


# class Resume12th(Resume10th):

#     def __init__(self, name, age, marks10, marks12):
#         Resume10th.__init__(self, name, age, marks10)
#         self.marks12 = marks12

#     def show12(self):
#         Resume10th.show10(self)
#         print("12th Marks:", self.marks12)


# class ResumeDegree(Resume12th):

#     def __init__(self, name, age, marks10, marks12, degree):
#         Resume12th.__init__(self, name, age, marks10, marks12)
#         self.degree = degree

#     def showDegree(self):
#         Resume12th.show12(self)
#         print("Degree:", self.degree)


# student1 = Resume12th("Rahul", 18, 85, 90)
# student2 = ResumeDegree("Shikhar", 21, 88, 92, "B.Tech")

# print("----- 12th Student Resume -----")
# student1.show12()

# print("\n----- Degree Student Resume -----")
# student2.showDegree()






# Problem Statement
# Create a Student class with a display() method that can:
# Display only the student's name
# Display name and age
# Display name, age, and course

# class Student:

#     def display(self, name, age=None, course=None):

#         print("Name:", name)

#         if age is not None:
#             print("Age:", age)

#         if course is not None:
#             print("Course:", course)

#         print()


# s = Student()
# s.display("Rahul")
# s.display("Shikhar", 19)
# s.display("Aman", 20, "B.Tech")





# Question: Create a base class called Vehicle and a child class called Car.The Vehicle class should initialize a brand attribute.The Car class should inherit from Vehicle and initialize its own model attribute.Implement constructor chaining using super() so that when a Car object is created, both the brand and model attributes are initialized correctly

# class Vehicle:

#     def __init__(self, brand):
#         self.brand = brand


# class Car(Vehicle):

#     def __init__(self, brand, model):
#         super().__init__(brand)
#         self.model = model

#     def display(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)


# c = Car("Toyota", "Fortuner")

# c.display()


# Question:Extend the previous Vehicle hierarchy by adding a third level:Grandparent Class (Vehicle): Initializes the brand.Parent Class (Car): Inherits from Vehicle and initializes the model.Child Class (ElectricCar): Inherits from Car and initializes a battery_capacity attribute.Implement chained constructors using super() so that all three attributes are properly initialized when an ElectricCar object is created.
# class Vehicle:

#     def __init__(self, brand):
#         self.brand = brand


# class Car(Vehicle):

#     def __init__(self, brand, model):
#         super().__init__(brand)
#         self.model = model


# class ElectricCar(Car):

#     def __init__(self, brand, model, battery_capacity):
#         super().__init__(brand, model)
#         self.battery_capacity = battery_capacity

#     def display(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Battery Capacity:", self.battery_capacity)


# e = ElectricCar("Tesla", "Model 3", "75 kWh")

# e.display()


# Question : Write a function safe_divide(a, b) that divides a by b. Use exception handling to catch scenarios where b is zero or if either input is not a number. Print distinct descriptive errors for each issue.

# def safe_divide(a, b):

#     try:
#         print("Result =", a / b)

#     except ZeroDivisionError:
#         print("Error: Cannot divide by zero")

#     except TypeError:
#         print("Error: Inputs must be numbers")


# safe_divide(10, 2)
# safe_divide(10, 0)
# safe_divide(10, "a") 





# Write a Python program that creates a generator function that yields cubes of numbers from 1 to n. Accept n from the user.

# # Generator function to yield cubes of numbers from 1 to n
# def cube_generator(n):
#     # Loop through numbers from 1 to n (inclusive)
#     for i in range(1, n + 1):
#         # Yield the cube of current number (i^3)
#         yield i ** 3

# # Accept input from user
# n = int(input("Enter a number: "))

# # Create generator object
# cubes = cube_generator(n)

# # Display the cubes
# print(f"Cubes of numbers from 1 to {n}:")
# for cube in cubes:
#     print(cube, end=" ")









'''Developer (programming language, experience)
Tester (testing tool, experience)
Requirements
Use constructor chaining with super().
Create two methods in the parent class:
display_basic_details()
display_contact_details()
Extend these methods in both child classes by adding their own details.
Use method chaining to display the complete information of a Developer and a Tester.'''

# Parent Class
# class Employee:

#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

#     def display_basic_details(self):
#         print("Name:", self.name)
#         return self

#     def display_contact_details(self):
#         print("Email:", self.email)
#         return self


# # Child Class - Developer
# class Developer(Employee):

#     def __init__(self, name, email, language, experience):
#         super().__init__(name, email)
#         self.language = language
#         self.experience = experience

#     def display_basic_details(self):
#         super().display_basic_details()
#         print("Programming Language:", self.language)
#         return self

#     def display_contact_details(self):
#         super().display_contact_details()
#         print("Experience:", self.experience, "years")
#         return self


# # Child Class - Tester
# class Tester(Employee):

#     def __init__(self, name, email, tool, experience):
#         super().__init__(name, email)
#         self.tool = tool
#         self.experience = experience

#     def display_basic_details(self):
#         super().display_basic_details()
#         print("Testing Tool:", self.tool)
#         return self

#     def display_contact_details(self):
#         super().display_contact_details()
#         print("Experience:", self.experience, "years")
#         return self


# # Developer Object
# dev = Developer("Rahul", "rahul@gmail.com", "Python", 3)

# # Tester Object
# test = Tester("Shikhar", "shikhar@gmail.com", "Selenium", 2)


# print("Developer Details")
# dev.display_basic_details().display_contact_details()

# print("\nTester Details")
# test.display_basic_details().display_contact_details()





'''Objective: Practice basic classes, lists of objects, and mutating object states.Task: Create two classes: Item and ShoppingCart.Item should have attributes: name, price, and quantity.ShoppingCart should hold a list of items and have methods to:add_item(item): Adds an Item object to the cart.remove_item(item_name): Removes an item from the cart by its name.calculate_total(): Calculates and returns the total price of all items in the cart.Expected Output: Students should be able to create 3 different items, add them to a cart, remove one, and print the correct final total balance.'''


# class Item:

#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity


# # ShoppingCart Class
# class ShoppingCart:

#     def __init__(self):
#         self.items = []

#     # Add item
#     def add_item(self, item):
#         self.items.append(item)

#     # Remove item by name
#     def remove_item(self, item_name):

#         for item in self.items:
#             if item.name == item_name:
#                 self.items.remove(item)
#                 print(item_name, "removed")
#                 break

#     # Calculate total price
#     def calculate_total(self):

#         total = 0

#         for item in self.items:
#             total = total + (item.price * item.quantity)

#         return total


# # Create items
# item1 = Item("Pen", 10, 2)
# item2 = Item("Book", 50, 1)
# item3 = Item("Pencil", 5, 4)

# # Create shopping cart
# cart = ShoppingCart()

# # Add items to cart
# cart.add_item(item1)
# cart.add_item(item2)
# cart.add_item(item3)

# # Remove one item
# cart.remove_item("Book")

# # Print final total
# print("Final Total =", cart.calculate_total())






# # Objective: Implement Inheritance and Method Overriding.Task: Create a base class called Member with attributes name and member_id.Create a subclass called Student that inherits from Member. Add a list attribute grades. Add a method display_info() that prints the student's name, ID, and their average grade.Create a subclass called Teacher that inherits from Member. Add an attribute subject. Override display_info() to print the teacher's name, ID, and the subject they teach.Expected Output: Students must instantiate both a Student and a Teacher object, call display_info() on both, and demonstrate that the correct overridden version runs for each


# #Parent Class
# class Member:

#     def __init__(self, name, member_id):
#         self.name = name
#         self.member_id = member_id


# # # Child Class - Student
# # class Student(Member):

# #     def __init__(self, name, member_id, grades):
# #         super().__init__(name, member_id)
# #         self.grades = grades

# #     def display_info(self):
# #         average = sum(self.grades) / len(self.grades)

# #         print("Name:", self.name)
# #         print("ID:", self.member_id)
# #         print("Average Grade:", average)


# # # Child Class - Teacher
# # class Teacher(Member):

# #     def __init__(self, name, member_id, subject):
# #         super().__init__(name, member_id)
# #         self.subject = subject

# #     def display_info(self):
# #         print("Name:", self.name)
# #         print("ID:", self.member_id)
# #         print("Subject:", self.subject)


# # # Create objects
# # s = Student("Rahul", 101, [80, 90, 85])
# # t = Teacher("Shikhar", 201, "Python")

# # # Display details
# # print("Student Details")
# # s.display_info()

# # print("\nTeacher Details")
# # t.display_info()








# # Objective: Master Encapsulation using private attributes and property getters/setters. 
# # Task: Create a SmartThermostat class.
# # Keep the __temperature attribute private so it cannot be changed directly from outside the class.
# # Use the @property decorator to create a getter for temperature.
# # Create a setter for temperature that includes validation rules: the temperature can only be set between 15°C and 30°C. If a value outside this range is given, print a warning or raise a ValueError without updating the value.
# # Expected Output: Students should show that they can read the temperature, change it safely within bounds, but are blocked with an error if they try to set it to an invalid temperature (like 50°C)

# class SmartThermostat:

#     def __init__(self, temperature):
#         self.__temperature = temperature   # Private attribute

#     # Getter
#     @property
#     def temperature(self):
#         return self.__temperature

#     # Setter
#     @temperature.setter
#     def temperature(self, value):

#         if 15 <= value <= 30:
#             self.__temperature = value
#             print("Temperature Updated")

#         else:
#             print("Temperature must be between 15°C and 30°C")


# # Create object
# thermostat = SmartThermostat(20) 

# # Read temperature
# print("Current Temperature:", thermostat.temperature)

# # Valid update
# thermostat.temperature = 25
# print("Updated Temperature:", thermostat.temperature)

# # Invalid update
# thermostat.temperature = 50
# print("Final Temperature:", thermostat.temperature)







# # Objective: Understand object collaboration, tracking shared class data, and basic abstraction.
# # Task: Design a system with a Book class and a Library class.
# # Book should track title, author, and a boolean is_borrowed flag.
# # Library should maintain a collection of books. Implement methods borrow_book(title) and return_book(title).
# # Bonus Challenge: Add a class-level variable total_borrowed_books in Library that increments every time a book is borrowed and decrements when returned.
# # Expected Output: A working script where multiple books are added to the library, a student borrows a book (marking it unavailable), and the system successfully tracks how many total books are currently checked out


# class Book:

#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.is_borrowed = False


# class Library:

#     total_borrowed_books = 0

#     def __init__(self):
#         self.books = []

#     def add_book(self, book):
#         self.books.append(book)

#     def borrow_book(self, title):

#         for book in self.books:

#             if book.title == title:

#                 if book.is_borrowed:
#                     print("Book already borrowed")

#                 else:
#                     book.is_borrowed = True
#                     Library.total_borrowed_books += 1
#                     print(title, "borrowed successfully")

#                 return

#         print("Book not found")

#     def return_book(self, title):

#         for book in self.books:

#             if book.title == title:

#                 if book.is_borrowed:
#                     book.is_borrowed = False
#                     Library.total_borrowed_books -= 1
#                     print(title, "returned successfully")

#                 else:
#                     print("Book was not borrowed")

#                 return

#         print("Book not found")


# # Create Library
# library = Library()

# # Add Books
# library.add_book(Book("Python", "John"))
# library.add_book(Book("Java", "Emma"))
# library.add_book(Book("C++", "David"))

# # Borrow Book
# library.borrow_book("Python")

# # Display borrowed count
# print("Total Borrowed Books:", Library.total_borrowed_books)

# # Return Book
# library.return_book("Python")

# # Display borrowed count again
# print("Total Borrowed Books:", Library.total_borrowed_books)








# Objective: Implement Polymorphism using operator overloading.Task: Create a Time class that represents hours and minutes, initialized as Time(hours, minutes).Overload the addition operator (_add) so that adding two Time objects together (e.g., t1 + t2) automatically handles minute overflow (e.g., 50 minutes + 20 minutes should add 1 to hours and leave 10 minutes).Overload the string representation (str_) so printing the object displays it neatly as HH:MM.Expected Output: Running print(Time(1, 45) + Time(2, 30)) should directly output 04:15 on the screen

# class Time:

#     def __init__(self, hours, minutes):
#         self.hours = hours
#         self.minutes = minutes

#     # Overload + operator
#     def __add__(self, other):

#         total_minutes = self.minutes + other.minutes
#         total_hours = self.hours + other.hours

#         # Handle minute overflow
#         if total_minutes >= 60:
#             total_hours += 1
#             total_minutes -= 60

#         return Time(total_hours, total_minutes)

#     # Display time as HH:MM
#     def __str__(self):

#         return f"{self.hours:02}:{self.minutes:02}"


# # Create objects
# t1 = Time(1, 45)
# t2 = Time(2, 30)

# # Add and display
# print(t1 + t2)  








# Objective: Practice writing basic anonymous lambda functions combined with map() to transform an iterable collection of numbers. [1, 2]
# Task: You are given a list of raw item prices: [19.99, 5.50, 100.00, 45.00]. Use a lambda function inside a map() call to apply a 10% discount to every item.
# Expected Output: A new list containing the discounted prices: [17.991, 4.95, 90.0, 40.5]. [1, 2]

# List of item prices
prices = [19.99, 5.50, 100.00, 45.00]
discounted_prices = list(map(lambda x: x * 0.9, prices))
print("Discounted Prices:", discounted_prices)






# Objective: Practice managing lists of objects, structural conditional logic, and state changes. [1]
# Task: Create a Room class and a Hotel class.
# Room should have attributes: room_number, room_type (e.g., Single, Double, Suite), price_per_night, and is_occupied (boolean, defaults to False).
# Hotel should contain a list of Room objects and include these methods:
# add_room(room): Adds a new room to the hotel inventory.
# check_in(room_type): Finds the first available room of that type, marks it as occupied, and returns the room number. If none are free, return a "No rooms available" message.
# check_out(room_number): Finds the room by its number and marks is_occupied back to False.
# Expected Output: Students instantiate a hotel, add 3-4 rooms, simulate checking guests in and out, and demonstrate that occupied rooms cannot be double-booked.
# Room Class

# class Room:

#     def __init__(self, room_number, room_type, price_per_night):
#         self.room_number = room_number
#         self.room_type = room_type
#         self.price_per_night = price_per_night
#         self.is_occupied = False


# # Hotel Class
# class Hotel:

#     def __init__(self):
#         self.rooms = []

#     # Add Room
#     def add_room(self, room):
#         self.rooms.append(room)

#     # Check In
#     def check_in(self, room_type):

#         for room in self.rooms:

#             if room.room_type == room_type and not room.is_occupied:

#                 room.is_occupied = True

#                 print("Room Booked:", room.room_number)

#                 return

#         print("No rooms available")

#     # Check Out
#     def check_out(self, room_number):

#         for room in self.rooms:

#             if room.room_number == room_number:

#                 room.is_occupied = False

#                 print("Room Checked Out:", room_number)

#                 return

#         print("Room not found")


# # Create Hotel
# hotel = Hotel()

# # Add Rooms
# hotel.add_room(Room(101, "Single", 1000))
# hotel.add_room(Room(102, "Single", 1000))
# hotel.add_room(Room(201, "Double", 2000))
# hotel.add_room(Room(301, "Suite", 5000))

# # Check In Guests
# hotel.check_in("Single")
# hotel.check_in("Single")
# hotel.check_in("Single")   # No room available

# # Check Out
# hotel.check_out(101)

# # Check In Again
# hotel.check_in("Single")






# Objective: Master Inheritance and structural Polymorphism where subclasses implement matching methods differently.
# Task: Create an abstract base class Employee using the abc module.
# The base class must have an abstract method called calculate_salary().
# Create a subclass SalariedEmployee with attributes name and monthly_salary. Implement calculate_salary() to return the flat monthly rate.
# Create a subclass HourlyEmployee with attributes name, hourly_rate, and hours_worked. Implement calculate_salary() to return hourly_rate * hours_worked.
# Expected Output: Students should loop through a mixed list containing both types of employee objects and print their names alongside their calculated salaries using a single unified loop.

from abc import ABC, abstractmethod


# Abstract Class
class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


# Salaried Employee
class SalariedEmployee(Employee):

    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


# Hourly Employee
class HourlyEmployee(Employee):

    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


# Create Employees
e1 = SalariedEmployee("Rahul", 50000)
e2 = HourlyEmployee("Shikhar", 500, 100)

# Store in a list
employees = [e1, e2]

# Single Loop
for emp in employees:

    print("Name:", emp.name)
    print("Salary:", emp.calculate_salary())
    print()