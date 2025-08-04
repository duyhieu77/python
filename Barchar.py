import matplotlib.pyplot as plt
from datetime import datetime

class Person:
    def __init__(self, firstname, middlename, lastname, birthday, address, phone):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.birthday = datetime.strptime(birthday, "%Y-%m-%d")
        self.address = address
        self.phone = phone

    def age(self):
        today = datetime.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))


class Student(Person):
    def __init__(self, firstname, middlename, lastname, birthday, address, phone, regno, gpa):
        super().__init__(firstname, middlename, lastname, birthday, address, phone)
        self.regno = regno
        self.gpa = gpa


students = []


def add_student():
    firstname = input("Enter first name: ")
    middlename = input("Enter middle name: ")
    lastname = input("Enter last name: ")
    birthday = input("Enter birthday (YYYY-MM-DD): ")
    address = input("Enter address: ")
    phone = input("Enter phone number: ")
    regno = input("Enter student registration number: ")
    gpa = float(input("Enter GPA: "))
    student = Student(firstname, middlename, lastname, birthday, address, phone, regno, gpa)
    students.append(student)
    print("Student has been added.")


def display_students():
    for s in students:
        print(f"{s.firstname} {s.middlename} {s.lastname}, GPA: {s.gpa}, Age: {s.age()}")


def filter_students_above_22():
    filtered = [s for s in students if s.age() > 22]
    for s in filtered:
        print(f"{s.firstname} {s.middlename} {s.lastname}, Age: {s.age()}")


def filter_students_under_22_with_high_gpa():
    filtered = [s for s in students if s.age() < 22 and 80 <= s.gpa <= 100]
    for s in filtered:
        print(f"{s.firstname} {s.middlename} {s.lastname}, GPA: {s.gpa}")


def save_students_to_file():
    with open("students.txt", "w") as file:
        for s in students:
            file.write(f"{s.firstname} {s.middlename} {s.lastname}, {s.birthday}, {s.address}, {s.phone}, {s.regno}, {s.gpa}\n")
    print("The list of students has been saved to file.")


def plot_gpa_chart():
    names = [f"{s.firstname} {s.middlename} {s.lastname}" for s in students]
    gpas = [s.gpa for s in students]

    plt.bar(names, gpas)
    plt.xlabel('Student Name')
    plt.ylabel('GPA')
    plt.title('GPA Chart of Students')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def menu():
    while True:
        print("\nMenu:")
        print("1. Add student")
        print("2. Display list of students")
        print("3. Filter students older than 22")
        print("4. Filter students with GPA between 80-100 and younger than 22")
        print("5. Save the entire list of students to a text file")
        print("6. Draw bar chart")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            filter_students_above_22()
        elif choice == '4':
            filter_students_under_22_with_high_gpa()
        elif choice == '5':
            save_students_to_file()
        elif choice == '6':
            plot_gpa_chart()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()