import json

FILE_NAME = "students.json"

# Load students from file
try:
    with open(FILE_NAME, "r") as file:
        students = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    students = []

# Save students


def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


while True:
    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        roll = input("Enter Roll Number: ")

        # Check duplicate roll number
        found = False
        for student in students:
            if student["roll"] == roll:
                found = True
                break

        if found:
            print("Student with this roll number already exists.")
        else:
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            department = input("Enter Department: ")

            students.append({
                "roll": roll,
                "name": name,
                "age": age,
                "department": department
            })

            save_students()
            print("Student added successfully!")

    # View Students
    elif choice == "2":

        if len(students) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records")
            print("-" * 60)

            for student in students:
                print(f"Roll No   : {student['roll']}")
                print(f"Name      : {student['name']}")
                print(f"Age       : {student['age']}")
                print(f"Department: {student['department']}")
                print("-" * 60)

    # Update Student
    elif choice == "3":

        roll = input("Enter Roll Number to update: ")

        found = False

        for student in students:

            if student["roll"] == roll:

                student["name"] = input("Enter New Name: ")
                student["age"] = input("Enter New Age: ")
                student["department"] = input("Enter New Department: ")

                save_students()

                print("Student updated successfully!")

                found = True
                break

        if not found:
            print("Student not found.")

    # Delete Student
    elif choice == "4":

        roll = input("Enter Roll Number to delete: ")

        found = False

        for student in students:

            if student["roll"] == roll:

                students.remove(student)

                save_students()

                print("Student deleted successfully!")

                found = True
                break

        if not found:
            print("Student not found.")

    # Exit
    elif choice == "5":

        print("Thank you!")

        break

    else:
        print("Invalid choice.")