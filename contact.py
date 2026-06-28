contacts = {}

while True:
    print("\n===== CONTACT LIST SYSTEM =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        number = input("Enter Phone Number: ")
        contacts[name] = number
        print("Contact Added Successfully!")

    elif choice == "2":
        name = input("Enter Name to Search: ")
        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact Not Found!")

    elif choice == "3":
        name = input("Enter Name to Update: ")
        if name in contacts:
            number = input("Enter New Number: ")
            contacts[name] = number
            print("Contact Updated Successfully!")
        else:
            print("Contact Not Found!")

    elif choice == "4":
        name = input("Enter Name to Delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact Deleted Successfully!")
        else:
            print("Contact Not Found!")

    elif choice == "5":
        if len(contacts) == 0:
            print("No Contacts Available!")
        else:
            print("\n----- Contact List -----")
            for name, number in contacts.items():
                print(name, ":", number)

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
