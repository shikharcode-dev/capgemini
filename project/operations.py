from student import Student
from data import students


# Add Student
def add_student():

    student_id = input("Enter Student ID: ")

    # Check if ID already exists
    for student in students:

        if student.student_id == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Name: ")

    age = int(input("Enter Age: "))

    marks = float(input("Enter Marks: "))

    student = Student(student_id, name, age, marks)

    students.append(student)

    print("Student Added Successfully")


# View All Students
def view_students():

    if len(students) == 0:
        print("No students found")
        return

    for student in students:

        print("\nStudent ID:", student.student_id)
        print("Name:", student.name)
        print("Age:", student.age)
        print("Marks:", student.marks)


# Search Student by ID
def search_student():

    student_id = input("Enter Student ID to Search: ")

    for student in students:

        if student.student_id == student_id:

            print("\nStudent Found")
            print("Student ID:", student.student_id)
            print("Name:", student.name)
            print("Age:", student.age)
            print("Marks:", student.marks)

            return

    print("Student Not Found")


# Update Student Marks
def update_marks():

    student_id = input("Enter Student ID: ")

    for student in students:

        if student.student_id == student_id:

            new_marks = float(input("Enter New Marks: "))

            student.marks = new_marks

            print("Marks Updated Successfully")

            return

    print("Student Not Found")


# Delete Student
def delete_student():

    student_id = input("Enter Student ID to Delete: ")

    for student in students:

        if student.student_id == student_id:

            students.remove(student)

            print("Student Deleted Successfully")

            return

    print("Student Not Found")


# Display Student with Highest Marks
def highest_marks_student():

    if len(students) == 0:
        print("No students found")
        return

    top_student = students[0]

    for student in students:

        if student.marks > top_student.marks:
            top_student = student

    print("\nStudent with Highest Marks")
    print("Student ID:", top_student.student_id)
    print("Name:", top_student.name)
    print("Age:", top_student.age)
    print("Marks:", top_student.marks)