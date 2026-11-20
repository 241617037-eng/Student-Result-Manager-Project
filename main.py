
students = {}
courses = {}
marks = {}

# Grade Calculation
def get_grade(mark):
    if mark >= 80:
        return "A+", 4.00
    elif mark >= 75:
        return "A", 3.75
    elif mark >= 70:
        return "A-", 3.50
    elif mark >= 65:
        return "B+", 3.25
    elif mark >= 60:
        return "B", 3.00
    elif mark >= 55:
        return "B-", 2.75
    elif mark >= 50:
        return "C+", 2.50
    elif mark >= 45:
        return "C", 2.25
    elif mark >= 40:
        return "D", 2.00
    else:
        return "F", 0.00

# Add Student
def add_student():
    sid = input("Student ID: ")

    if sid in students:
        print("Student ID already exists!")
        return

    students[sid] = input("Student Name: ")
    print("Student Added Successfully!")

# Add Course
def add_course():
    code = input("Course Code: ")

    if code in courses:
        print("Course already exists!")
        return

    title = input("Course Title: ")

    try:
        credit = float(input("Course Credit: "))
        if credit <= 0:
            print("Credit must be positive!")
            return
    except ValueError:
        print("Invalid Credit!")
        return

    courses[code] = (title, credit)
    print("Course Added Successfully!")

# Enter Marks
def enter_marks():
    sid = input("Student ID: ")
    code = input("Course Code: ")

    if sid not in students:
        print("Student not found!")
        return

    if code not in courses:
        print("Course not found!")
        return

    try:
        mark = float(input("Enter Marks (0-100): "))

        if mark < 0 or mark > 100:
            print("Marks must be between 0 and 100!")
            return

    except ValueError:
        print("Invalid Marks!")
        return

    marks[(sid, code)] = mark
    print("Marks Saved Successfully!")

# Show Result
def show_result():
    sid = input("Enter Student ID: ")

    if sid not in students:
        print("Student not found!")
        return

    print("\n========== RESULT SHEET ==========")
    print("Student ID:", sid)
    print("Student Name:", students[sid])
    print("----------------------------------")

    total_points = 0
    total_credits = 0

    for code, (title, credit) in courses.items():

        if (sid, code) in marks:
            mark = marks[(sid, code)]
            grade, point = get_grade(mark)

            print("\nCourse:", code, "-", title)
            print("Mark:", mark)
            print("Grade:", grade)
            print("Grade Point:", point)

            total_points += point * credit
            total_credits += credit

    if total_credits > 0:
        cgpa = total_points / total_credits
        print("\nCGPA:", round(cgpa, 2))
    else:
        print("\nNo marks available!")

    print("==================================")

# Main Menu
while True:
    print("\n===== STUDENT RESULT MANAGER =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Add Course")
    print("4. Show Courses")
    print("5. Enter Marks")
    print("6. Show Result Sheet")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        for sid, name in students.items():
            print(sid, "-", name)

    elif choice == "3":
        add_course()

    elif choice == "4":
        for code, (title, credit) in courses.items():
            print(code, title, credit)

    elif choice == "5":
        enter_marks()

    elif choice == "6":
        show_result()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
