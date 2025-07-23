class Student:
    def __init__(self, name, age, points):
        self.name = name
        self.age = age
        self.points = points

    def average_point(self):
        return sum(self.points) / len(self.points) if self.points else 0

    def find_highest_student_point(students):
        highest_student = max(students, key=lambda std: std.average_point(), default=None)
        return highest_student

    def filter_std_above8(students, threshold=8):
        return [std for std in students if std.average_point() > threshold]

students = [
    Student("A", 20, [8, 9, 10]),
    Student("B", 21, [7, 6, 5]),
    Student("C", 22, [9, 8, 10]),
]

highest_std = Student.find_highest_student_point(students) 
if highest_std:
    print(f"Student with highest GPA: {highest_std.name} with GPA of {highest_std.average_point()}")

high_points = Student.filter_std_above8(students)
print("Students with GPA > 8:")
for student in high_points:
    print(f"{student.name} with GPA {student.average_point()}")