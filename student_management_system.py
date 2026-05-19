# Student Management System
# Simple Python Mini Project for Resume and GitHub

students = []


def add_student():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    marks = input("Enter Marks: ")

    student = {
        "Name": name,
        "Roll Number": roll,
        "Marks": marks
    }

    students.append(student)
    print("\nStudent Added Successfully!\n")


def view_students():
    if len(students) == 0:
        print("\nNo Student Records Found\n")
    else:
        print("\nStudent Records:\n")
        for i, student in enumerate(students, start=1):
            print(f"Student {i}")
            print(f"Name : {student['Name']}")
            print(f"Roll Number : {student['Roll Number']}")
            print(f"Marks : {student['Marks']}")
            print("----------------------")


def search_student():
    roll = input("Enter Roll Number to Search: ")

    found = False

    for student in students:
        if student["Roll Number"] == roll:
            print("\nStudent Found:\n")
            print(f"Name : {student['Name']}")
            print(f"Roll Number : {student['Roll Number']}")
            print(f"Marks : {student['Marks']}")
            found = True
            break

    if not found:
        print("\nStudent Not Found\n")


def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    for student in students:
        if student["Roll Number"] == roll:
            students.remove(student)
            print("\nStudent Deleted Successfully\n")
            return

    print("\nStudent Not Found\n")


while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == '1':
        add_student()

    elif choice == '2':
        view_students()

    elif choice == '3':
        search_student()

    elif choice == '4':
        delete_student()

    elif choice == '5':
        print("\nThank You! Exiting Program...")
        break

    else:
        print("\nInvalid Choice! Please Try Again.\n")
