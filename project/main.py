from operations import (
    add_student,
    view_students,
    search_student,
    update_marks,
    delete_student,
    highest_marks_student
)


while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Display Highest Marks Student")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_marks()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        highest_marks_student()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")