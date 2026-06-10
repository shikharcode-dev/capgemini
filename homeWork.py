# # Question. create a resume builder using multilevel inheritance. create a class 1oth resume to store the personal details and 10th accedimic detiled 
# #creare a class resume 12th that inharit from resume 10th and store 12th accedmic detils.
# #create a class resume degree that inharit resume 12th class and store the accedmic details. use constructor chaining to insilized all the data 
# #use method to display the resume detailed at each level
# # create ojcect for 10,12th and degree class and display their resume.



# #Q. create an employee amangement system using Hierarchical inheritance create a parrent class employee with name email. create two child class tech team and support(mamagement and experiance) team (programing and experiance). using constructor chaining with super function. create two method in parent class display basic detailed and contact details both in parent. extand these two methos in child class by adding their own detailed. use method chaining to diaplay the information of this two child clas

# # create a procted variable in employee id and ascess in a inside a child 
# # create a procted variable in employee id and ascess in a inside a child 
# class employee:
#     def __init__(self,empid):
#         self._empid= empid  #protected variable  

# class manager(employee):
#     def display(self):
#         print("empid:", self._empid) 

# m = manager(223)
# m.display()


# # H.W.=  create a parent class vecheil with the method start engin now create a child class car bike. override the methos start engin.





# #Ex
# class student:
#     def __init__(self):
#         self.__marks= 95      #private variable

#     #Setter method
#     def set_marks(self, marks):
#         self.__marks= marks

#     #getter method
#     def get_marks(self):
#         return self.__marks
    
# #creating metho
# s= student()

# #setting value
# s.set_marks(98)

# #getting value
# print("Marks:",s.get_marks())

# # Property Decorator: A cleaner way to implement getters and setters in Python
# # Instead of calling methods like get_marks() and set_marks(), we can access attributes directly
# # The @property decorator makes a method behave like an attribute

# class Student:
#     def __init__(self):
#         self._marks = 95  # Using single underscore as convention for "internal use"
    
#     # Getter method - allows reading the value using student.marks
#     @property
#     def marks(self):
#         return self._marks
    
#     # Setter method - allows setting the value using student.marks = value
#     @marks.setter
#     def marks(self, value):
#         if value >= 0 and value <= 100:  # Adding validation
#             self._marks = value
#         else:
#             print("Invalid marks! Must be between 0 and 100")

# # Creating object
# s = Student()

# # Getting value - no need to call get_marks(), just use it like an attribute
# print("Marks:", s.marks)

# # Setting value - no need to call set_marks(), just assign directly
# s.marks = 98
# print("Updated Marks:", s.marks)

# # Validation in action
# s.marks = 150  # This will print error message.


# #test Q come on saturday
# #Q. test cases question, 







# # Alternative method using regular function
# def check_char_in_string(s, char):
#     return char in s

# print(check_char_in_string("hello", "e"))
# print(check_char_in_string("hello", "z"))
# print(check_char_in_string("python", "p"))







# #Q. WAP to check the given is string is keyword or not
# import keyword
# is_keyword = lambda s: keyword.iskeyword(s)
# print(is_keyword("if"))      
# print(is_keyword("hello"))   
# print(is_keyword("for"))     
# print(is_keyword("class")) 


# WAP to return square if collection has even length, otherwise return cube
# square_or_cube = lambda collection: len(collection) ** 2 if len(collection) % 2 == 0 else len(collection) ** 3
# print(square_or_cube([1, 2, 3, 4]))      
# print(square_or_cube([1, 2, 3]))         
# print(square_or_cube("hello"))           
# print(square_or_cube("test")) 



# numbers_to_squares = lambda nums: {num: num**2 for num in nums}
# print(numbers_to_squares([1, 2, 3, 4, 5]))
# print(numbers_to_squares([10, 20, 30]))
# print(numbers_to_squares(range(1, 6)))






# # Method 2: Using map with custom function (more readable)
# numbers = ['123', '345', '764']
# def reverse_and_convert(string_num):
#     reversed_string = string_num[::-1]  # Reverse the string using slicing
#     return int(reversed_string)  # Convert to integer

# result2 = list(map(reverse_and_convert, numbers))

# print("\nUsing custom function:")
# print("Original String List:", numbers)
# print("Reversed Integer List:", result2)

# Explanation:
# x[::-1] reverses the string ('123' becomes '321')
# int() converts the reversed string to integer
# map() applies this operation to every element in the list





# f = open("student.txt", "w")
# f.write("Shikhar")
# f.close()







# l = [1,-5,-6,23]

# # Filter positive numbers and calculate sum
# result = sum(list(filter(lambda x: x > 0, l)))

# print("Original List:", l)
# print("Sum of Positive Numbers:", result)






# Create a parent class Animal with a method eat().
# Create a child class Dog that inherits from Animal.
# Add a method bark() in the child class.
# Create an object of Dog and call both methods.
class Animal:
    def eat(self):
        print("The animal is eating")
class Dog(Animal):
    def bark(self):
        print("The dog is barking: Woof! Woof!")

my_dog = Dog()
my_dog.eat()   
my_dog.bark()





# Create a parent class Employee.
# Initialize:
# employee name
# salary
# Create child class Developer.
# Add:
# programming language
# Display all details.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display_details(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    
    def display_details(self):
        super().display_details()
        print("Programming Language:", self.programming_language)
dev = Developer("John", 50000, "Python")
dev.display_details()