# # # create one class = school, with 3 class member and 3 obj with 3 obj member
# # class School:
# #     name = "ABC School"
# #     location = "New York"
# #     traner = "PJ"

# #     object1 = "Student"
# #     object2 = "Teacher"
# #     object3 = "Principal"

# # school1 = School()
# # school2 = School()
# # school3 = School()
 
# # school1.name = "XYZ School"
# # school1.location = "Los Angeles"
# # school1.traner = "John"

# # print(school1.name)
# # print(school1.location)
# # print(school1.traner)


# # # when multiples things are happen we use constructor or magic method __init__ to avoid the problem of multiple object creation 

# # class School:
# #     def __init__(self, name, age, section, location, rollno):
# #         self.name = name
# #         self.age = age
# #         self.section = section
# #         self.location = location
# #         self.rollno = rollno

# # # creating object for school class 
# # student1 = School("Luffy", 20, "A", "New York", 1)
# # student2 = School("Ichigo", 19, "B", "L.A.", 2)
# # student3 = School("Aizen", 21, "C", "Maxico", 3)

# # print(student1.name, student1.age, student1.section, student1.location, student1.rollno)
# # print(student2.name, student2.age, student2.section, student2.location, student2.rollno)
# # print(student3.name, student3.age, student3.section, student3.location, student3.rollno)

# # Q create class mobile, 2 class member, 2 object and 3 objject member
# class Mobile:
#     def __init__(self, brand, model, price):
#         self.brand = brand  
#         self.model = model
#         self.price = price

# mobile1 = Mobile("Apple", "iPhone 13", 999)
# mobile2 = Mobile("Samsung", "Galaxy S21", 799)

# print(mobile1.brand, mobile1.model, mobile1.price)
# print(mobile2.brand, mobile2.model, mobile2.price)

# # so in the above Q what are the 2 class member, 2 object and 3 object member
# # class member = brand, model
# # object = mobile1, mobile2
# # object member = brand, model, price, ok my Q is? i give only 2 class member but i have 3 object member, how is it possible?
# # in the above code, we have defined 2 class members (brand and model) in the __init__ method, but we also have a third object member (price) that is being initialized in the constructor. This is possible because the __init__ method can accept any number of parameters, and we can choose to initialize as many object members as we want within it. The class members are defined as parameters in the __init__ method, and we can add additional parameters for object members as needed. In this case, we have added the price parameter to initialize the price object member for each mobile instance.

# # why output give error?
# # The output gives an error because we have not defined the price parameter in the __init__ method of the Mobile class. When we try to access mobile1.price and mobile2.price, it raises an AttributeError because the price attribute does not exist for those objects. To fix this error, we need to add the price parameter to the __init__ method and initialize it for each mobile instance.
# # so that mean Q is wrong because we have only 2 class member but we have 3 object member, so we need to add price in class member to avoid error aa?
# # Yes, to avoid the error, we need to add the price parameter to the __init__ method of the Mobile class. This way, we can initialize the price object member for each mobile instance without any issues. The corrected code would look like this:

# # method and its types
# # method is a function that is defined inside a class and is used to perform a specific task
# # types of method
# # 1. Object , class and static method
# # object method is used to perform some modification on the object member and it is called by the object of the class
# #syntax of object method
# #class class_name:
# # def method_name(self, parameters):
#     #code to perform some task
# #obj name

# #Example of object method
# # class school:

# #     def __init__(self):
# #         Sname = "ABC School"
# #         Slocation = "New York"

# #     def display(self):
# #         print("School Name:", self.Sname)
# #         print("School Location:", self.Slocation)

# # #creating object for school class
# # s1 = school()
# # s1.Sname = "ABC School"
# # s1.Slocation = "New York"
# # s1.display() # or School.display(s1) both are same


# # i all ready created class mobile now i have to display the details of mobile using object method, how can i do that?
# class Mobile:
#     def __init__(self, brand, model, price):
#         self.brand = brand  
#         self.model = model
#         self.price = price

#     def display_details(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Price:", self.price)

# mobile1 = Mobile("Apple", "iPhone 13", 999)
# mobile1.display_details()


# # now i have to modify the age of the student 
# class School:
#     def __init__(self, name, age, section, location, rollno):
#         self.name = name
#         self.age = age
#         self.section = section
#         self.location = location
#         self.rollno = rollno

#     def modify_age(self, new_age):
#         self.age = new_age

# student1 = School("Luffy", 20, "A", "New York", 1)
# print("Before modification:", student1.age)

# student1.modify_age(21)
# print("After modification:", student1.age)


# # lets modify the price of the mobile using object method
# class Mobile:
#     def __init__(self, brand, model, price):
#         self.brand = brand  
#         self.model = model
#         self.price = price

