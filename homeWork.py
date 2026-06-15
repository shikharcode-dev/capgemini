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

# Generator function to yield cubes of numbers from 1 to n
def cube_generator(n):
    # Loop through numbers from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Yield the cube of current number (i^3)
        yield i ** 3

# Accept input from user
n = int(input("Enter a number: "))

# Create generator object
cubes = cube_generator(n)

# Display the cubes
print(f"Cubes of numbers from 1 to {n}:")
for cube in cubes:
    print(cube, end=" ")
