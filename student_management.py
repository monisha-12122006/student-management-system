students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print("Student Added Successfully!")

    elif choice == "2":
        print("\nStudent List:")
        for student in students:
            print(student)

    elif choice == "3":
        name = input("Enter student name to delete: ")

        if name in students:
            students.remove(name)
            print("Student Deleted Successfully!")
        else:
            print("Student Not Found!")

    elif choice == "4":
        name = input("Enter student name to search: ")

        if name in students:
            print("Student Found!")
        else:
            print("Student Not Found!")

    elif choice == "5":
        name = input("Enter student name to update: ")
        if name in students:
            new_name = input("Enter new student name: ")
            index = students.index(name)
            students[index] = new_name
            print("Student Updated Successfully!")
        else:
            print("Student Not Found!")

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")