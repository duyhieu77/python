from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

app = FastAPI()

DATABASE_URL = "mysql+pymysql://root:password@localhost/employee_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(50))
    middlename = Column(String(50), nullable=True)
    lastname = Column(String(50))
    birthday = Column(Date)
    phone = Column(String(15))
    email = Column(String(100), unique=True)

Base.metadata.create_all(bind=engine)

class EmployeeCreate(BaseModel):
    firstname: str
    middlename: str = None
    lastname: str
    birthday: str
    phone: str
    email: str

class EmployeeResponse(EmployeeCreate):
    id: int

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/employees/", response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate, db: Session = next(get_db())):
    db_employee = Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@app.get("/employees/", response_model=list[EmployeeResponse])
def read_employees(skip: int = 0, limit: int = 10, db: Session = next(get_db())):
    employees = db.query(Employee).offset(skip).limit(limit).all()
    return employees

@app.get("/employees/{employee_id}", response_model=EmployeeResponse)
def read_employee(employee_id: int, db: Session = next(get_db())):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@app.put("/employees/{employee_id}", response_model=EmployeeResponse)
def update_employee(employee_id: int, employee: EmployeeCreate, db: Session = next(get_db())):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    for key, value in employee.dict().items():
        setattr(db_employee, key, value)
    
    db.commit()
    db.refresh(db_employee)
    return db_employee

@app.delete("/employees/{employee_id}", response_model=dict)
def delete_employee(employee_id: int, db: Session = next(get_db())):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(db_employee)
    db.commit()
    return {"detail": "Employee deleted successfully"}