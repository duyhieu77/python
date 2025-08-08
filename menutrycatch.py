import json
import matplotlib.pyplot as plt

class Student:
    def __init__(self, student_id, name, gpa):
        self.student_id = student_id
        self.name = name
        self.gpa = gpa

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "gpa": self.gpa
        }

students = []

def add_student():
    try:
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        gpa = float(input("Enter student GPA: "))
        students.append(Student(student_id, name, gpa))
        print("Student added successfully!")
    except ValueError:
        print("Error: Please enter a valid GPA format.")

def display_students():
    if not students:
        print("No students to display.")
        return
    for student in students:
        print(f"ID: {student.student_id}, Name: {student.name}, GPA: {student.gpa}")

def display_top_students():
    top_students = [s for s in students if s.gpa >= 8]
    if not top_students:
        print("No top students found.")
        return
    for student in top_students:
        print(f"ID: {student.student_id}, Name: {student.name}, GPA: {student.gpa}")

def save_to_file():
    try:
        with open("students.json", "w") as file:
            json.dump([s.to_dict() for s in students], file)
        print("Student information has been saved to file.")
    except Exception as e:
        print(f"Error while saving file: {e}")

def view_student_info():
    try:
        student_id = input("Enter student ID to view information: ")
        student = next((s for s in students if s.student_id == student_id), None)
        if student:
            print(f"ID: {student.student_id}, Name: {student.name}, GPA: {student.gpa}")
        else:
            print("No student found with this ID.")
    except Exception as e:
        print(f"Error: {e}")

def plot_gpa():
    if not students:
        print("No data available to plot.")
        return
    ids = [s.student_id for s in students]
    gpas = [s.gpa for s in students]

    plt.bar(ids, gpas, color='blue')
    plt.xlabel('Student ID')
    plt.ylabel('GPA')
    plt.title('GPA Chart of Students')
    plt.show()

def main():
    while True:
        print("\nMenu:")
        print("1. Add student")
        print("2. Display all students")
        print("3. Display top students with GPA >= 8")
        print("4. Save to file")
        print("5. View student information by ID")
        print("6. Plot GPA chart")
        print("7. Exit program")

        choice = input("Choose a function (1-7): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            display_top_students()
        elif choice == "4":
            save_to_file()
        elif choice == "5":
            view_student_info()
        elif choice == "6":
            plot_gpa()
        elif choice == "7":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()