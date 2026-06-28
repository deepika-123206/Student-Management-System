students = {}

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        marks = input("Enter Marks: ")

        students[roll_no] = {
            "Name": name,
            "Marks": marks
        }
        print("Student Added Successfully!")

    elif choice == "2":
        roll_no = input("Enter Roll Number to Search: ")

        if roll_no in students:
            print("Roll No :", roll_no)
            print("Name :", students[roll_no]["Name"])
            print("Marks :", students[roll_no]["Marks"])
        else:
            print("Student Not Found!")

    elif choice == "3":
        roll_no = input("Enter Roll Number to Update: ")

        if roll_no in students:
            name = input("Enter New Name: ")
            marks = input("Enter New Marks: ")

            students[roll_no]["Name"] = name
            students[roll_no]["Marks"] = marks

            print("Student Updated Successfully!")
        else:
            print("Student Not Found!")

    elif choice == "4":
        roll_no = input("Enter Roll Number to Delete: ")

        if roll_no in students:
            del students[roll_no]
            print("Student Deleted Successfully!")
        else:
            print("Student Not Found!")

    elif choice == "5":
        if len(students) == 0:
            print("No Students Available!")
        else:
            print("\n----- Student Details -----")
            for roll_no, details in students.items():
                print("Roll No :", roll_no)
                print("Name :", details["Name"])
                print("Marks :", details["Marks"])
                print("----------------------")

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
