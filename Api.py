from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    age: int
    email: str

students = []

@app.post("/students/", response_model=Student)
def create_student(student: Student):
    students.append(student)
    return student

@app.get("/students/", response_model=List[Student])
def read_students():
    return students

@app.get("/students/{student_id}", response_model=Student)
def read_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return updated_student
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{student_id}", response_model=Student)
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            return students.pop(index)
    raise HTTPException(status_code=404, detail="Student not found")
