from pathlib import Path
DATA_FILE = Path(__file__).resolve().parent / "nisha.txt"
def read_students():
    students = []
    if not DATA_FILE.exists():
        return students
    with DATA_FILE.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = [part.strip() for part in line.split(",", 2)]
            if len(parts) == 3:
                students.append(parts)
    return students
def add_student():
    name = input("Enter student name: ").strip()
    course = input("Enter course: ").strip()
    cgpa = input("Enter CGPA: ").strip()
    with DATA_FILE.open("a", encoding="utf-8") as f:
        f.write(f"{name},{course},{cgpa}\n")
    print("Student added.")
def view_students():
    students = read_students()
    if not students:
        print("No students found.")
        return
    for name, course, cgpa in students:
        print("Name:", name, "Course:", course, "CGPA:", cgpa)
def search_student():
    search_name = input("Enter student name: ").strip().lower()
    if not search_name:
        print("Please enter a name.")
        return
    students = read_students()
    if not students:
        print("No student records yet.")
        return
    results = [s for s in students if search_name in s[0].lower()]
    if not results:
        print("Student not found.")
        return
    for name, course, cgpa in results:
        print("Student found:")
        print("Name:", name)
        print("Course:", course)
        print("CGPA:", cgpa)

def count_students():
    print("Total students:", len(read_students()))
while True:
    print("\n1 Add student")
    print("2 View students")
    print("3 Search student")
    print("4 Count students")
    print("5 Exit")
    choice = input("Choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        count_students()
    elif choice == "5":
        print("Bye.")
        break
    else:
        print("Invalid choice.")