#     def modify_price(self, new_price):
#         self.price = new_price

# mobile1 = Mobile("Apple", "iPhone 13", 999)
# print("Before modification:", mobile1.price)

# mobile1.modify_price(899)
# print("After modification:", mobile1.price)

# # Q. create 1 class called employee, 1 class member, 2object with 3 obj member = employee name, employee id, employee salary and display all properties and modify the salary of the employee using object method
# class Employee:
#     def __init__(self, name, emp_id, salary):
#         self.name = name
#         self.emp_id = emp_id
#         self.salary = salary

#     def display_details(self):
#         print("Employee Name:", self.name)
#         print("Employee ID:", self.emp_id)
#         print("Employee Salary:", self.salary)

#     def modify_salary(self, new_salary):
#         self.salary = new_salary

# employee1 = Employee("Luffy", 12345, 50000)
# employee1.display_details()

# employee1.modify_salary(55000)
# print("After modification:", employee1.salary)

# create one class bank and name and create 2 object as customer and create constructor as account holder and balance by 1k and creat one amount to add balance and shown the current balance and also shown then balnce after adding the amount
# now widraw the amount 

# class Bank:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance

#     def display(self):
#         print("Account Holder:", self.account_holder)
#         print("Current Balance:", self.balance)

#     def add_balance(self, amount):
#         self.balance += amount
#         print("Balance after adding amount:", self.balance)

#     def withdraw_amount(self, withdraw):
#         withdraw_amount = self.balance - withdraw
#         print("Balance after withdrawing amount:", withdraw_amount)

# customer1 = Bank("Luffy", 1000)
# customer1.display()
# customer1.add_balance(500)
# customer1.withdraw_amount(300)

# the way mam did
# class bank:
#     branch = "SBI"
#     IFSC = "SBIN0002449"
#     Branch = "Chnadigarh"

#     def __init__(self, cname, pno, balance, ac_no):
#         self.cname = cname
#         self.pno = pno
#         self.balance = balance
#         self.ac_no = ac_no

#     def display(self):
#         print("Customer Name:", self.cname)
#         print("Phone Number:", self.pno)
#         print("Balance:", self.balance)
#         print("Account Number:", self.ac_no)
#         print("Branch:", self.branch)
#         print("IFSC:", self.IFSC)
#         print("Branch:", self.Branch)

#     def deposit(self, amount):
#         self.balance += amount
#         print("Balance after deposit:", self.balance)

#     def withdraw(self, amount):
#         self.balance -= amount
#         print("Balance after withdrawal:", self.balance)
    
#     @classmethod # class method is used to perform some modification on the class member and it is called by the class name @classmethod is used to define a method that belongs to the class rather than an instance of the class. It can be called using the class name and can modify class-level attributes. The first parameter of a class method is conventionally named 'cls', which refers to the class itself. Class methods are defined using the @classmethod decorator.
#     def display_branch(cls):
#         print("Branch:", cls.branch)
#         print("IFSC:", cls.IFSC)
#         print("Branch:", cls.Branch)
#     @classmethod
#     def ch_branch(cls, new_branch):
#         cls.branch = new_branch
#         print("Branch name changed to:", cls.branch)

# # object creation
# customer1 = bank("Luffy", 1234567890, 1000, "SBIN0002449")
# customer1.display()
# customer1.deposit(500)
# customer1.withdraw(300)
# bank.display_branch()
# bank.ch_branch("HDFC")
# bank.display_branch()


#Q. create a class called shoping and add product if user buy product if 8 items and reduces amount. add item, remove item if not in stock, or defected item, and also display if item not there show outof stock.
class Shopping:
    stock = 8   # Class variable

    @classmethod
    def add_item(cls, quantity):
        cls.stock += quantity
        print(quantity, "items added.")
        print("Current Stock:", cls.stock)

    @classmethod
    def buy_item(cls, quantity):
        if quantity <= cls.stock:
            cls.stock -= quantity
            print(quantity, "items purchased.")
            print("Remaining Stock:", cls.stock)
        else:
            print("Out of Stock!")

    @classmethod
    def remove_item(cls, quantity):
        if quantity <= cls.stock:
            cls.stock -= quantity
            print(quantity, "defected items removed.")
            print("Remaining Stock:", cls.stock)
        else:
            print("Not enough items in stock!")

    @classmethod
    def display_stock(cls):
        if cls.stock > 0:
            print("Current Stock:", cls.stock)
        else:
            print("Out of Stock!")


# Calling class methods
Shopping.display_stock()

Shopping.buy_item(3)

Shopping.add_item(5)

Shopping.remove_item(2)

Shopping.display_stock()

