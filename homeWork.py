# Question. create a resume builder using multilevel inheritance. create a class 1oth resume to store the personal details and 10th accedimic detiled 
#creare a class resume 12th that inharit from resume 10th and store 12th accedmic detils.
#create a class resume degree that inharit resume 12th class and store the accedmic details. use constructor chaining to insilized all the data 
#use method to display the resume detailed at each level
# create ojcect for 10,12th and degree class and display their resume.



#Q. create an employee amangement system using Hierarchical inheritance create a parrent class employee with name email. create two child class tech team and support(mamagement and experiance) team (programing and experiance). using constructor chaining with super function. create two method in parent class display basic detailed and contact details both in parent. extand these two methos in child class by adding their own detailed. use method chaining to diaplay the information of this two child clas

# create a procted variable in employee id and ascess in a inside a child 
# create a procted variable in employee id and ascess in a inside a child 
class employee:
    def __init__(self,empid):
        self._empid= empid  #protected variable  

class manager(employee):
    def display(self):
        print("empid:", self._empid) 

m = manager(223)
m.display()


# H.W.=  create a parent class vecheil with the method start engin now create a child class car bike. override the methos start engin.





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

# Property Decorator: A cleaner way to implement getters and setters in Python
# Instead of calling methods like get_marks() and set_marks(), we can access attributes directly
# The @property decorator makes a method behave like an attribute

class Student:
    def __init__(self):
        self._marks = 95  # Using single underscore as convention for "internal use"
    
    # Getter method - allows reading the value using student.marks
    @property
    def marks(self):
        return self._marks
    
    # Setter method - allows setting the value using student.marks = value
    @marks.setter
    def marks(self, value):
        if value >= 0 and value <= 100:  # Adding validation
            self._marks = value
        else:
            print("Invalid marks! Must be between 0 and 100")

# Creating object
s = Student()

# Getting value - no need to call get_marks(), just use it like an attribute
print("Marks:", s.marks)

# Setting value - no need to call set_marks(), just assign directly
s.marks = 98
print("Updated Marks:", s.marks)

# Validation in action
s.marks = 150  # This will print error message.


#test Q come on saturday
#Q. test cases question, 