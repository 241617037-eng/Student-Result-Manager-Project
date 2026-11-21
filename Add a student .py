
students = {}

while True:
    print("\n=== STUDENT RESULT MANAGER ===")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        sid = input("Student ID: ")

        if sid in students:
            print("ID Already Exists!")
        else:
            name = input("Student Name: ")
            students[sid] = name
            print("Student Added Successfully!")

    elif choice == "2":
        for sid, name in students.items():
            print(sid, "-", name)

    elif choice == "3":
        break

    else:
        print("Invalid Choice!")
