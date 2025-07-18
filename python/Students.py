class Student:
    def __init__(self, id, firstname, middlename, lastname, birthday):
        self.id = id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.birthday = birthday

    def display_info(self):
        fullname = f"{self.firstname} {self.middlename} {self.lastname}"
        print(f"id: {self.id}")
        print(f"full name: {fullname}")
        print(f"birthday: {self.birthday}")

std = [
    Student(1, "hoàng", "thị", "họ", "3-6-2000"),
    Student(2, "hoàng", "thị", "họ", "6-7-2005"),
    Student(3, "hoàng", "thị", "họ", "12-8-2002"),
    Student(4, "hoàng", "thị", "họ", "24-12-2009"),
    Student(5, "hoàng", "thị", "họ", "30-10-2001")
]

for student in std:
    student.display_info()  
    