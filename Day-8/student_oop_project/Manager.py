from student import Student

def add_student():
    roll = input("Roll No: ")
    name = input("Name: ")
    marks = input("Marks: ")

    obj = Student(roll, name, marks)

    with open("students.txt", "a") as f:
        f.write(obj.to_text())

    print("✅ Student added")

def view_students():
    print("===== STUDENT LIST =====")
    try:
        with open("students.txt", "r") as f:
            print(f.read())
    except:
        print("No data yet.")

def menu():
    while True:
        print("""
1. Add Student
2. View Students
3. Exit
""")
        ch = input("Choose: ")

        if ch == "1":
            add_student()
        elif ch == "2":
            view_students()
        else:
            break

menu()
