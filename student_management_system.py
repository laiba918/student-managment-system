"""
Student Management System (Professional Version)
Author: Laiba
"""

students = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")

    students.append({
        "roll": roll,
        "name": name,
        "department": department
    })

    print("Student added successfully!")

def view_students():
    if not students:
        print("No student records found.")
        return

    print("\n--- Student List ---")
    for s in students:
        print(f"Roll: {s['roll']} | Name: {s['name']} | Dept: {s['department']}")

def edit_student():
    roll = input("Enter Roll Number to Edit: ")

    for s in students:
        if s["roll"] == roll:
            s["name"] = input("Enter New Name: ")
            s["department"] = input("Enter New Department: ")
            print("Student updated successfully!")
            return

    print("Student not found.")

def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted successfully!")
            return

    print("Student not found.")

def menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Edit Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            edit_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
