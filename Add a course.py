
students = {}
courses = {}

while True:
    print("\n=== STUDENT RESULT MANAGER ===")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Add Course")
    print("4. Show Courses")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        sid = input("Student ID: ")
        if sid in students:
            print("ID Already Exists!")
        else:
            students[sid] = input("Student Name: ")
            print("Student Added!")

    elif choice == "2":
        for sid, name in students.items():
            print(sid, "-", name)

    elif choice == "3":
        code = input("Course Code: ")
        if code in courses:
            print("Course Already Exists!")
        else:
            title = input("Course Title: ")
            credit = float(input("Course Credit: "))
            if credit <= 0:
                print("Invalid Credit!")
            else:
                courses[code] = (title, credit)
                print("Course Added!")

    elif choice == "4":
        for code, (title, credit) in courses.items():
            print(code, title, credit)

    elif choice == "5":
        break

    else:
        print("Invalid Choice!")
