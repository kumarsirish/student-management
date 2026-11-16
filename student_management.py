
students = []


def add_student():
    roll_no = input("Enter Roll Number1: ")
    name = input("Enter Student Name: ")
    marks = float(input("Enter Marks: "))

    student = {
        "roll_no": roll_no,
        "name": name,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")


def display_students():
    if not students:
        print("No students available.")
        return

    print("\n--- Student Details ---")

    for student in students:
        print(
            f"Roll No: {student['roll_no']}, "
            f"Name: {student['name']}, "
            f"Marks: {student['marks']}"
        )


def search_student():
    roll_no = input("Enter Roll Number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("Student Found:", student)
            return

    print("Student not found.")


def calculate_average():
    if not students:
        print("No student records available.")
        return

    total = sum(student["marks"] for student in students)
    average = total / len(students)

    print(f"Average Marks: {average:.2f}")


def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Calculate Average Marks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            calculate_average()
        elif choice == "5":
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

